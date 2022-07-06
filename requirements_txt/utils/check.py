import re


def is_pip_name(name: str) -> bool:
    pip_regex = re.compile('pip\d')
    return pip_regex.search(name) or name == 'pip'
