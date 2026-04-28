from interfaces import Printable, Comparable
from models import (
    PrintableBachelorStudent,
    PrintableMasterStudent,
    PrintablePhDStudent,
    InterfaceStudentCollection,
)


def print_header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_all(items: list[Printable]):
    """Универсальная функция, работающая через интерфейс Printable."""
    for item in items:
        print(item.to_string())


def show_comparison(first: Comparable, second: Comparable):
    """Универсальная функция, работающая через интерфейс Comparable."""
    result = first.compare_to(second)

    if result > 0:
        print("Первый объект имеет GPA выше")
    elif result < 0:
        print("Второй объект имеет GPA выше")
    else:
        print("GPA одинаковый")


def scenario_1_create_objects():
    print_header("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И ВЫЗОВ ИНТЕРФЕЙСНЫХ МЕТОДОВ")

    bachelor = PrintableBachelorStudent(
        "Анна", "B-101", 2, 4.7,
        "Материаловедение", "очная"
    )

    master = PrintableMasterStudent(
        "Иван", "M-201", 1, 4.8,
        "Инженерные системы", "Наноматериалы"
    )

    phd = PrintablePhDStudent(
        "Сергей", "P-301", 3, 4.9,
        "Новые сплавы", "Проф. Петров"
    )

    print(bachelor.to_string())
    print(master.to_string())
    print(phd.to_string())

    return bachelor, master, phd


def scenario_2_universal_function(students):
    print_header("СЦЕНАРИЙ 2: УНИВЕРСАЛЬНАЯ ФУНКЦИЯ ЧЕРЕЗ ИНТЕРФЕЙС Printable")

    print_all(students)


def scenario_3_isinstance(students):
    print_header("СЦЕНАРИЙ 3: ПРОВЕРКА ИНТЕРФЕЙСОВ ЧЕРЕЗ isinstance()")

    for student in students:
        print(student.to_string())
        print(f"Printable: {isinstance(student, Printable)}")
        print(f"Comparable: {isinstance(student, Comparable)}")
        print("-" * 50)


def scenario_4_comparable(bachelor, master):
    print_header("СЦЕНАРИЙ 4: СРАВНЕНИЕ ЧЕРЕЗ ИНТЕРФЕЙС Comparable")

    print(bachelor.to_string())
    print(master.to_string())
    show_comparison(bachelor, master)


def scenario_5_collection(students):
    print_header("СЦЕНАРИЙ 5: КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСАМ")

    collection = InterfaceStudentCollection()

    for student in students:
        collection.add(student)

    print("Все Printable-объекты:")
    for item in collection.get_printable():
        print(item.to_string())

    print("\nВсе Comparable-объекты:")
    for item in collection.get_comparable():
        print(item.to_string())

    return collection


def scenario_6_sorting(collection):
    print_header("СЦЕНАРИЙ 6: АРХИТЕКТУРНОЕ ПОВЕДЕНИЕ — СОРТИРОВКА ЧЕРЕЗ Comparable")

    sorted_students = collection.sort_by_gpa(reverse=True)

    print("Студенты отсортированы по GPA:")
    for student in sorted_students:
        print(student.to_string())


def main():
    bachelor, master, phd = scenario_1_create_objects()

    students = [bachelor, master, phd]

    scenario_2_universal_function(students)
    scenario_3_isinstance(students)
    scenario_4_comparable(bachelor, master)
    collection = scenario_5_collection(students)
    scenario_6_sorting(collection)


if __name__ == "__main__":
    main()
