import re


def is_pip_name(name: str) -> bool:
    """
    Is given name is the name of pip executive.

    :param name: name to check.
    :return: True if given name is pip executive.
    """
    pip_regex = re.compile("^pip\d*(\.\d+)?")  # noqa: W605
    return bool(pip_regex.search(name)) or name == "pip"


__all__ = [
    "is_pip_name",
]
