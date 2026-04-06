from model import Student
from collection import StudentCollection


def print_block(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    group = StudentCollection()

    print_block("СЦЕНАРИЙ 1: ДОБАВЛЕНИЕ ОБЪЕКТОВ")
    s1 = Student("Анна", "ST-1", 2, 4.5)
    s2 = Student("Иван", "ST-2", 3, 4.2)
    s3 = Student("Сергей", "ST-3", 1, 3.9)

    group.add(s1)
    group.add(s2)
    group.add(s3)

    for student in group:
        print(student)

    print_block("СЦЕНАРИЙ 2: ПОИСК ПО ID")
    found = group.find_by_id("ST-2")
    print("Найденный студент:", found)

    print_block("СЦЕНАРИЙ 3: LEN И ИНДЕКСАЦИЯ")
    print("Количество студентов:", len(group))
    print("Первый студент:", group[0])

    print_block("СЦЕНАРИЙ 4: СОРТИРОВКА ПО ИМЕНИ")
    group.sort_by_name()
    for student in group:
        print(student)

    print_block("СЦЕНАРИЙ 5: ФИЛЬТРАЦИЯ АКТИВНЫХ")
    s2.expel()
    active_group = group.get_active()

    for student in active_group:
        print(student)

    print_block("СЦЕНАРИЙ 6: УДАЛЕНИЕ ПО ИНДЕКСУ")
    group.remove_at(0)

    for student in group:
        print(student)

    print_block("СЦЕНАРИЙ 7: ПРОВЕРКА ДУБЛИКАТОВ")
    try:
        duplicate = Student("Аня2", "ST-2", 2, 4.1)
        group.add(duplicate)
    except Exception as error:
        print("Ошибка:", error)

    print_block("СЦЕНАРИЙ 8: ПРОВЕРКА ТИПА")
    try:
        group.add("не студент")
    except Exception as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
