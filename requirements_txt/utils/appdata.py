import os
from functools import wraps
from typing import Callable

from appdata import AppDataPaths


def validate_app_data_decorator(func: Callable) -> Callable:
    """
    Setup to-requirements.txt data paths on function call.

    :param func: function to decorate.
    :return: decorated function.
    """

    @wraps(func)
    def _func(*args, **kwargs):
        app_paths = AppDataPaths("to-requirements.txt")
        if app_paths.require_setup:
            app_paths.setup()
        return func(*args, **kwargs)

    return _func


def validate_app_data(global_: bool = False):
    """
    Setup to-requirements.txt data paths if not done.

    :param global_: whether to setup global data paths.
    """
    app_paths = get_app_paths(global_)
    if app_paths.require_setup:
        app_paths.setup()


def insert_app_paths(func: Callable) -> Callable:
    """
    Insert app paths as an argument to function.

    :param func: function to decorate.
    :return: decorated function.
    """

    @wraps(func)
    def _func(*args, **kwargs):
        app_paths = AppDataPaths("to-requirements.txt")
        return func(*args, app_paths=app_paths, **kwargs)

    return _func


def get_app_paths(global_: bool = False) -> AppDataPaths:
    """
    Get app paths.

    :param global_: whether to get global or local paths.
    :return: app paths object.
    """
    if global_:
        app_paths = AppDataPaths("to-requirements.txt")
    else:
        app_paths = AppDataPaths("to-requirements.txt", home_folder_path=os.getcwd())
    return app_paths


__all__ = [
    "validate_app_data_decorator",
    "validate_app_data",
    "insert_app_paths",
    "get_app_paths",
]
