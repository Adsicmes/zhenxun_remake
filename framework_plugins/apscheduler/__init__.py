import logging
import os
from nonebot import get_driver, require
from nonebot.plugin import PluginMetadata
from nonebot.log import LoguruHandler, logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .config import Config

require("localstore")
from framework_plugins.localstore import get_config_file, get_config_dir


__plugin_meta__ = PluginMetadata(
    name="APScheduler",
    description="APScheduler 定时任务插件",
    usage=(
        "仅限插件内开发使用\n\n"
        '声明依赖: `require("nonebot_plugin_apscheduler")\n'
        "导入调度器: `from nonebot_plugin_apscheduler import scheduler`\n"
        "添加任务: `scheduler.add_job(...)`\n"
    ),
    type="library",
    homepage="https://github.com/nonebot/plugin-apscheduler",
    config=Config,
    supported_adapters=None,
)

plugin_config_dir = get_config_dir(__plugin_meta__.name)
plugin_config_file = get_config_file(__plugin_meta__.name, "config.json")
if not os.path.isfile(plugin_config_file):
    os.makedirs(plugin_config_dir, exist_ok=True)
    with open(plugin_config_file, "w") as f:
        f.write(Config().json(indent=4))

plugin_config = Config.parse_file(plugin_config_file)

scheduler = AsyncIOScheduler()
scheduler.configure(plugin_config.apscheduler_config)
driver = get_driver()


async def _start_scheduler():
    if not scheduler.running:
        scheduler.start()
        logger.opt(colors=True).info("<y>Scheduler Started</y>")


async def _shutdown_scheduler():
    if scheduler.running:
        scheduler.shutdown()
        logger.opt(colors=True).info("<y>Scheduler Shutdown</y>")


if plugin_config.apscheduler_autostart:
    driver.on_startup(_start_scheduler)
    driver.on_shutdown(_shutdown_scheduler)

aps_logger = logging.getLogger("apscheduler")
aps_logger.setLevel(plugin_config.apscheduler_log_level)
aps_logger.handlers.clear()
aps_logger.addHandler(LoguruHandler())
