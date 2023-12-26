import click

from requirements_txt.utils.appdata import validate_app_data_decorator


@click.group()
@validate_app_data_decorator
def cli():
    ...


__all__ = [
    "cli",
]
