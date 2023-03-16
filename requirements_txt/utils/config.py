from typing import Any

from requirements_txt.commands.config.service import read_config

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


def get_config_value(key: str, global_: bool = None) -> Any:
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
