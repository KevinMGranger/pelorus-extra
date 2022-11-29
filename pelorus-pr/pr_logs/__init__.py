#!/usr/bin/env python3

import json
import re
import subprocess
from typing import Iterable, Optional
from google.cloud import storage

import click
from dataclasses import dataclass
import sys
from pathlib import PurePath


def get_e2e_log_blob(pr: str, test: str) -> storage.Blob:
    PULLS_DIR = PurePath("pr-logs/pull/konveyor_pelorus")
    TEST_NAME_TEMPLATE = "pull-ci-konveyor-pelorus-master-{test}-e2e-openshift"

    LATEST_BUILD_FILENAME = "latest-build.txt"

    BUILD_LOG_SUBPATH = PurePath("artifacts/e2e-openshift/e2e/build-log.txt")

    artifact_root_dir = PULLS_DIR / pr / TEST_NAME_TEMPLATE.format(test=test)

    client = storage.Client.create_anonymous_client()
    bucket = client.bucket("origin-ci-test")

    latest_build_id_blob = bucket.blob(str(artifact_root_dir / LATEST_BUILD_FILENAME))
    latest_build_id = latest_build_id_blob.download_as_text()

    build_log_path = str(artifact_root_dir / latest_build_id / BUILD_LOG_SUBPATH)
    return bucket.blob(build_log_path)


@dataclass
class PRStatusResult:
    name: str
    state: str
    description: str

    def __str__(self):
        # EXAMPLE_NAME_LEN = 26 # len("ci/prow/4.10-e2e-openshift")
        # MAX_STATE_LEN = 7 # len("pending")
        # TODO: are there other states?

        description = self.description.replace("\n", r"\n")

        return f"{self.name:26}{' '*4}{self.state:7}{' '*4}{description}"


def _get_pr_ref(pr: str) -> str:
    args = [*"gh pr view".split(), pr, *"--json headRefOid --jq .headRefOid".split()]
    subproc = subprocess.run(
        args,
        check=True,
        capture_output=True,
        text=True,
    )
    return subproc.stdout.strip()


class NoPrOpenError(Exception):
    MSG = re.compile(r"^no pull requests found for branch")

    __cause__: subprocess.CalledProcessError

    def __init__(self, called_process_err: subprocess.CalledProcessError):
        super().__init__(called_process_err.stderr)
        self.__cause__ = called_process_err

    @property
    def message(self):
        return self.__cause__.stderr


def _get_current_pr_number() -> str:
    # TODO: couldn't find one for jenkins pr? are drafts not counted somehow?
    # even let me open one in the web, but it wouldn't compare properly.
    # maybe that's because I skipped pushing or something
    # TODO: can you have multiple PRs per branch?
    try:
        return subprocess.run(
            "gh pr view --json number --jq '.number'".split(),
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except subprocess.CalledProcessError as e:
        if NoPrOpenError.MSG.match(e.stderr) is not None:
            raise NoPrOpenError(e)
        else:
            raise


def get_non_succeeding_checks(pr: str) -> Iterable[PRStatusResult]:
    JQ_FAILING_TESTS_FILTER = '[.statuses[] | {name: .context, state, description} | select(.state != "success")]'

    ref = _get_pr_ref(pr)
    args = [
        *"gh api".split(),
        f"https://api.github.com/repos/konveyor/pelorus/commits/{ref}/status",
        "--jq",
        JQ_FAILING_TESTS_FILTER,
    ]
    subproc = subprocess.run(
        args,
        capture_output=True,
        text=True,
    )

    if subproc.returncode != 0:
        sys.stderr.write(f"gh api call returned {subproc.returncode}:\n")
        sys.stderr.write(subproc.stderr)
        sys.stdout.write(subproc.stdout)
        subproc.check_returncode()

    json_output = json.loads(subproc.stdout)
    if not isinstance(json_output, list):
        sys.exit(f"json output was not a list: {json_output}")

    for obj in json_output:
        yield PRStatusResult(**obj)


@click.group
def pr_logs():
    pass


@pr_logs.command
@click.argument("pr_or_test")
@click.argument("test", required=False)
@click.option("--view-url", is_flag=True)
def e2e(pr_or_test: str, test: Optional[str], view_url: bool):
    # TODO: doc
    if test is None:
        try:
            pr, test = _get_current_pr_number(), pr_or_test
        except NoPrOpenError as e:
            sys.exit(e.message)
    else:
        pr, test = pr_or_test, test

    blob = get_e2e_log_blob(pr, test)

    if view_url:
        print(blob.public_url)
    else:
        print(blob.download_as_text())


@pr_logs.command
@click.argument("pr", required=False)
def check(pr: Optional[str]):
    try:
        pr = pr if pr is not None else _get_current_pr_number()
    except NoPrOpenError as e:
        sys.exit(e.message)

    for check in get_non_succeeding_checks(pr):
        print(check)


if __name__ == "__main__":
    pr_logs()
