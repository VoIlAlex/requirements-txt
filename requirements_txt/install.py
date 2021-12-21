import logging
import os.path
import re
import subprocess
import sys


def _get_destination_command():
    if sys.platform in ['win32', 'cygwin']:
        command = 'where'
    else:
        command = 'which'
    return command


def _get_pip_path(pip_name):
    command = _get_destination_command()
    try:
        pip_command_pipe = subprocess.Popen([command, pip_name], stdout=subprocess.PIPE)
        pip_path = str(pip_command_pipe.communicate()[0].decode()).replace('\n', '')
        if pip_path.startswith(pip_name):
            pip_path = None
        if pip_path:
            pip_version_pipe = subprocess.Popen([pip_name, '--version'], stdout=subprocess.PIPE)
            pip_version_data = str(pip_version_pipe.communicate()[0].decode()).replace('\n', '')
            python_version_pattern = re.compile('.*(python(.*?))/.*')
            python_name = python_version_pattern.search(pip_version_data).groups()[0]
            return pip_path, python_name
    except Exception:
        logging.error('pip not found.')
    return None, None


def _get_python_path(python_name):
    command = _get_destination_command()
    try:
        python_command_pipe = subprocess.Popen([command, python_name], stdout=subprocess.PIPE)
        python_path = str(python_command_pipe.communicate()[0].decode()).replace('\n', '')
        if python_path.startswith(python_name):
            python_path = None
        if python_path:
            return python_path
    except Exception:
        logging.error('python not found.')


def _override_pip(pip_path, python_path):
    new_pip_path = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        'static',
        'new_pip.py'
    )
    with open(pip_path, 'w+') as old_pip_file:
        with open(new_pip_path) as new_pip_file:
            old_pip_file.write(
                new_pip_file.read().format(python_path=python_path)
            )


def install():
    pip_paths = []
    for pip in ['pip', 'pip3']:
        pip_path, python_name = _get_pip_path(pip)
        if python_name is not None:
            python_path = _get_python_path(python_name)
            if python_path:
                pip_paths.append((pip_path, python_path))

    for pip_path, python_path in pip_paths:
        _override_pip(pip_path, python_path)
