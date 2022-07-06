from functools import wraps
import os
from appdata import AppDataPaths


def validate_app_data_decorator(func):
    @wraps(func)
    def _func(*args, **kwargs):
        app_paths = AppDataPaths('to-requirements.txt')
        if app_paths.require_setup:
            app_paths.setup()
        return func(*args, **kwargs)
    return _func


def validate_app_data(global_=False):
    app_paths = get_app_paths(global_)
    if app_paths.require_setup:
        app_paths.setup()


def insert_app_paths(func):
    @wraps(func)
    def _func(*args, **kwargs):
        app_paths = AppDataPaths('to-requirements.txt')
        return func(*args, app_paths=app_paths, **kwargs)
    return _func


def get_app_paths(global_=False):
    if global_:
        app_paths = AppDataPaths('to-requirements.txt')
    else:
        app_paths = AppDataPaths(
            'to-requirements.txt',
            home_folder_path=os.getcwd()
        )
    return app_paths
