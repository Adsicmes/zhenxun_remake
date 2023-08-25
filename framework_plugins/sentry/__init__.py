import os
import sentry_sdk
from nonebot import get_driver, require
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
from sentry_sdk.integrations.logging import EventHandler, BreadcrumbHandler

from .config import Config

require("localstore")
from framework_plugins.localstore import get_config_file, get_config_dir

__plugin_meta__ = PluginMetadata(
    name="SentryLogWarning",
    description="使用Sentry监控机器人日志并处理报错",
    usage="在配置文件中填写Sentry DSN即可启用",
    type="application",
    homepage="https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_sentry",
    config=Config,
    supported_adapters=None,
)

driver = get_driver()

if not os.path.isfile(get_config_file("SentryLogWarning", "config.json")):
    os.makedirs(get_config_dir("SentryLogWarning"), exist_ok=True)
    with open(get_config_file("SentryLogWarning", "config.json"), "w") as f:
        f.write(Config().json(indent=4))
config = Config.parse_file(get_config_file("SentryLogWarning", "config.json"))


def init_sentry(config: Config):
    sentry_config = {
        key[7:]: value
        for key, value in config.dict(exclude={"sentry_environment"}).items()
    }
    sentry_sdk.init(
        **sentry_config, environment=config.sentry_environment or driver.env
    )

    logger.add(
        EventHandler("ERROR"),
        filter=lambda r: r["level"].no >= logger.level("ERROR").no,
    )
    logger.add(
        BreadcrumbHandler("INFO"),
        filter=lambda r: r["level"].no >= logger.level("INFO").no,
    )


if config.sentry_dsn:
    init_sentry(config)