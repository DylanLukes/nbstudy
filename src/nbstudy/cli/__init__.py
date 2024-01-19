# SPDX-FileCopyrightText: 2024-present Dylan Lukes <lukes.dylan@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
from pathlib import Path

import click

from nbstudy.workspace import Workspace


@click.group()
def cli():
    pass


@cli.command(
    "init",
    short_help="Initialize a new workspace in the current directory.",
)
@click.argument(
    "directory",
    default=".",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True, path_type=Path
    ),
)
def init(directory: Path):
    workspace = Workspace(directory)
    click.echo(f"Initializing {workspace}")


main = click.CommandCollection(sources=[cli])

if __name__ == "__main__":
    main()
