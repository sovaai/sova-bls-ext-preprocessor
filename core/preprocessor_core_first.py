import logging


async def check_if_new(message):
    """

    :param message:
    :return:
    """
    if message['technical_info'].get('technical_context'):
        message['technical_info']['not_send_engine'] = True
        logging.debug(f"Set flag disable engine  {message}")
    else:
        logging.debug(f"Обрабатываем как обычный запрос {message}")
    return message


async def event_handler(message):
    """

    :param message: dict обрабатываемое сообщение
    :return: dict
    """
    if message['euid'] == '00b2fcbe-f27f-437b-a0d5-91072d840ed3':
        await check_if_new(message)

    if message['context'].get('count'):
        message['euid'] = f"EVENT {message['euid']} COUNT {message['context']['count']}"
    else:
        message['euid'] = f"EVENT {message['euid']}"
    return message


async def preprocessor(message):
    logging.debug(f"First")
    if message['type'] == 'event':
        message = await event_handler(message)
    return message
