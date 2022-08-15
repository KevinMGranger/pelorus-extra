import yaml
from importlib.util import spec_from_file_location, module_from_spec
import sys

from value_config import Values

spec = spec_from_file_location("values", sys.argv[1])
if spec is None:
    sys.exit("can't find that module idk")

mod = module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore

value = getattr(mod, "values", None)

match value:
    case None:
        sys.exit("No 'values' defined")
    case Values():
        print(yaml.dump(value))
    case _:
        sys.exit(f"Value of unknown type {type(value)}")
