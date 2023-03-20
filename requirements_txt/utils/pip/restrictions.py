import os
from typing import Tuple, Optional


from requirements_txt.utils.config import get_config_value


def check_git_only_restriction() -> bool:
    """
    Check whether git_only configuration condition is met.

    :return: True if everything is okay.
    """
    git_only = get_config_value("only_git")
    if git_only:
        git_path = os.path.join(os.getcwd(), ".git")
        if not os.path.exists(git_path):
            return False
    return True


def get_requirements_txt_path(try_create: bool = False) -> Tuple[Optional[str], bool]:
    """
    Get requirements.txt path. Create one if not exists, try_create is specified
    configuration doesn't restrict it.

    :param try_create: whether to try to create requirements.txt if not exists.
    :return: path to requirements_txt, and whether it's newly created.
    """
    requirements_txt_path = os.path.join(os.getcwd(), "requirements.txt")
    created = False
    if not os.path.exists(requirements_txt_path):
        if try_create:
            allow_create = get_config_value("allow_create")
            if allow_create:
                with open(requirements_txt_path, "w+"):
                    created = True
            else:
                created = False
                requirements_txt_path = None
        else:
            created = False
            requirements_txt_path = None
    return requirements_txt_path, created


__all__ = [
    "check_git_only_restriction",
    "get_requirements_txt_path",
]
