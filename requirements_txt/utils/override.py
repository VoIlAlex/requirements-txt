import os.path


def override_pip(pip_path: str, python_path: str):
    """
    Override the pip script with one presented by to-requirements.txt.

    :param pip_path: path to pip script to override.
    :param python_path: path to python to set as executive for pip script.
    """
    new_pip_path = os.path.join(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)),
        ),
        "static",
        "new_pip.py",
    )
    with open(pip_path, "w+") as old_pip_file:
        with open(new_pip_path) as new_pip_file:
            old_pip_file.write(new_pip_file.read().format(python_path=python_path))


__all__ = [
    "override_pip",
]
