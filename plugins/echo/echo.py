from nonebot.plugin import on_command

echo = on_command("echo", priority=100, block=False)


@echo.handle()
async def handle_func():
    await echo.finish("没似")
