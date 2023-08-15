import argparse

import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter  # 避免重复命名
from nonebot.adapters.onebot.v12 import Adapter as OnebotV12Adapter
from services.logger import logger_configure


def init(console_test=False, onebot=True):
    nonebot.init()

    logger_configure()

    driver = nonebot.get_driver()

    if console_test:
        driver.register_adapter(ConsoleAdapter)

    if onebot:
        driver.register_adapter(OnebotV12Adapter)

    nonebot.load_plugins("basic_plugins")
    nonebot.load_plugins("plugins")


def main(args: argparse.Namespace):
    init(args.enable_console, args.enable_onebot)
    nonebot.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--enable_console', type=bool, default=False, help='whether to use console to test.')
    parser.add_argument('--enable_onebot', type=bool, default=True, help='whether to enable onebot adapter')

    main(parser.parse_args())
