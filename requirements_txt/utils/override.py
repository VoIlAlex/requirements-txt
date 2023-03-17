import os.path


def override_pip(pip_path: str, python_path: str):
    new_pip_path = os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
        ),
        'static',
        'new_pip.py'
    )
    with open(pip_path, 'w+') as old_pip_file:
        with open(new_pip_path) as new_pip_file:
            old_pip_file.write(
                new_pip_file.read().format(python_path=python_path)
            )
