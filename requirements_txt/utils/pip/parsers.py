from collections import OrderedDict
from typing import Iterable, List, Dict

from pip._internal.commands.show import search_packages_info
from pip._vendor.pkg_resources import _initialize_master_working_set


def get_package_name(package_info):
    if isinstance(package_info, dict):
        return package_info["name"]
    else:
        return package_info.name


def get_package_version(package_info):
    if isinstance(package_info, dict):
        return package_info["version"]
    else:
        return package_info.version


def get_packages_info(packages_names: List[str]) -> Dict[str, str]:
    _initialize_master_working_set()
    return {
        get_package_name(package_info): get_package_version(package_info)
        for package_info in search_packages_info(packages_names)
    }


def parse_packages_names(args: Iterable):
    packages_names = [
        x.split("==")[0] for x in args if not x.startswith("-") and x != "."
    ]
    return packages_names


def parse_requirements_txt(path: str):
    requirements_dict = OrderedDict()
    with open(path, "r") as f:
        requirements = f.readlines()
        for requirement in requirements:
            requirement = requirement.replace("\n", "").strip()
            if requirement.startswith("#") or requirement == "":
                continue
            requirement_split = requirement.split("==")
            if len(requirement_split) == 1:
                requirements_dict[requirement_split[0]] = None
            else:
                requirement_split[1].replace("\n", "")
                requirements_dict[requirement_split[0]] = requirement_split[1]
    return requirements_dict


__all__ = [
    "get_packages_info",
    "parse_packages_names",
    "parse_requirements_txt",
]
