from copy import deepcopy
from hashlib import sha256
from typing import Any, Generic, Sequence, TypeVar, Union
from pelorus.utils import split_path
from datetime import datetime, timezone
from committime.app import DEFAULT_COMMIT_DATE_FORMAT
from uuid import uuid4

from dataclasses import MISSING
import json
import sys

spec = {
    "apiVersion": "image.openshift.io/v1",
    "dockerImageLayers": [
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:8dfe9326f733b815c486432e93e0a97f03e90e7cc35def9511cd1efa7f917f56",
            "size": 81522888,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:0d875a68bf996a2e45cd381e8eb3c8b1efa6191d8e3f6ec98be685c7e9823815",
            "size": 1803,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:950c796b5dbc22ecb4f4bd661013c9286715d238a0dbdd9b7ed1406c395086a1",
            "size": 17214436,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:5f29c45159acfbdb8d8400647590911ce9293454489844644266db3d957ddfbb",
            "size": 143050690,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:a6c51f156ad5d3bdd55c68736a1e066f7464c95ea3d1ee3a9984f3d1af53f067",
            "size": 75125109,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:6e4cbbd49293789e8c91c6745aba63e473b71d9aa30b90b6789ef7c83d43b878",
            "size": 867,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:af1d01dc11eba4dbf74e41ba4c47091bff3138cfeb2b6d10d313c5f86ba9f296",
            "size": 916,
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "name": "sha256:6a495049eb0910e808346de1cd0bc93b9e69434a8de81e948ff909fcf70d65e1",
            "size": 1049,
        },
    ],
    "dockerImageManifestMediaType": "application/vnd.oci.image.manifest.v1+json",
    "dockerImageMetadata": {
        "Architecture": "amd64",
        "Config": {
            "Cmd": ["/bin/sh", "-c", "/usr/libexec/s2i/run"],
            "Entrypoint": ["container-entrypoint"],
            "Env": [
                "PATH=/opt/app-root/src/.local/bin/:/opt/app-root/src/bin:/opt/app-root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "container=oci",
                "SUMMARY=Platform for building and running Python 3.8 applications",
                "DESCRIPTION=Python 3.8 available as container is a base platform for building and running various Python 3.8 applications and frameworks. Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
                "STI_SCRIPTS_URL=image:///usr/libexec/s2i",
                "STI_SCRIPTS_PATH=/usr/libexec/s2i",
                "APP_ROOT=/opt/app-root",
                "HOME=/opt/app-root/src",
                "PLATFORM=el8",
                "NODEJS_VER=14",
                "PYTHON_VERSION=3.8",
                "PYTHONUNBUFFERED=1",
                "PYTHONIOENCODING=UTF-8",
                "LC_ALL=en_US.UTF-8",
                "LANG=en_US.UTF-8",
                "CNB_STACK_ID=com.redhat.stacks.ubi8-python-38",
                "CNB_USER_ID=1001",
                "CNB_GROUP_ID=0",
                "PIP_NO_CACHE_DIR=off",
                "BASH_ENV=/opt/app-root/etc/scl_enable",
                "ENV=/opt/app-root/etc/scl_enable",
                "PROMPT_COMMAND=. /opt/app-root/etc/scl_enable",
            ],
            "ExposedPorts": {"8080/tcp": {}},
            "Labels": {
                "architecture": "x86_64",
                "build-date": "2022-02-25T22:15:10.175Z",
                "com.redhat.build-host": "cpt-1002.osbs.prod.upshift.rdu2.redhat.com",
                "com.redhat.component": "python-38-container",
                "com.redhat.license_terms": "https://www.redhat.com/en/about/red-hat-end-user-license-agreements#UBI",
                "description": "Python 3.8 available as container is a base platform for building and running various Python 3.8 applications and frameworks. Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
                "distribution-scope": "public",
                "io.buildah.version": "1.21.4",
                "io.buildpacks.stack.id": "com.redhat.stacks.ubi8-python-38",
                "io.k8s.description": "Python 3.8 available as container is a base platform for building and running various Python 3.8 applications and frameworks. Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
                "io.k8s.display-name": "Python 3.8",
                "io.openshift.expose-services": "8080:http",
                "io.openshift.s2i.build.image": "image-registry.openshift-image-registry.svc:5000/openshift/python:3.8-ubi8",
                "io.openshift.s2i.build.source-location": "demo/python-example",
                "io.openshift.s2i.scripts-url": "image:///usr/libexec/s2i",
                "io.openshift.tags": "builder,python,python38,python-38,rh-python38",
                "io.s2i.scripts-url": "image:///usr/libexec/s2i",
                "maintainer": "SoftwareCollections.org <sclorg@redhat.com>",
                "name": "ubi8/python-38",
                "release": "80.1645821300",
                "summary": "Platform for building and running Python 3.8 applications",
                "url": "https://access.redhat.com/containers/#/registry.access.redhat.com/ubi8/python-38/images/1-80.1645821300",
                "usage": "s2i build https://github.com/sclorg/s2i-python-container.git --context-dir=3.8/test/setup-test-app/ ubi8/python-38 python-sample-app",
                "vcs-ref": "a42d712a71400035853b25d40f54b5bc3ebf84ec",
                "vcs-type": "git",
                "vendor": "Red Hat, Inc.",
                "version": "1",
            },
            "User": "1001",
            "WorkingDir": "/opt/app-root/src",
        },
        "ContainerConfig": {},
        "Created": "2022-08-23T15:46:59Z",
        "Id": "sha256:bc89df5befb9651496516ab927f0cf7b6688f0634f8037197c849266af9733fc",
        "Size": 316923595,
        "apiVersion": "image.openshift.io/1.0",
        "kind": "DockerImage",
    },
    "dockerImageMetadataVersion": "1.0",
    "dockerImageReference": "image-registry.openshift-image-registry.svc:5000/basic-python-tekton/basic-python-tekton@sha256:210578ab5cf3d0286f9c0140d2d81b47d7ff02dd1d2860b6701dc36c1b3e08e4",
    "kind": "Image",
    "metadata": {
        "annotations": {
            "image.openshift.io/dockerLayersOrder": "ascending",
            "image.openshift.io/manifestBlobStored": "true",
            "io.openshift.build.commit.id": "16ef25d531ce169f5ae36990ef7b050920d2a395",
            "io.openshift.build.source-location": "https://github.com/kevinmgranger/pelorus",
            "openshift.io/image.managed": "true",
        },
        "creationTimestamp": "2022-08-23T15:47:04Z",
        "labels": {"app.kubernetes.io/name": "basic-python-tekton"},
        "name": "sha256:210578ab5cf3d0286f9c0140d2d81b47d7ff02dd1d2860b6701dc36c1b3e08e4",
        "resourceVersion": "25493722",
        "uid": "78cdae6e-fed5-4070-9cec-70bf9a7ea569",
    },
}

T = TypeVar("T")


class DictRef(Generic[T]):
    def __init__(self, path: Union[str, Sequence[str]]):
        self.path = split_path(path)

    @property
    def pre(self):
        return self.path[:-1]

    @property
    def last(self):
        return self.path[-1]

    def __get__(self, obj, objtype=None):
        if obj is None and objtype is not None:
            raise TypeError("only usable with instance")

        obj = obj.spec
        for part in self.pre:
            obj = obj[part]

        return obj.get(self.last, MISSING)

    def __set__(self, obj, value):
        obj = obj.spec
        for part in self.pre:
            obj = obj[part]

        if value is MISSING:
            del obj[self.last]
        else:
            obj[self.last] = value

    def __delete__(self, obj):
        obj = obj.spec
        for part in self.pre:
            obj = obj[part]

        if self.last in obj:
            del obj[self.last]


def dictref(*path: str) -> Any:
    if len(path) == 1:
        return DictRef(path[0])
    else:
        return DictRef(path)


class Spec:
    _LABELS = ("dockerImageMetadata", "Config", "Labels")

    app_name = dictref("metadata", "labels", "app.kubernetes.io/name")
    name = dictref("metadata.name")  # required
    ref = dictref("dockerImageReference")  # required (but where is it used?)
    dockerlabels = dictref(*_LABELS)

    namespace = dictref(*_LABELS, "io.openshift.build.namespace")

    commit_time_from_label = dictref(
        *_LABELS, "io.openshift.build.commit.date"
    )  # required here or in annotation
    commit_hash_from_label = dictref(*_LABELS, "io.openshift.build.commit.id")

    repo_url = dictref(*_LABELS, "io.openshift.build.source-location")
    committer = dictref(*_LABELS, "io.openshift.build.commit.author")

    commit_time_from_annotation = dictref(
        "metadata", "annotations", "io.openshift.build.commit.date"
    )  # required here or in annotation
    commit_hash_from_annotation = dictref(
        "metadata", "annotations", "io.openshift.build.commit.id"
    )

    def __init__(self, spec: dict):
        self.spec = deepcopy(spec)


def hash_name(name: str) -> str:
    hash = sha256(name.encode()).digest().hex()
    return f"sha256:{hash}"


def image_ref(hashed_name: str) -> str:
    return f"image-registry.openshift-image-registry.svc:5000/basic-python-tekton/basic-python-tekton@{hashed_name}"


def named(name: str) -> Spec:
    _spec = Spec(spec)
    hname = hash_name(name)
    _spec.name = hname
    _spec.ref = image_ref(hname)
    _spec.app_name = name
    _spec.spec["metadata"]["uid"] = str(uuid4())
    return _spec


missing_name = named("missing_name")
del missing_name.name

missing_ref = named("missing_ref")
del missing_ref.ref

missing_time = named("missing_time")
del missing_time.commit_time_from_label
del missing_time.commit_time_from_annotation


proper_label = named("label")
proper_label.commit_time_from_label = datetime.now(timezone.utc).strftime(
    DEFAULT_COMMIT_DATE_FORMAT
)

proper_anno = named("anno")
proper_anno.commit_time_from_annotation = datetime.now(timezone.utc).strftime(
    DEFAULT_COMMIT_DATE_FORMAT
)

images = dict(
    kind="List",
    apiVersion="v1",
    items=[
        image.spec
        for image in (
            missing_name,
            missing_ref,
            missing_time,
            proper_label,
            proper_anno,
        )
    ],
)

json.dump(images, sys.stdout, indent=2)
