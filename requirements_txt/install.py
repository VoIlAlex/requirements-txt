import os.path
import subprocess
import sys

from loguru import logger

from requirements_txt.utils import insert_app_paths


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
        if pip_path.startswith('pip'):
            pip_path = None
        if pip_path:
            return pip_path
    except Exception:
        logger.warning('pip not found.')


def _override_pip(pip_path):
    new_pip_path = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        'static',
        'new_pip.py'
    )
    with open(pip_path, 'w+') as old_pip_file:
        with open(new_pip_path) as new_pip_file:
            old_pip_file.writelines(
                new_pip_file.readlines()
            )


@insert_app_paths
def install(app_paths):
    pip_paths = []
    pip_paths.append(_get_pip_path('pip'))
    pip_paths.append(_get_pip_path('pip3'))
    pip_paths = [pip_path for pip_path in pip_paths if pip_path is not None]

    for pip_path in pip_paths:
        _override_pip(pip_path)
