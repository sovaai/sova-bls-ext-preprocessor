import logging


async def preprocessor(message):
    logging.debug(f"Third {message}")
    return message
