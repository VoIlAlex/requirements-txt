import configparser
import os
from requirements_txt.utils.appdata import get_app_paths


ALLOWED_CONFIG_KEYS = {
    'only_git': {
        'type': bool,
        'default': False
    },
    'allow_create': {
        'type': bool,
        'default': False
    },
    'disable': {
        'type': bool,
        'default': False
    }
}


def get_allowed_types(value: str):
    types = []
    if value is None:
        return [type(None), bool]
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


def read_config(global_=False):
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


def save_config(config, global_=False):
    app_paths = get_app_paths(global_)
    with open(app_paths.config_path, 'w+') as f:
        config.write(f)


def get_config_value(key, global_=None):
    if key not in ALLOWED_CONFIG_KEYS.keys():
        raise RuntimeError('Wrong key.')

    config = read_config(global_=global_)
    value = config['DEFAULT'].get(key, ALLOWED_CONFIG_KEYS[key].get('default', None))
    if value is not None:
        type_ = ALLOWED_CONFIG_KEYS[key].get('type', str)
        if type_ is bool:
            return True if value == '1' else False
        elif type_ is float:
            return float(value)
        else:
            return value
