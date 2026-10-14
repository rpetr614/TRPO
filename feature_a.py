"""Модуль feature_a: простой калькулятор.

Демонстрирует документирование класса, методов с аргументами,
типами и исключениями (Raises) для pdoc.
"""

from __future__ import annotations


class Calculator:
    """Простой калькулятор с базовыми арифметическими операциями.

    Attributes:
        precision: количество знаков после запятой при округлении результата.
    """

    def __init__(self, precision: int = 2) -> None:
        """Создаёт калькулятор с заданной точностью округления.

        Args:
            precision: количество знаков после запятой (по умолчанию 2).
        """
        self.precision = precision

    def add(self, a: float, b: float) -> float:
        """Складывает два числа.

        Args:
            a: первое слагаемое.
            b: второе слагаемое.

        Returns:
            float: сумма a и b, округлённая до self.precision знаков.

        Example:
            >>> Calculator().add(2, 3)
            5.0
        """
        return round(a + b, self.precision)

    def divide(self, a: float, b: float) -> float:
        """Делит a на b.

        Args:
            a: делимое.
            b: делитель.

        Returns:
            float: результат деления, округлённый до self.precision знаков.

        Raises:
            ZeroDivisionError: если b равно нулю.

        Example:
            >>> Calculator().divide(10, 2)
            5.0
        """
        if b == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        return round(a / b, self.precision)


def feature_a() -> None:
    """Функция-заглушка, сохранена для совместимости с тестами.

    Returns:
        None.
    """
    pass
