import re


def is_pip_name(name: str) -> bool:
    pip_regex = re.compile("^pip\d*(\.\d+)?")  # noqa: W605
    return bool(pip_regex.search(name)) or name == 'pip'


__all__ = [
    "is_pip_name",
]
