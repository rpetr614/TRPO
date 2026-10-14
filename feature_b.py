"""Модуль feature_b: менеджер задач.

Демонстрирует перечисление (Enum), dataclass и управление состоянием
списка задач — для разнообразия в документации pdoc.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    """Статус задачи в списке дел."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """Единица задачи в TaskManager.

    Attributes:
        title: название задачи.
        status: текущий статус задачи (см. TaskStatus).
    """

    title: str
    status: TaskStatus = TaskStatus.TODO


class TaskManager:
    """Управляет списком задач: добавление, завершение, фильтрация."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        """Добавляет новую задачу со статусом TODO.

        Args:
            title: название задачи.

        Returns:
            Task: созданная задача.

        Example:
            >>> tm = TaskManager()
            >>> tm.add_task("Написать отчёт").status
            <TaskStatus.TODO: 'todo'>
        """
        task = Task(title=title)
        self._tasks.append(task)
        return task

    def complete_task(self, title: str) -> bool:
        """Отмечает задачу с указанным названием как выполненную.

        Args:
            title: название задачи, которую нужно завершить.

        Returns:
            bool: True, если задача найдена и обновлена, иначе False.
        """
        for task in self._tasks:
            if task.title == title:
                task.status = TaskStatus.DONE
                return True
        return False

    def pending_tasks(self) -> list[Task]:
        """Возвращает список незавершённых задач.

        Returns:
            list[Task]: задачи со статусом, отличным от DONE.
        """
        return [t for t in self._tasks if t.status != TaskStatus.DONE]


def feature_b() -> None:
    """Функция-заглушка, сохранена для совместимости с тестами.

    Returns:
        None.
    """
    pass
