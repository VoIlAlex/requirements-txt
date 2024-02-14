import sys
import tempfile
import os
import subprocess
from contextlib import contextmanager

CURRENT_DIR = os.getcwd()


@contextmanager
def virtual_environment():
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chdir(tmpdir)
            subprocess.run([sys.executable, '-m', 'virtualenv', 'venv'])
            subprocess.run(['./venv/bin/pip', 'install', CURRENT_DIR])
            subprocess.run(['./venv/bin/rt', 'i'])
            yield tmpdir
    finally:
        os.chdir(CURRENT_DIR)


def init_rt():
    subprocess.run(['./venv/bin/pip', 'install', CURRENT_DIR])
    subprocess.run(['./venv/bin/rt', 'i'])


def install_package(package_name: str):
    subprocess.run(['./venv/bin/pip', 'install', package_name])


def uninstall_package(package_name: str):
    subprocess.run(['./venv/bin/pip', 'uninstall', '-y', package_name])


def is_importable(module_name: str):
    try:
        subprocess.check_output(['./venv/bin/python', '-c', f'import {module_name}'])
    except Exception as e:
        return False
    return True


class TestPIP:
    def test_package_installation(self):
        with virtual_environment() as path:
            init_rt()
            install_package('appdata==2.2.1')
            requirements_txt_path = os.path.join(path, 'requirements.txt')
            with open(requirements_txt_path, 'r') as requirements_file:
                requirements = [x.strip() for x in requirements_file.readlines()]

            assert len(requirements) == 1
            assert requirements[0] == 'appdata==2.2.1'
            assert is_importable('appdata')

    def test_local_package_installation(self):
        with virtual_environment() as path:
            init_rt()
            path_to_local_package = os.path.join(
                os.path.dirname(__file__),
                'test_package',
            )
            install_package(path_to_local_package)
            requirements_txt_path = os.path.join(path, 'requirements.txt')
            with open(requirements_txt_path, 'r') as requirements_file:
                requirements = [x.strip() for x in requirements_file.readlines()]

            assert len(requirements) == 1
            assert requirements[0] == path_to_local_package
            assert is_importable('test_package')

    def test_git_package_installation(self):
        with virtual_environment() as path:
            init_rt()
            package_name = "git+https://github.com/VoIlAlex/appdata.git"
            install_package(package_name)
            requirements_txt_path = os.path.join(path, 'requirements.txt')
            with open(requirements_txt_path, 'r') as requirements_file:
                requirements = [x.strip() for x in requirements_file.readlines()]

            assert len(requirements) == 1
            assert requirements[0] == package_name
            assert is_importable('appdata')

    def test_package_uninstallation(self):
        with virtual_environment() as path:
            init_rt()
            install_package('appdata==2.2.1')
            requirements_txt_path = os.path.join(path, 'requirements.txt')
            with open(requirements_txt_path, 'r') as requirements_file:
                requirements = [x.strip() for x in requirements_file.readlines()]

            assert len(requirements) == 1
            assert requirements[0] == 'appdata==2.2.1'
            assert is_importable('appdata')

            uninstall_package('appdata')
            with open(requirements_txt_path, 'r') as requirements_file:
                requirements = [x.strip() for x in requirements_file.readlines()]

            assert len(requirements) == 0
            assert not is_importable('appdata')
