class StrategyStudentCollection:
    """Коллекция студентов с поддержкой стратегий сортировки, фильтрации и обработки."""

    def __init__(self, items=None):
        self._items = list(items) if items is not None else []

    def add(self, item):
        """Добавить объект в коллекцию."""
        self._items.append(item)

    def get_all(self):
        """Получить список всех объектов."""
        return list(self._items)

    def sort_by(self, key_func, reverse=False):
        """Отсортировать коллекцию через функцию-стратегию key_func."""
        return StrategyStudentCollection(sorted(self._items, key=key_func, reverse=reverse))

    def filter_by(self, predicate):
        """Отфильтровать коллекцию через функцию-предикат predicate."""
        return StrategyStudentCollection(list(filter(predicate, self._items)))

    def apply(self, func):
        """Применить произвольную функцию ко всем элементам коллекции."""
        return list(map(func, self._items))

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]
