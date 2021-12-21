import os
import click
import configparser
from appdata import AppDataPaths

from requirements_txt.install import install

if __name__ == '__main__':
    import sys
    sys.path.append(os.getcwd())


from requirements_txt.utils import setup_logging
from requirements_txt.utils import validate_app_data, insert_app_paths
from requirements_txt.config import get_allowed_types, ALLOWED_CONFIG_KEYS, read_config, save_config


@click.group()
@validate_app_data
def cli():
    setup_logging()


@cli.command()
@click.argument('key', required=False)
@click.argument('value', required=False)
@insert_app_paths
def config(key, value, app_paths: AppDataPaths):
    """Allows to access to-requirements.txt config. Available keys:


    only_git - specify if the requirements.txt should be written only in git repositories.

    allow_create - specify if the requirements.txt should be created if not exists.
    """
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
        return
    key_data = ALLOWED_CONFIG_KEYS[key]
    if key_data['type'] not in get_allowed_types(value):
        click.echo('Wrong type of value.')
    if key_data['type'] is bool and value is None:
        value = '1'

    lock = app_paths.lock()
    with lock.context():
        config = read_config()
        if 'DEFAULT' not in config:
            config['DEFAULT'] = {}
        config['DEFAULT'][key] = value
        save_config(config)


@cli.command()
def setup():
    install()


if __name__ == '__main__':
    cli()
