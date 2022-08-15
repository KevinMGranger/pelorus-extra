from typing import Any, TypeAlias

import yaml
from attrs import asdict, field, frozen

from .utils import YAML_STD_TAG, YamlAble, yaml_register


def _extra_env_mapping(extra_env: dict[str, str], target: dict[str, Any]):
    if extra_env:
        target["extraEnv"] = [
            dict(name=name.upper(), value=value) for name, value in extra_env.items()
        ]


@frozen
class Exporter:
    extra_env: dict[str, str] = field(factory=dict, kw_only=True)

    def _exporter_mapping(self) -> dict[str, Any]:
        mapping = asdict(self, filter=lambda attr, _: attr.name != "extra_env")
        _extra_env_mapping(self.extra_env, mapping)
        return mapping


@frozen
class DefaultExporter(Exporter):
    exporter_type: str


@frozen
class SourceExporter(Exporter):
    app_file: str
    source_context_dir: str = field(default="exporters", kw_only=True)
    source_ref: str = "master"
    source_url: str = "https://github.com/konveyor/pelorus"
    extra_env: dict[str, str] = field(factory=dict, kw_only=True)

    def _exporter_mapping(self) -> dict[str, Any]:
        mapping = asdict(
            self, filter=lambda attr, _: attr.name not in {"extra_env", "app_file"}
        )
        extra_env = self.extra_env | dict(app_file=self.app_file)
        _extra_env_mapping(extra_env, mapping)
        return mapping


@frozen
class ImageExporter(Exporter):
    image_name: str
    image_tag: str
    exporter_type: str
    extra_env: dict[str, str] = field(factory=dict, kw_only=True)


# ExporterConfig: TypeAlias = DefaultExporter | SourceExporter | ImageExporter


@yaml_register
@frozen
class OtherFields:
    openshift_prometheus_htpasswd_auth: str = (
        "internal:{SHA}+pvrmeQCmtWmYVOZ57uuITVghrM="
    )
    openshift_prometheus_basic_auth_pass: str = "changeme"
    extra_prometheus_hosts: str | None = None
    snapshot_schedule: str = "@monthly"


@frozen
class ExporterWithName(YamlAble):
    app_name: str
    config: Exporter

    def _to_yaml(self, dumper: yaml.Dumper) -> yaml.Node:
        app_name = self.app_name.replace("_", "-")
        mapping = dict(app_name=app_name) | self.config._exporter_mapping()

        return dumper.represent_mapping(f"{YAML_STD_TAG}:map", mapping, False)


@frozen
class Values(YamlAble):
    exporters: list[ExporterWithName] | dict[str, Exporter]
    other: OtherFields = field(factory=OtherFields)

    def _to_yaml(self, dumper: yaml.Dumper) -> yaml.Node:
        match self.exporters:
            case list():
                exporters = self.exporters
            case dict():
                exporters = [
                    ExporterWithName(name, config)
                    for name, config in self.exporters.items()
                ]

        value: dict[str, Any] = asdict(self.other) | dict(
            exporters=dict(instances=exporters)
        )

        return dumper.represent_mapping(f"{YAML_STD_TAG}:map", value, False)
