import click

from requirements_txt.commands.cli import cli
from requirements_txt.commands.init.service import init_virtual_env


# Init
@cli.command()
@click.option("-v", "--verbose", is_flag=True, help="Show installation process logs.")
def init(verbose: bool):
    """Initialize virtualenv project."""
    init_virtual_env(verbose)


@cli.command()
@click.option("-v", "--verbose", is_flag=True, help="Show installation process logs.")
def i(verbose: bool):
    """Initialize virtualenv project. (alias)"""
    init_virtual_env(verbose)


__all__ = [
    "init",
    "i",
]
