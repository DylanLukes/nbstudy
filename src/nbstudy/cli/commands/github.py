# SPDX-FileCopyrightText: 2024-present Dylan Lukes <lukes.dylan@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

import click
import github
from github import Auth as GithubAuth
from github import Github
from loguru import logger


@click.command(
    short_help="Checks GitHub auth for the current workspace.",
)
@click.pass_context
def auth_test(ctx: click.Context):
    """
    Checks GitHub auth for the current workspace.
    """
    logger.debug("GitHub authentication test command invoked.")

    auth = GithubAuth.Token(ctx.obj.github.token)
    gh = Github(auth=auth)

    try:
        gh.get_user("DylanLukes")
    except github.BadCredentialsException as exc:
        logger.error("GitHub authentication failed.")
        raise click.Abort from exc


@click.command(
    short_help="Scrape a given URL, adding it to the current workspace.",
)
@click.pass_context
def scrape(ctx: click.Context):
    """
    Scrape a given URL, adding it to the current workspace.
    """

    auth = GithubAuth.Token(ctx.obj.github.token)
    _gh = Github(auth=auth)


# @shared_options
@click.group(
    name="github",
    short_help="GitHub related commands.",
)
def group():
    """
    GitHub related commands.
    """
    logger.debug("GitHub group invoked.")


group.add_command(auth_test)
group.add_command(scrape)
