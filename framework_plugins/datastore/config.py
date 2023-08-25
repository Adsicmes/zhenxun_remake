""" 配置 """
import os
from pathlib import Path
from typing import Any, Dict

import ujson
from nonebot import get_driver, require
from pydantic import BaseModel, Extra, root_validator

require("localstore")
from framework_plugins.localstore import get_cache_dir, get_config_dir, get_data_dir, get_config_file


class Config(BaseModel, extra=Extra.ignore):
    datastore_cache_dir: Path = Path(get_cache_dir("Datastore"))
    datastore_config_dir: Path = Path(get_config_dir("Datastore"))
    datastore_data_dir: Path = Path(get_data_dir("Datastore"))
    datastore_database_url: str = f"sqlite+aiosqlite:///{Path(get_data_dir('Datastore')) / 'data.db'}"
    """数据库连接字符串

    默认使用 SQLite
    """
    datastore_enable_database: bool = True
    datastore_database_echo: bool = False
    datastore_engine_options: Dict[str, Any] = {}
    datastore_config_provider: str = "~json"

    # @root_validator(pre=True, allow_reuse=True)
    # def set_defaults(cls, values: Dict):
    #     """设置默认值"""
    #     # 设置默认目录
    #     # 仅在未设置时调用 get_*_dir 函数，因为这些函数会自动创建目录
    #     values["datastore_cache_dir"] = (
    #         Path(cache_dir)
    #         if (cache_dir := values.get("datastore_cache_dir"))
    #         else Path(get_cache_dir(""))
    #     )
    #     values["datastore_config_dir"] = (
    #         Path(config_dir)
    #         if (config_dir := values.get("datastore_config_dir"))
    #         else Path(get_config_dir(""))
    #     )
    #     values["datastore_data_dir"] = (
    #         Path(data_dir)
    #         if (data_dir := values.get("datastore_data_dir"))
    #         else Path(get_data_dir(""))
    #     )
    #
    #     # 设置默认数据库连接字符串
    #     if not values.get("datastore_database_url"):
    #         values[
    #             "datastore_database_url"
    #         ] = f"sqlite+aiosqlite:///{values['datastore_data_dir'] / 'data.db'}"
    #
    #     return values


plugin_config_dir = get_config_dir("Datastore")
plugin_config_file = get_config_file("Datastore", "config.json")
if not os.path.isfile(plugin_config_file):
    os.makedirs(plugin_config_dir, exist_ok=True)
    with open(plugin_config_file, "w") as f:
        f.write(Config().json(indent=4))

plugin_config = Config.parse_file(plugin_config_file)
