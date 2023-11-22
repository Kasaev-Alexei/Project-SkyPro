import logging

logger = logging.getLogger('__masks__')
file_handler_masks = logging.FileHandler('masks_loger.log', 'w', encoding='utf-8')
file_formatter_masks = logging.Formatter('%(asctime)s %(module)s %(levelname)s %(message)s')
file_handler_masks.setFormatter(file_formatter_masks)
logger.addHandler(file_handler_masks)
logger.setLevel(logging.INFO)


def mask_user_card(user_card: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :param user_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(user_card) == 16:
        logger.info('Номер карты введен верно')
        return f"{user_card[0:4]} {user_card[4:6]}** **** {user_card[-4:]}"
    else:
        logger.error('Введен короткий или длинный номер карты')
        return "Введен короткий или длинный номер карты"


def mask_user_account(user_account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    :param user_account: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(user_account) == 20:
        logger.info('Номер счета введен верно')
        return f"**{user_account[-4:]}"
    else:
        logger.error('Введен короткий или длинный номер счета')
        return "Введен короткий или длинный номер счета"


mask_user_card("123456789012345")
mask_user_account("12345678901234567890")
