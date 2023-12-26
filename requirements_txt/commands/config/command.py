import configparser

import click

from requirements_txt.commands.cli import cli
from requirements_txt.commands.config.service import set_config
from requirements_txt.utils.appdata import get_app_paths, validate_app_data


# Config
@cli.command()
@click.option(
    "-g", "--global", "global_", is_flag=True, help="Write to global configuration."
)
@click.argument("key", required=False)
@click.argument("value", required=False)
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
            print(f"[{section}]")
            for key, value in config[section].items():
                print(f"{key}={value}")
            print("\n")
        return

    set_config(app_paths, key, value, global_)


__all__ = [
    "config",
]
