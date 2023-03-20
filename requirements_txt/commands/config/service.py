import click
from appdata import AppDataPaths

from requirements_txt.utils.config import (
    ALLOWED_CONFIG_KEYS,
    read_config,
    save_config,
    get_allowed_types,
)


def set_config(app_paths: AppDataPaths, key: str, value: str, global_: bool):
    if key not in ALLOWED_CONFIG_KEYS.keys():
        click.echo("Wrong config key.")
        raise click.Abort()
    key_data = ALLOWED_CONFIG_KEYS[key]

    if key_data["type"] is bool and value is None:
        value = "1"

    if key_data["type"] not in get_allowed_types(value):
        click.echo("Wrong type of value.")
        raise click.Abort()

    lock = app_paths.lock()
    with lock.context():
        config = read_config(global_)
        if "DEFAULT" not in config:
            config["DEFAULT"] = {}
        config["DEFAULT"][key] = value
        save_config(config, global_=global_)


__all__ = [
    "set_config",
]
