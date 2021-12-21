import configparser

from requirements_txt.utils import insert_app_paths

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


@insert_app_paths
def read_config(app_paths):
    config = configparser.ConfigParser()
    config.read(app_paths.config_path)
    return config


@insert_app_paths
def save_config(config, app_paths):
    with open(app_paths.config_path, 'w+') as f:
        config.write(f)


@insert_app_paths
def get_config_value(key, app_paths):
    if key not in ALLOWED_CONFIG_KEYS.keys():
        raise RuntimeError('Wrong key.')

    config = read_config()
    value = config['DEFAULT'].get(key, ALLOWED_CONFIG_KEYS[key].get('default', None))
    if value is not None:
        type_ = ALLOWED_CONFIG_KEYS[key].get('type', str)
        if type_ is bool:
            return True if value == '1' else False
        elif type_ is float:
            return float(value)
        else:
            return value
