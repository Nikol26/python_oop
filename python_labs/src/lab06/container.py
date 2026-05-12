from __future__ import annotations

from typing import Callable, Generic, Iterator, Optional, Protocol, TypeVar, runtime_checkable


T = TypeVar("T")
R = TypeVar("R")


@runtime_checkable
class Displayable(Protocol):
    """Protocol для объектов, которые умеют возвращать строковое представление."""

    def display(self) -> str:
        ...


@runtime_checkable
class Scorable(Protocol):
    """Protocol для объектов, которые умеют возвращать числовую оценку."""

    def score(self) -> float:
        ...


D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


class TypedCollection(Generic[T]):
    """Generic-коллекция с аннотациями типов."""

    def __init__(self, expected_type: type | None = None) -> None:
        self._items: list[T] = []
        self._expected_type: type | None = expected_type

    def add(self, item: T) -> None:
        """Добавить объект в коллекцию."""
        if self._expected_type is not None and not isinstance(item, self._expected_type):
            raise TypeError(f"Можно добавлять только объекты типа {self._expected_type}")
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удалить объект из коллекции."""
        self._items.remove(item)

    def get_all(self) -> list[T]:
        """Получить все элементы коллекции."""
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Найти первый элемент, подходящий под условие."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Вернуть список всех элементов, подходящих под условие."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """Преобразовать каждый элемент коллекции и вернуть список результатов."""
        return [transform(item) for item in self._items]

    def sort_by(self, key_func: Callable[[T], object], reverse: bool = False) -> "TypedCollection[T]":
        """Отсортировать коллекцию по переданной функции."""
        result: TypedCollection[T] = TypedCollection(self._expected_type)
        result._items = sorted(self._items, key=key_func, reverse=reverse)
        return result

    def apply(self, func: Callable[[T], R]) -> list[R]:
        """Применить функцию ко всем элементам коллекции."""
        return [func(item) for item in self._items]

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]
