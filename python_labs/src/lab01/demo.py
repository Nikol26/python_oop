from model import Student


def print_block(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # СЦЕНАРИЙ 1
    print_block("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТА И ВЫВОД")
    student1 = Student("Анна Петрова", "ST-101", 2, 4.6)
    print(student1)

    # СЦЕНАРИЙ 2
    print_block("СЦЕНАРИЙ 2: СРАВНЕНИЕ ОБЪЕКТОВ (__eq__)")
    student2 = Student("Анна Петрова", "ST-101", 2, 4.6)
    student3 = Student("Иван Иванов", "ST-102", 3, 4.2)

    print("student1 == student2:", student1 == student2)
    print("student1 == student3:", student1 == student3)

    # СЦЕНАРИЙ 3
    print_block("СЦЕНАРИЙ 3: ПРОВЕРКА SETTER И ВАЛИДАЦИИ")
    print("Старый GPA:", student1.gpa)

    student1.gpa = 4.9
    print("Новый GPA:", student1.gpa)

    try:
        student1.gpa = 6
    except Exception as error:
        print("Ошибка при установке GPA:", error)

    # СЦЕНАРИЙ 4
    print_block("СЦЕНАРИЙ 4: ДОСТУП К АТРИБУТАМ КЛАССА")
    print("Через класс:", Student.MAX_COURSE)
    print("Через объект:", student1.MAX_COURSE)

    # СЦЕНАРИЙ 5
    print_block("СЦЕНАРИЙ 5: СОСТОЯНИЕ ОБЪЕКТА И ОГРАНИЧЕНИЯ")
    print("Текущий статус:", student1.status)

    student1.expel()
    print("Статус после отчисления:", student1.status)

    try:
        student1.promote()
    except Exception as error:
        print("Ошибка при повышении:", error)

    try:
        student1.gpa = 4.0
    except Exception as error:
        print("Ошибка при изменении GPA:", error)

    # СЦЕНАРИЙ 6
    print_block("СЦЕНАРИЙ 6: НЕВЕРНОЕ СОЗДАНИЕ ОБЪЕКТА")

    try:
        Student("", "ST-200", 2, 4.0)
    except Exception as error:
        print("Ошибка 1:", error)

    try:
        Student("A", "ST-200", 2, 4.0)
    except Exception as error:
        print("Ошибка 2:", error)

    try:
        Student("Иван Иванов", "", 2, 4.0)
    except Exception as error:
        print("Ошибка 3:", error)

    try:
        Student("Иван Иванов", "ST-200", 10, 4.0)
    except Exception as error:
        print("Ошибка 4:", error)

    try:
        Student("Иван Иванов", "ST-200", 2, 10)
    except Exception as error:
        print("Ошибка 5:", error)

    # СЦЕНАРИЙ 7
    print_block("СЦЕНАРИЙ 7: БИЗНЕС-МЕТОД promote()")

    student4 = Student("Сергей Волков", "ST-300", 5, 4.3)
    print("До повышения:", student4)

    student4.promote()
    print("После повышения:", student4)

    try:
        student4.promote()
    except Exception as error:
        print("Ошибка при превышении курса:", error)


if __name__ == "__main__":
    main()