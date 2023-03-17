import configparser
import os
from typing import List, Optional

from requirements_txt.utils.appdata import get_app_paths


def get_allowed_types(value: str) -> List[type]:
    types = []
    if value is None:
        return [type(None)]
    types.append(str)
    if value.isdigit():
        types.append(int)
        types.append(float)
    try:
        float(value)
        if float not in types:
            types.append(float)
    except Exception:
        pass
    if value in ['0', '1']:
        types.append(bool)
    return types


def read_config(global_: Optional[bool] = False) -> configparser.ConfigParser:
    app_paths_list = []
    if isinstance(global_, bool):
        app_paths = get_app_paths(global_)
        app_paths_list.append(app_paths)
    else:
        app_paths_list.append(
            get_app_paths(False)
        )
        app_paths = get_app_paths(True)
        if os.path.exists(app_paths.config_path):
            app_paths_list.append(
                app_paths
            )

    config = configparser.ConfigParser()
    config.read([x.config_path for x in app_paths_list])
    return config


def save_config(config: configparser.ConfigParser, global_: Optional[bool] = False):
    app_paths = get_app_paths(global_)
    with open(app_paths.config_path, 'w+') as f:
        config.write(f)
