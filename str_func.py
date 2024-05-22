def to_uppercase(s: str) -> str:
    """
    Принимает строку и возвращает её со всеми заглавными буквами.

    :param s: Исходная строка.
    :return: Строка с заглавными буквами.
    """
    return s.upper()


def capitalize_words(s: str) -> str:
    """
    Принимает строку и делает заглавными первые буквы каждого слова.

    :param s: Исходная строка.
    :return: Строка с заглавными первыми буквами каждого слова.
    """
    return s.title()