import logging


async def preprocessor(message):
    logging.debug(f"Second {message}")
    return message
