from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для объектов, которые можно вывести в строковом виде."""

    @abstractmethod
    def to_string(self) -> str:
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать между собой."""

    @abstractmethod
    def compare_to(self, other) -> int:
        pass
