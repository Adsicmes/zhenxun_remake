from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="echo",
    description="Check if the bot is dead or not",
    usage="!echo echo /echo ！echo",
    extra={
        "name": "echo",
        "help": {
            "normal": "echo",
            "group_admin": "echo",
            "bot_admin": "echo"
        }
    }
)
