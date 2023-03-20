from requirements_txt.utils.logging import logger
from requirements_txt.utils.override import override_pip
from requirements_txt.utils.path import get_pip_path, get_python_path


def install():
    pip_paths = []
    for pip in ["pip", "pip3"]:
        pip_path, python_name = get_pip_path(pip)
        if python_name is not None:
            python_path = get_python_path(python_name)
            if python_path:
                pip_paths.append((pip_path, python_path))

    for pip_path, python_path in pip_paths:
        logger.info(f'Overriding "{pip_path}" with python "{python_path}"')
        override_pip(pip_path, python_path)


__all__ = [
    "install",
]
