import os
import re
import subprocess
from requirements_txt.utils.crossplatform import get_destination_command


def get_pip_path(pip_name=None):
    command = get_destination_command()
    pips_to_try = [pip_name] if pip_name else ['pip', 'pip3']
    for pip_to_try in pips_to_try:
        try:
            pip_command_pipe = subprocess.Popen([command, pip_to_try], stdout=subprocess.PIPE)
            pip_path = str(pip_command_pipe.communicate()[0].decode()).replace('\n', '')
            if pip_path.startswith(pip_to_try):
                pip_path = None
            if pip_path:
                pip_version_pipe = subprocess.Popen([pip_to_try, '--version'], stdout=subprocess.PIPE)
                pip_version_data = str(pip_version_pipe.communicate()[0].decode()).replace('\n', '')
                python_version_pattern = re.compile('.*(python(.*?))/.*')
                python_name = python_version_pattern.search(pip_version_data).groups()[0]
                break
        except Exception:
            continue
    else:
        return None, None
    return pip_path, python_name


def get_python_path(python_name=None):
    command = get_destination_command()
    pythons_to_try = [python_name] if python_name else ['python3', 'python']
    for python_to_try in pythons_to_try:
        try:
            python_command_pipe = subprocess.Popen([command, python_name], stdout=subprocess.PIPE)
            python_path = str(python_command_pipe.communicate()[0].decode()).replace('\n', '')
            if python_path.startswith(python_name):
                python_path = None
            if python_path:
                return python_path
        except Exception:
            ...


def find_virtualenv(path: str = None) -> str:
    path = path or os.getcwd()
    for file in os.listdir(path):
        if os.path.isdir(file):
            files_in_dir = os.listdir(file)
            if 'bin' in files_in_dir \
                and 'lib' in files_in_dir \
                and 'pyvenv.cfg' in files_in_dir:
                return os.path.join(path, file)
