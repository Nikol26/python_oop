from __future__ import annotations

import sys
import importlib.util
from pathlib import Path

from container import Displayable, Scorable, TypedCollection


LAB03_DIR: Path = Path(__file__).resolve().parents[1] / "lab03"

if str(LAB03_DIR) not in sys.path:
    sys.path.insert(0, str(LAB03_DIR))

spec = importlib.util.spec_from_file_location("lab03_models_for_lab06", LAB03_DIR / "models.py")
lab03_models = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab03_models)

BachelorStudent = lab03_models.BachelorStudent
MasterStudent = lab03_models.MasterStudent
PhDStudent = lab03_models.PhDStudent


def get_field(obj: object, name: str) -> object:
    """Получить значение поля объекта."""
    return getattr(obj, f"_{name}", getattr(obj, name, None))


class TypedBachelorStudent(BachelorStudent):
    """Бакалавр с методами display() и score() для Protocol."""

    def display(self) -> str:
        return (
            f"Бакалавр: {get_field(self, 'name')} | "
            f"ID: {get_field(self, 'student_id')} | "
            f"Курс: {get_field(self, 'course')} | "
            f"GPA: {get_field(self, 'gpa')} | "
            f"Направление: {get_field(self, 'major')}"
        )

    def score(self) -> float:
        return float(get_field(self, "gpa"))


class TypedMasterStudent(MasterStudent):
    """Магистр с методами display() и score() для Protocol."""

    def display(self) -> str:
        return (
            f"Магистр: {get_field(self, 'name')} | "
            f"ID: {get_field(self, 'student_id')} | "
            f"Курс: {get_field(self, 'course')} | "
            f"GPA: {get_field(self, 'gpa')} | "
            f"Программа: {get_field(self, 'program_name')}"
        )

    def score(self) -> float:
        return float(get_field(self, "gpa"))


class TypedPhDStudent(PhDStudent):
    """Аспирант с методами display() и score() для Protocol."""

    def display(self) -> str:
        return (
            f"Аспирант: {get_field(self, 'name')} | "
            f"ID: {get_field(self, 'student_id')} | "
            f"Курс: {get_field(self, 'course')} | "
            f"GPA: {get_field(self, 'gpa')} | "
            f"Тема: {get_field(self, 'thesis_topic')}"
        )

    def score(self) -> float:
        return float(get_field(self, "gpa"))


def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def create_students() -> list[Displayable]:
    return [
        TypedBachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная"),
        TypedBachelorStudent("Мария", "B-102", 1, 4.3, "Информатика", "очная"),
        TypedMasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы"),
        TypedMasterStudent("Олег", "M-202", 2, 4.5, "Прикладная математика", "Моделирование"),
        TypedPhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров"),
    ]


def scenario_1_typed_collection() -> TypedCollection[Displayable]:
    print_header("СЦЕНАРИЙ 1: ТИПИЗИРОВАННАЯ КОЛЛЕКЦИЯ TypedCollection[Displayable]")

    collection: TypedCollection[Displayable] = TypedCollection(Displayable)

    for student in create_students():
        collection.add(student)

    print("Все объекты в коллекции:")
    for student in collection.get_all():
        print(student.display())

    print("\nПроверка валидации типа:")
    try:
        collection.add("Это не студент")
    except TypeError as error:
        print(f"Ошибка добавления: {error}")

    return collection


def scenario_2_find_filter_map(collection: TypedCollection[Displayable]) -> None:
    print_header("СЦЕНАРИЙ 2: find(), filter(), map() И ИЗМЕНЕНИЕ ТИПА РЕЗУЛЬТАТА")

    found: Displayable | None = collection.find(
        lambda student: str(get_field(student, "name")) == "Иван"
    )
    print("find(): найденный элемент:")
    print(found.display() if found is not None else "Ничего не найдено")

    not_found: Displayable | None = collection.find(
        lambda student: str(get_field(student, "name")) == "Никита"
    )
    print("\nfind(): поиск несуществующего элемента:")
    print(not_found.display() if not_found is not None else "None")

    filtered: list[Displayable] = collection.filter(
        lambda student: float(get_field(student, "gpa")) >= 4.7
    )
    print("\nfilter(): студенты с GPA >= 4.7:")
    for student in filtered:
        print(student.display())

    names: list[str] = collection.map(lambda student: str(get_field(student, "name")))
    print("\nmap(): результат list[str] — имена студентов:")
    print(names)

    gpa_values: list[float] = collection.map(lambda student: float(get_field(student, "gpa")))
    print("\nmap(): результат list[float] — GPA студентов:")
    print(gpa_values)


def scenario_3_protocol_displayable() -> None:
    print_header("СЦЕНАРИЙ 3: Protocol Displayable БЕЗ ЯВНОГО НАСЛЕДОВАНИЯ")

    display_collection: TypedCollection[Displayable] = TypedCollection(Displayable)

    display_collection.add(TypedBachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная"))
    display_collection.add(TypedMasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы"))
    display_collection.add(TypedPhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров"))

    print("Объекты не наследуются от Displayable явно, но имеют метод display():")
    for item in display_collection:
        print(item.display())
        print(f"isinstance(item, Displayable): {isinstance(item, Displayable)}")


def scenario_4_protocol_scorable() -> None:
    print_header("СЦЕНАРИЙ 4: Protocol Scorable И СОРТИРОВКА ПО score()")

    score_collection: TypedCollection[Scorable] = TypedCollection(Scorable)

    score_collection.add(TypedBachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная"))
    score_collection.add(TypedMasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы"))
    score_collection.add(TypedPhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров"))

    print("Оценки объектов через score():")
    for item in score_collection:
        print(f"{item.display()} | score = {item.score()}")

    sorted_collection: TypedCollection[Scorable] = score_collection.sort_by(
        lambda item: item.score(),
        reverse=True
    )

    print("\nСортировка TypedCollection[Scorable] по score():")
    for item in sorted_collection:
        print(f"{item.display()} | score = {item.score()}")


def main() -> None:
    collection = scenario_1_typed_collection()
    scenario_2_find_filter_map(collection)
    scenario_3_protocol_displayable()
    scenario_4_protocol_scorable()


if __name__ == "__main__":
    main()
