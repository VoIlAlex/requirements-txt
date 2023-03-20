import os
import re
import subprocess
from typing import Optional, Tuple

from requirements_txt.utils.crossplatform import get_destination_command


def _execute_command(args: list) -> str:
    pipe = subprocess.Popen(args, stdout=subprocess.PIPE)
    output = str(pipe.communicate()[0].decode()).replace('\n', '')
    return output


def get_pip_path(pip_name: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
    command = get_destination_command()
    pips_to_try = [pip_name] if pip_name else ['pip', 'pip3']
    for pip_to_try in pips_to_try:
        try:
            pip_path = _execute_command([command, pip_to_try])
            if pip_path.startswith(pip_to_try):
                pip_path = None
            if pip_path:
                pip_version_data = _execute_command([pip_to_try, '--version'])
                python_version_pattern = re.compile('.*(python(.*?))/.*')
                python_name = python_version_pattern.search(pip_version_data).groups()[0]
                break
        except Exception:
            continue
    else:
        return None, None
    return pip_path, python_name


def get_python_path(python_name: str = None) -> Optional[str]:
    command = get_destination_command()
    pythons_to_try = [python_name] if python_name else ['python3', 'python']
    for python_to_try in pythons_to_try:
        try:
            python_path = _execute_command([command, python_to_try])
            if python_path.startswith(python_to_try):
                python_path = None
            if python_path:
                return python_path
        except Exception:
            ...


def find_virtualenv(path: str = None) -> Optional[str]:
    path = path or os.getcwd()
    for file in os.listdir(path):
        if os.path.isdir(file):
            files_in_dir = os.listdir(file)
            if 'bin' in files_in_dir and 'lib' in files_in_dir and 'pyvenv.cfg' in files_in_dir:
                return os.path.join(path, file)


__all__ = [
    "get_pip_path",
    "get_python_path",
    "find_virtualenv",
]
