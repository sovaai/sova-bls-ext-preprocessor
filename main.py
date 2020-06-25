import logging
from external_modules.preprocessor.core import event_handler


async def main(message):
    logging.debug(f"First {message}")
    if message['type'] == 'event':
        message = await event_handler(message)
    return message