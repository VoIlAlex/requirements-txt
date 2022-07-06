import logging
import os
from collections import OrderedDict

from requirements_txt.config import get_config_value
from pip._internal.commands.show import search_packages_info
from pip._vendor.pkg_resources import _initialize_master_working_set


def add_installed_packages_to_requirements_txt(args):
    packages_names = [x.split('==')[0] for x in args if not x.startswith('-') and x != '.']
    _initialize_master_working_set()
    get_package_data = lambda package_info: (package_info['name'], package_info['version']) \
        if isinstance(package_info, dict) else (package_info.name, package_info.version)
    packages = [get_package_data(x) for x in search_packages_info(packages_names)]
    git_only = get_config_value('only_git')
    if git_only:
        git_path = os.path.join(
            os.getcwd(),
            '.git'
        )
        if not os.path.exists(git_path):
            logging.error("Cannot write to requirements.txt. git_only flag is set.")
            return

    requirements_txt_path = os.path.join(
        os.getcwd(),
        'requirements.txt'
    )
    if not os.path.exists(requirements_txt_path):
        allow_create = get_config_value('allow_create')
        if allow_create:
            with open(requirements_txt_path, 'w+') as f:
                pass
        else:
            logging.error('requirements.txt not found. Specify allow_create config key if you want it to create automatically.')
            return

    with open(requirements_txt_path, 'r') as f:
        requirements = f.readlines()
        requirements_dict = OrderedDict()
        for requirement in requirements:
            requirement = requirement.replace('\n', '').strip()
            if requirement.startswith('#') or requirement == '':
                continue
            requirement_split = requirement.split('==')
            if len(requirement_split) == 1:
                requirements_dict[requirement_split[0]] = None
            else:
                requirement_split[1].replace('\n', '')
                requirements_dict[requirement_split[0]] = requirement_split[1]

    for package_name, package_version in packages:
        if package_name in requirements_dict:
            if requirements_dict[package_name] != package_version:
                requirements_dict[package_name] = package_version
        else:
            requirements_dict[package_name] = package_version

    with open(requirements_txt_path, 'w+') as f:
        f.writelines([f'{package_name}=={package_version}\n' for package_name, package_version in requirements_dict.items()])


def remove_uninstalled_packages_from_requirements_txt(args):
    packages_names = set([x.split('==')[0].strip() for x in args if not x.startswith('-')])
    _initialize_master_working_set()
    get_package_name = lambda package_info: package_info['name'] if isinstance(package_info, dict) else package_info.name
    get_package_version = lambda package_info: package_info['version'] if isinstance(package_info, dict) else package_info.version
    packages = {get_package_name(x): get_package_version(x) for x in search_packages_info(list(packages_names))}

    git_only = get_config_value('only_git')
    if git_only:
        git_path = os.path.join(
            os.getcwd(),
            '.git'
        )
        if not os.path.exists(git_path):
            logging.error("Cannot write to requirements.txt. git_only flag is set.")
            return

    requirements_txt_path = os.path.join(
        os.getcwd(),
        'requirements.txt'
    )
    if not os.path.exists(requirements_txt_path):
        logging.error('requirements.txt not found')
        return

    with open(requirements_txt_path, 'r') as f:
        requirements = f.readlines()
        requirements_dict = OrderedDict()
        for requirement in requirements:
            requirement = requirement.replace('\n', '').strip()
            if requirement.startswith('#') or requirement == '':
                continue
            requirement_split = requirement.split('==')
            if requirement_split[0] in packages_names and requirement_split[0] not in packages:
                continue
            if len(requirement_split) == 1:
                requirements_dict[requirement_split[0]] = None
            else:
                requirement_split[1].replace('\n', '')
                requirements_dict[requirement_split[0]] = requirement_split[1]

    with open(requirements_txt_path, 'w+') as f:
        f.writelines([f'{package_name}=={package_version}\n' for package_name, package_version in requirements_dict.items()])
