import os
import click
import configparser

from requirements_txt.install import install as install_to_requirements_txt, init_virtual_env
from requirements_txt.show import show_requirements_txt

if __name__ == '__main__':
    import sys
    sys.path.append(os.getcwd())


from requirements_txt.utils.appdata import get_app_paths, validate_app_data_decorator, validate_app_data
from requirements_txt.config import get_allowed_types, ALLOWED_CONFIG_KEYS, read_config, save_config


@click.group()
@validate_app_data_decorator
def cli():
    ...


# Config
@cli.command()
@click.option('-g', '--global', 'global_', is_flag=True, help='Write to global configuration.')
@click.argument('key', required=False)
@click.argument('value', required=False)
def config(key, value, global_):
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
def install():
    """Install to-requirements.txt to the module."""
    install_to_requirements_txt()


# Init
@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='Show installation process logs.')
def init(verbose):
    """Initialize virtualenv project."""
    init_virtual_env(verbose)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='Show installation process logs.')
def i(verbose):
    """Initialize virtualenv project. (alias)"""
    init_virtual_env(verbose)


# Show
@cli.command()
def show():
    """Show requirements.txt contents."""
    show_requirements_txt()


@cli.command()
def s():
    """Show requirements.txt contents. (alias)"""
    show_requirements_txt()


# Alias (real implementation in bash script
@cli.command()
def alias():
    """
    Put aliases to your .bashrc, .zshrc or others. Allows to activate virtual environment using "rt i".
    """
    ...


if __name__ == '__main__':
    cli()
