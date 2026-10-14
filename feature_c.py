"""Модуль feature_c: строковые утилиты и генератор приветствий.

Добавлен в ветви development в рамках тренировки Pull Request
и автоматического слияния (auto-merge) после прохождения CI.
"""

from __future__ import annotations


class Greeter:
    """Генерирует персонализированные приветствия.

    Attributes:
        language: код языка приветствия ("ru" или "en").
    """

    _GREETINGS = {"ru": "Привет", "en": "Hello"}

    def __init__(self, language: str = "ru") -> None:
        """Создаёт генератор приветствий.

        Args:
            language: код языка, "ru" или "en" (по умолчанию "ru").

        Raises:
            ValueError: если язык не поддерживается.
        """
        if language not in self._GREETINGS:
            raise ValueError(f"Неподдерживаемый язык: {language}")
        self.language = language

    @property
    def greeting_word(self) -> str:
        """str: слово приветствия на выбранном языке."""
        return self._GREETINGS[self.language]

    def greet(self, name: str) -> str:
        """Формирует приветственную фразу для указанного имени.

        Args:
            name: имя, которое нужно поприветствовать.

        Returns:
            str: готовая фраза приветствия.

        Example:
            >>> Greeter("en").greet("Petr")
            'Hello, Petr!'
        """
        return f"{self.greeting_word}, {name}!"


def feature_c() -> str:
    """Возвращает строку-подтверждение работы функции.

    Returns:
        str: строка "feature_c работает".

    Example:
        >>> feature_c()
        'feature_c работает'
    """
    return "feature_c работает"


def feature_c_extra() -> str:
    """Дополнительная функция, добавлена для проверки поведения
    кнопки auto-merge при повторном Pull Request.

    Returns:
        str: строка "ok".

    Example:
        >>> feature_c_extra()
        'ok'
    """
    return "ok"
