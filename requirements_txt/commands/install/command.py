from requirements_txt.commands.cli import cli
from requirements_txt.commands.install.service import (
    install as install_to_requirements_txt,
)


@cli.command()
def install():
    """Install to-requirements.txt to the module."""
    install_to_requirements_txt()


__all__ = [
    "install",
]
