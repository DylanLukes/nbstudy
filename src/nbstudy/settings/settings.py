# SPDX-FileCopyrightText: 2024-present Dylan Lukes <lukes.dylan@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class GithubSection(BaseModel):
    token: str = "MISSING_API_TOKEN"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="NBSTUDY_",
        env_nested_delimiter="_",
        env_file="nbstudy.config.env",
        env_file_encoding="utf-8",
    )

    github: GithubSection = GithubSection()
