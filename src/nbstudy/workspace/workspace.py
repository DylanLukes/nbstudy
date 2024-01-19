# SPDX-FileCopyrightText: 2024-present Dylan Lukes <lukes.dylan@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
from pathlib import Path

from loguru import logger


class Workspace:
    def __init__(self, path: Path):
        self.path = path

        if not self._exists_config():
            self._initialize_config()
        else:
            logger.info(f"Found existing config at {self.path / 'nbstudy.toml'}")

        if not self._exists_cache():
            self._initialize_cache()
        else:
            logger.info(f"Found existing cache at {self.path / 'cache'}")

        if not self._exists_db():
            self._initialize_db()
        else:
            logger.info(f"Found existing database at {self.path / 'nbstudy.db'}")

        if not self._exists_repo():
            self._initialize_repo()
        else:
            logger.info(f"Found existing repository at {self.path}")

    def __repr__(self):
        return f"Workspace(path={self.path})"

    def __eq__(self, other):
        return self.path == other.path

    def __hash__(self):
        return hash(self.path)

    def _exists_config(self) -> bool:
        """Check if the configuration file of the workspace exists."""
        return (self.path / "nbstudy.toml").exists()

    def _initialize_config(self):
        """Initialize the configuration file of the workspace."""
        (self.path / "nbstudy.toml").touch(exist_ok=False)

    def _exists_cache(self) -> bool:
        """Check if the cache directory of the workspace exists."""

    def _initialize_cache(self):
        """Initialize the cache directory of the workspace."""

    def _exists_db(self) -> bool:
        """Check if the SQLite database of the workspace exists."""

    def _initialize_db(self):
        """Initialize the SQLite database of the workspace."""

    def _exists_repo(self) -> bool:
        """Check if the top level Git repository of the workspace exists."""

    def _initialize_repo(self):
        """Initialize the top level Git repository of the workspace."""
