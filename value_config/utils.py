from abc import ABC
from typing import TypeVar

import attrs
import yaml
from attrs import asdict

YAML_STD_TAG = "tag:yaml.org,2002"


class YamlAble(ABC):
    def __init_subclass__(cls) -> None:
        yaml.add_representer(cls, _to_yaml_representer)

    def _to_yaml(self, dumper: yaml.Dumper) -> yaml.Node:
        ...


T = TypeVar("T")
Y = TypeVar("Y", bound=YamlAble)


def asdict_representer(dumper: yaml.Dumper, data):
    """
    Uses the attrs asdict representation for yaml
    """
    return dumper.represent_mapping(f"{YAML_STD_TAG}:map", asdict(data), False)


def _to_yaml_representer(dumper: yaml.Dumper, data: YamlAble) -> yaml.Node:
    return data._to_yaml(dumper)


def to_yaml_register(cls: type[Y]) -> type[Y]:
    """
    Registers a class that has __to_yaml
    """
    yaml.add_representer(cls, _to_yaml_representer)

    return cls


def yaml_register(cls: type[T]) -> type[T]:
    if isinstance(cls, YamlAble):
        yaml_register(cls)
    elif attrs.has(cls):
        yaml.add_representer(cls, asdict_representer)
    else:
        raise TypeError(
            f"Class {cls.__name__} is not attrs and does not have __to_yaml"
        )

    return cls
