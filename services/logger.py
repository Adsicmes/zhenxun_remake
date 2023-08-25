from nonebot import logger
from nonebot.log import default_format, default_filter


def logger_configure():
    logger.add(
        "logs/logs_{time}.log",
        level="INFO",
        rotation="10MB",
        compression="zip",
        format=default_format,
        filter=default_filter
    )

    logger.add(
        "logs/error_{time}.log",
        level="ERROR",
        rotation="10MB",
        compression="zip",
        format=default_format,
        filter=default_filter
    )
