import logging
from collections import OrderedDict
from typing import Iterable, List, Dict, Union

from pip._internal.commands.show import (
    search_packages_info,
    _PackageInfo,
    logger as pip_logger,
)
from pip._vendor.pkg_resources import _initialize_master_working_set


def get_package_name(package_info: Union[dict, _PackageInfo]) -> str:
    """
    Get package name for package info.

    :param package_info: package info to get package name from.
    :return: package name.
    """
    if isinstance(package_info, dict):
        return package_info["name"]
    else:
        return package_info.name


def get_package_version(package_info: Union[dict, _PackageInfo]) -> str:
    """
    Get package version for package info.

    :param package_info: package info to get package version from.
    :return: package version.
    """
    if isinstance(package_info, dict):
        return package_info["version"]
    else:
        return package_info.version


def get_packages_info(packages_names: List[str]) -> Dict[str, str]:
    """
    Get package name and package version of installed packages by names.

    :param packages_names: list of package names to check.
    :return: mapping of package names to package versions.
    """
    _initialize_master_working_set()
    initial_pip_logger_level = pip_logger.level
    pip_logger.setLevel(level=logging.CRITICAL)
    data = {
        get_package_name(package_info): get_package_version(package_info)
        for package_info in search_packages_info(packages_names)
    }
    pip_logger.setLevel(level=initial_pip_logger_level)
    return data


def parse_packages_names(args: Iterable) -> List[str]:
    """
    Parse package names from `pip install` arguments.

    :param args: arguments.
    :return: list of package names.
    """
    packages_names = [
        x.split("==")[0].strip() for x in args if not x.startswith("-") and x != "."
    ]
    return packages_names


def parse_requirements_txt(path: str) -> OrderedDict:
    """
    Parse requirements.txt file.

    :param path: path to requirements.txt.
    :return: mapping of package names to package versions.
    """
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
