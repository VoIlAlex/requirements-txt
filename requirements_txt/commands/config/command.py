import configparser

import click

from requirements_txt.commands.cli import cli
from requirements_txt.commands.config.service import (get_allowed_types,
                                                      read_config, save_config)
from requirements_txt.utils.appdata import get_app_paths, validate_app_data
from requirements_txt.utils.config import ALLOWED_CONFIG_KEYS


# Config
@cli.command()
@click.option('-g', '--global', 'global_', is_flag=True, help='Write to global configuration.')
@click.argument('key', required=False)
@click.argument('value', required=False)
def config(key: str, value: str, global_: bool):
    """Allows to access to-requirements.txt config. Available keys:


    only_git - specify if the requirements.txt should be written only in git repositories.

    allow_create - specify if the requirements.txt should be created if not exists.
    """
    validate_app_data(global_)
    app_paths = get_app_paths(global_)

    # If key/value are not specified
    # show current config
    if key is None:
        config = configparser.ConfigParser()
        config.read(app_paths.config_path)
        for section in config:
            print(f'[{section}]')
            for key, value in config[section].items():
                print(f'{key}={value}')
            print('\n')
        return

    if key not in ALLOWED_CONFIG_KEYS.keys():
        click.echo('Wrong config key.')
        raise click.Abort()
    key_data = ALLOWED_CONFIG_KEYS[key]

    if key_data['type'] is bool and value is None:
        value = '1'

    if key_data['type'] not in get_allowed_types(value):
        click.echo('Wrong type of value.')
        raise click.Abort()

    lock = app_paths.lock()
    with lock.context():
        config = read_config(global_)
        if 'DEFAULT' not in config:
            config['DEFAULT'] = {}
        config['DEFAULT'][key] = value
        save_config(config, global_=global_)


__all__ = [
    "config",
]
