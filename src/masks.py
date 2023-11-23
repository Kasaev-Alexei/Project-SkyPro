from src.log import logger


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
