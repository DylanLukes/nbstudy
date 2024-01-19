# SPDX-FileCopyrightText: 2024-present Dylan Lukes <lukes.dylan@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
from pathlib import Path

import click

from nbstudy.cli.commands.github import group as github_group
from nbstudy.settings import Settings
from nbstudy.workspace import Workspace


@click.group()
@click.pass_context
@click.option("-v", "--verbose", "is_verbose", is_flag=True, help="Increase the verbosity of the output")
@click.option(
    "-D",
    "--dir",
    "directory",
    default=".",
    help="The directory to use as the workspace. Defaults to the current directory.",
    type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=Path),
)
def cli(ctx: click.Context, is_verbose: bool, directory: Path):  # noqa: FBT001
    if is_verbose:
        click.echo("Verbose mode is on.")
    ctx.obj = Settings(_env_file=directory / Settings.model_config["env_file"])


@cli.command(
    "init",
    short_help="Initialize a new workspace in the current directory.",
)
@click.argument(
    "directory",
    default=".",
    type=click.Path(exists=True, file_okay=False, writable=True, resolve_path=True, path_type=Path),
)
def init(directory: Path):
    workspace = Workspace(directory)
    click.echo(f"Initializing {workspace}")


cli.add_command(github_group)

if __name__ == "__main__":
    cli()
