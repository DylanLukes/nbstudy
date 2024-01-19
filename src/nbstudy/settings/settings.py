# SPDX-FileCopyrightText: 2024-present Dylan Lukes <lukes.dylan@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_conig = SettingsConfigDict(
        env_prefix="NBSTUDY",
        env_file="nbstudy.env",
        env_file_encoding="utf-8",
    )
