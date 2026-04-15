from models import BachelorStudent, MasterStudent, PhDStudent
from collection import StudentCollection


def print_block(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    b1 = BachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная")
    m1 = MasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы")
    p1 = PhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров")

    # СЦЕНАРИЙ 1
    print_block("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ")
    print(b1)
    print(m1)
    print(p1)

    # СЦЕНАРИЙ 2
    print_block("СЦЕНАРИЙ 2: МЕТОДЫ БАЗОВОГО И ДОЧЕРНИХ КЛАССОВ")
    print("Базовый метод promote():", b1.promote())
    print("Дочерний метод BachelorStudent:", b1.choose_elective("3D-моделирование"))
    print("Дочерний метод MasterStudent:", m1.submit_research_plan())
    print("Дочерний метод PhDStudent:", p1.publish_article())

    # СЦЕНАРИЙ 3
    print_block("СЦЕНАРИЙ 3: РАБОТА ЧЕРЕЗ ОДНУ КОЛЛЕКЦИЮ")
    group = StudentCollection()
    group.add(b1)
    group.add(m1)
    group.add(p1)

    print("Все объекты в одной коллекции:")
    for student in group:
        print(student)

    # СЦЕНАРИЙ 4
    print_block("СЦЕНАРИЙ 4: ПОЛИМОРФИЗМ ЧЕРЕЗ ОБЩИЙ МЕТОД display()")
    for student in group:
        print(student.display())

    # СЦЕНАРИЙ 5
    print_block("СЦЕНАРИЙ 5: ПРОВЕРКА ТИПОВ isinstance()")
    for student in group:
        if isinstance(student, BachelorStudent):
            print(f"{student.name} является BachelorStudent")
        elif isinstance(student, MasterStudent):
            print(f"{student.name} является MasterStudent")
        elif isinstance(student, PhDStudent):
            print(f"{student.name} является PhDStudent")

    # СЦЕНАРИЙ 6
    print_block("СЦЕНАРИЙ 6: ФИЛЬТРАЦИЯ ПО ТИПУ ЧЕРЕЗ КОЛЛЕКЦИЮ")
    print("Только бакалавры:")
    for student in group.get_only_bachelors():
        print(student)

    print("Только магистры:")
    for student in group.get_only_masters():
        print(student)

    print("Только аспиранты:")
    for student in group.get_only_phd():
        print(student)


if __name__ == "__main__":
    main()
