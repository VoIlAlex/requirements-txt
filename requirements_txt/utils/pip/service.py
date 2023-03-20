import logging
from collections import OrderedDict
from typing import Iterable
from requirements_txt.utils.pip.parsers import parse_packages_names, get_packages_info, parse_requirements_txt
from requirements_txt.utils.pip.restrictions import check_git_only_restriction, get_requirements_txt_path


def add_installed_packages_to_requirements_txt(args: Iterable):
    packages_names = parse_packages_names(args)
    packages = get_packages_info(packages_names)

    if not check_git_only_restriction():
        logging.error("Cannot write to requirements.txt. git_only flag is set.")
        return

    requirements_txt_path, created = get_requirements_txt_path()

    if requirements_txt_path is None and not created:
        logging.error(
            'requirements.txt not found. Specify allow_create '
            'config key if you want it to create automatically.'
        )
        return

    requirements_dict = OrderedDict()

    if not created:
        requirements_dict = parse_requirements_txt(requirements_txt_path)

    for package_name, package_version in packages.items():
        requirements_dict[package_name] = package_version

    with open(requirements_txt_path, 'w+') as f:
        f.writelines([
            f'{package_name}=={package_version}\n'
            for package_name, package_version in requirements_dict.items()
        ])


def remove_uninstalled_packages_from_requirements_txt(args: Iterable):
    packages_names = parse_packages_names(args)
    packages = get_packages_info(packages_names)

    if not check_git_only_restriction():
        logging.error("Cannot write to requirements.txt. git_only flag is set.")
        return

    requirements_txt_path, _ = get_requirements_txt_path(try_create=False)

    if requirements_txt_path is None:
        logging.error('requirements.txt not found')
        return

    requirements_dict = parse_requirements_txt(requirements_txt_path)
    for package_name in list(requirements_dict.keys()):
        if package_name in packages_names and package_name not in packages:
            del requirements_dict[package_name]

    with open(requirements_txt_path, 'w+') as f:
        f.writelines([
            f'{package_name}=={package_version}\n'
            for package_name, package_version in requirements_dict.items()
        ])


__all__ = [
    "add_installed_packages_to_requirements_txt",
    "remove_uninstalled_packages_from_requirements_txt"
]
