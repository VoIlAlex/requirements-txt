from requirements_txt.commands.cli import cli
from requirements_txt.commands.show.service import show_requirements_txt


# Show
@cli.command()
def show():
    """Show requirements.txt contents."""
    show_requirements_txt()


@cli.command()
def s():
    """Show requirements.txt contents. (alias)"""
    show_requirements_txt()


__all__ = [
    "show",
    "s",
]
