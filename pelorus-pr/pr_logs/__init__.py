#!/usr/bin/env python3

# import subprocess # `gh` command if checking for statuses on pr
from google.cloud import storage  # pip: google-cloud-storage

# import click
import sys
from pathlib import PurePath

PULLS_DIR = PurePath("pr-logs/pull/konveyor_pelorus")
TEST_NAME_TEMPLATE = "pull-ci-konveyor-pelorus-master-{test}-e2e-openshift"

LATEST_BUILD_FILENAME = "latest-build.txt"

BUILD_LOG_SUBPATH = PurePath("artifacts/e2e-openshift/e2e/build-log.txt")

_, pr, test = sys.argv
# pr-logs/pull/konveyor_pelorus/729/pull-ci-konveyor-pelorus-master-4.10-e2e-openshift/1597612199445008384/artifacts/e2e-openshift/e2e/
artifact_root_dir = PULLS_DIR / pr / TEST_NAME_TEMPLATE.format(test=test)

client = storage.Client.create_anonymous_client()
bucket = client.bucket("origin-ci-test")


latest_build_id_blob = bucket.blob(str(artifact_root_dir / LATEST_BUILD_FILENAME))
latest_build_id = latest_build_id_blob.download_as_text()

build_log_path = str(artifact_root_dir / latest_build_id / BUILD_LOG_SUBPATH)
build_log = bucket.blob(build_log_path).download_as_text()
print(build_log)
