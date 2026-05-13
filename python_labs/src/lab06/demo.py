from future import annotations

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
    return getattr(obj, f"_{name}", getattr(obj, name, None))


class TypedBachelorStudent(BachelorStudent):
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
    print_header("СЦЕНАРИЙ 1: TypedCollection[Displayable] И ВАЛИДАЦИЯ ТИПОВ")

    collection: TypedCollection[Displayable] = TypedCollection(Displayable)

    for student in create_students():
        collection.add(student)

    print("Все элементы коллекции:")
    for student in collection.get_all():
        print(student.display())

    print("\nПроверка валидации типов:")
    try:
        collection.add("Обычная строка")
    except TypeError as error:
        print(f"Ошибка: {error}")

    return collection


def scenario_2_find_filter_map(collection: TypedCollection[Displayable]) -> None:
    print_header("СЦЕНАРИЙ 2: find(), filter(), map()")

    found: Displayable | None = collection.find(
        lambda student: str(get_field(student, "name")) == "Иван"
    )
    print("find(): найденный студент:")
    print(found.display() if found is not None else "None")

    not_found: Displayable | None = collection.find(
        lambda student: str(get_field(student, "name")) == "Никита"
    )
    print("\nfind(): несуществующий студент:")
    print(not_found.display() if not_found is not None else "None")

    filtered: list[Displayable] = collection.filter(
        lambda student: float(get_field(student, "gpa")) >= 4.7
    )
    print("\nfilter(): GPA >= 4.7:")
    for student in filtered:
        print(student.display())names: list[str] = collection.map(lambda student: str(get_field(student, "name")))
    print("\nmap(): результат list[str]:")
    print(names)

    gpa_values: list[float] = collection.map(lambda student: float(get_field(student, "gpa")))
    print("\nmap(): результат list[float]:")
    print(gpa_values)


def scenario_3_displayable_protocol() -> None:
    print_header("СЦЕНАРИЙ 3: Protocol Displayable БЕЗ ЯВНОГО НАСЛЕДОВАНИЯ")

    collection: TypedCollection[Displayable] = TypedCollection(Displayable)

    collection.add(TypedBachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная"))
    collection.add(TypedMasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы"))
    collection.add(TypedPhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров"))

    print("Объекты подходят под Displayable, потому что имеют метод display():")
    for item in collection:
        print(item.display())
        print(f"isinstance(item, Displayable): {isinstance(item, Displayable)}")


def scenario_4_scorable_protocol() -> None:
    print_header("СЦЕНАРИЙ 4: Protocol Scorable И TypedCollection[Scorable]")

    collection: TypedCollection[Scorable] = TypedCollection(Scorable)

    collection.add(TypedBachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная"))
    collection.add(TypedMasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы"))
    collection.add(TypedPhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров"))

    print("Объекты подходят под Scorable, потому что имеют метод score():")
    for item in collection:
        print(f"{item.display()} | score = {item.score()}")

    sorted_collection: TypedCollection[Scorable] = collection.sort_by(
        lambda item: item.score(),
        reverse=True
    )

    print("\nСортировка по score():")
    for item in sorted_collection:
        print(f"{item.display()} | score = {item.score()}")


def main() -> None:
    collection = scenario_1_typed_collection()
    scenario_2_find_filter_map(collection)
    scenario_3_displayable_protocol()
    scenario_4_scorable_protocol()


if name == "__main__":
    main()
