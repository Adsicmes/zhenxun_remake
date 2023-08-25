import argparse

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
from services.logger import logger_configure


def init(onebot=True):
    nonebot.init()

    logger_configure()
    driver = nonebot.get_driver()

    if onebot:
        driver.register_adapter(OnebotV11Adapter)

    nonebot.load_plugins("framework_plugins")
    nonebot.load_plugins("plugins")


def main(args: argparse.Namespace):
    init(args.enable_onebot)
    nonebot.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--enable_onebot', type=bool, default=True, help='whether to enable onebot adapter')

    main(parser.parse_args())
