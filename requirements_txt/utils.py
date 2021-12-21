from functools import wraps
import os
from appdata import AppDataPaths


def validate_app_data(func):
    @wraps(func)
    def _func(*args, **kwargs):
        app_paths = AppDataPaths('to-requirements.txt')
        if app_paths.require_setup:
            app_paths.setup()
        return func(*args, **kwargs)
    return _func


def insert_app_paths(func):
    @wraps(func)
    def _func(*args, **kwargs):
        app_paths = AppDataPaths('to-requirements.txt')
        return func(*args, app_paths=app_paths, **kwargs)
    return _func


@insert_app_paths
def setup_logging(app_paths: AppDataPaths):
    pass
