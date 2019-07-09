import click
import sys


@click.group()
def main():
    pass


@main.command()
@click.option("--host")
def serve(host):
    from . import server

    server.api.run(address=host)
    sys.exit(0)


@main.command("init-db")
def init_db():
    from .models import create_tables

    create_tables()
