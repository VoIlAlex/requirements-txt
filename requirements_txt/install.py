import os.path
import subprocess
import sys

from requirements_txt.utils.check import is_pip_name
from requirements_txt.utils.logging import logger, show_all_dome_message, set_verbose
from requirements_txt.utils.path import get_pip_path, get_python_path, find_virtualenv


def override_pip(pip_path, python_path):
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


def init_virtual_env(verbose=False):
    set_verbose(verbose)
    logger.info('Installing virtualenv...')
    venv_path = find_virtualenv()
    stdout = sys.stdout if verbose else subprocess.PIPE
    stderr = sys.stderr if verbose else subprocess.PIPE
    if not venv_path:
        subprocess.call([sys.executable, '-m', 'pip', 'install', 'virtualenv'], stdout=stdout, stderr=stderr)
        subprocess.call([sys.executable, '-m', 'virtualenv', 'venv'], stdout=stdout, stderr=stderr)
        logger.info(' Done.\n')
        venv_path = './venv'
    else:
        logger.info(' Skip.\n')

    logger.info('Creating requirements.txt...')
    if os.path.exists('./requirements.txt'):
        logger.info(' Skip.\n')
    else:
        with open('./requirements.txt', 'w+') as f:
            ...
        logger.info(' Done.\n')

    logger.info('Installing dependencies...')
    subprocess.call([f'{venv_path}/bin/pip', 'install', '-r', 'requirements.txt'], stdout=stdout, stderr=stderr)
    logger.info(' Done.\n')

    logger.info('Installing to-requirements.txt to virtual environment...')
    subprocess.call([f'{venv_path}/bin/pip', 'install', 'to-requirements.txt'], stdout=stdout, stderr=stderr)
    logger.info(' Done.\n')
    logger.info('Setting up to-requirements.txt...')
    install_for_venv()
    logger.info(' Done.\n')
    show_all_dome_message()


def install():
    pip_paths = []
    for pip in ['pip', 'pip3']:
        pip_path, python_name = get_pip_path(pip)
        if python_name is not None:
            python_path = get_python_path(python_name)
            if python_path:
                pip_paths.append((pip_path, python_path))

    for pip_path, python_path in pip_paths:
        logger.info(f'Overriding "{pip_path}" with python "{python_path}"')
        override_pip(pip_path, python_path)


def install_for_venv():
    venv_dir = find_virtualenv()

    if venv_dir is None:
        logger.error("Virtualenv not found.")
        return

    bin_venv_dir = os.path.join(venv_dir, 'bin')

    pip_scripts_paths = [os.path.join(bin_venv_dir, pip_script_path) for pip_script_path in os.listdir(
        bin_venv_dir
    ) if is_pip_name(pip_script_path)]

    for pip_script_path in pip_scripts_paths:
        override_pip(
            pip_script_path,
            os.path.join(bin_venv_dir, 'python')
        )
