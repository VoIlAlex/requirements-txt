import configparser
import os
from typing import Any, Optional, List

from requirements_txt.utils.appdata import get_app_paths


ALLOWED_CONFIG_KEYS = {
    "only_git": {"type": bool, "default": False},
    "allow_create": {"type": bool, "default": False},
    "disable": {"type": bool, "default": False},
}


def get_allowed_types(value: str) -> List[type]:
    """
    Get allowed types for presented string value.

    :param value: value to check.
    :return: list of types that the value could be converted to.
    """
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
    if value in ["0", "1"]:
        types.append(bool)
    return types


def get_config_value(key: str, global_: bool = None) -> Any:
    """
    Get value from config.

    :param key: config key to get.
    :param global_: whether to search in global config. Search in both global and local if None.
    """
    if key not in ALLOWED_CONFIG_KEYS.keys():
        raise RuntimeError("Wrong key.")

    config = read_config(global_=global_)
    value = config["DEFAULT"].get(key, ALLOWED_CONFIG_KEYS[key].get("default", None))
    if value is not None:
        type_ = ALLOWED_CONFIG_KEYS[key].get("type", str)
        if type_ is bool:
            return True if value == "1" else False
        elif type_ is float:
            return float(value)
        else:
            return value


def read_config(global_: Optional[bool] = False) -> configparser.ConfigParser:
    """
    Read config.

    :param global_: whether to read global config. Read both global and local if None.
    """
    app_paths_list = []
    if isinstance(global_, bool):
        app_paths = get_app_paths(global_)
        app_paths_list.append(app_paths)
    else:
        app_paths = get_app_paths(True)
        if os.path.exists(app_paths.config_path):
            app_paths_list.append(app_paths)
        app_paths_list.append(get_app_paths(False))

    config = configparser.ConfigParser()
    config.read([x.config_path for x in app_paths_list])
    return config


def save_config(config: configparser.ConfigParser, global_: Optional[bool] = False):
    """
    Save config.

    :param config: config to save.
    :param global_: whether to save config as global or local.
    """
    app_paths = get_app_paths(global_)
    with open(app_paths.config_path, "w+") as f:
        config.write(f)


__all__ = [
    "ALLOWED_CONFIG_KEYS",
    "get_app_paths",
    "get_config_value",
    "read_config",
    "save_config",
]
