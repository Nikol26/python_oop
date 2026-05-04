from collection import StrategyStudentCollection
from strategies import (
    BachelorStudent,
    MasterStudent,
    PhDStudent,
    by_name,
    by_gpa,
    by_course_and_gpa,
    is_high_gpa,
    is_bachelor,
    make_gpa_filter,
    make_bonus_strategy,
    student_to_string,
    student_to_dict,
    add_bonus_gpa,
    GpaBonusStrategy,
    ShortInfoStrategy,
)


def print_header(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_collection(title, collection):
    print(f"\n{title}")
    for student in collection:
        print(student_to_string(student))


def create_collection():
    collection = StrategyStudentCollection()

    collection.add(BachelorStudent("Анна", "B-101", 2, 4.7, "Материаловедение", "очная"))
    collection.add(BachelorStudent("Мария", "B-102", 1, 4.3, "Информатика", "очная"))
    collection.add(MasterStudent("Иван", "M-201", 1, 4.8, "Инженерные системы", "Наноматериалы"))
    collection.add(MasterStudent("Олег", "M-202", 2, 4.5, "Прикладная математика", "Моделирование"))
    collection.add(PhDStudent("Сергей", "P-301", 3, 4.9, "Новые сплавы", "Проф. Петров"))

    return collection


def scenario_1_sorting_and_filtering(collection):
    print_header("СЦЕНАРИЙ 1: СОРТИРОВКА И ФИЛЬТРАЦИЯ ЧЕРЕЗ ФУНКЦИИ")

    print_collection("Исходная коллекция:", collection)

    sorted_by_name = collection.sort_by(by_name)
    print_collection("Сортировка по имени:", sorted_by_name)

    sorted_by_gpa = collection.sort_by(by_gpa, reverse=True)
    print_collection("Сортировка по GPA по убыванию:", sorted_by_gpa)

    sorted_by_course_and_gpa = collection.sort_by(by_course_and_gpa)
    print_collection("Сортировка по курсу и GPA:", sorted_by_course_and_gpa)

    high_gpa_students = collection.filter_by(is_high_gpa)
    print_collection("Фильтрация: GPA >= 4.7:", high_gpa_students)

    bachelors = collection.filter_by(is_bachelor)
    print_collection("Фильтрация: только бакалавры:", bachelors)


def scenario_2_map_lambda_factory(collection):
    print_header("СЦЕНАРИЙ 2: MAP, LAMBDA И ФАБРИКА ФУНКЦИЙ")

    print("\nmap(): преобразование студентов в строки")
    strings = list(map(student_to_string, collection))
    for item in strings:
        print(item)

    print("\nmap(): преобразование студентов в словари")
    dictionaries = list(map(student_to_dict, collection))
    for item in dictionaries:
        print(item)

    print("\nlambda: получение имён студентов")
    names = list(map(lambda student: student_to_dict(student)["name"], collection))
    print(names)

    print("\nФабрика функций: фильтр GPA >= 4.6")
    gpa_filter = make_gpa_filter(4.6)
    filtered = collection.filter_by(gpa_filter)
    print_collection("Результат фильтра из фабрики:", filtered)

    print("\nСравнение lambda и именованной функции")
    named_result = collection.filter_by(is_high_gpa)
    lambda_result = collection.filter_by(lambda student: student_to_dict(student)["gpa"] >= 4.7)

    print_collection("Через именованную функцию:", named_result)
    print_collection("Через lambda:", lambda_result)


def scenario_3_chain(collection):
    print_header("СЦЕНАРИЙ 3: ЦЕПОЧКА ОПЕРАЦИЙ filter -> sort -> apply")

    result = (
        collection
        .filter_by(is_high_gpa)
        .sort_by(by_gpa, reverse=True)
        .apply(add_bonus_gpa)
    )

    print("\nРезультат цепочки:")
    for item in result:
        print(item)


def scenario_4_strategy_replacement(collection):
    print_header("СЦЕНАРИЙ 4: ЗАМЕНА СТРАТЕГИИ БЕЗ ИЗМЕНЕНИЯ КОДА КОЛЛЕКЦИИ")

    print_collection("Сортировка стратегией by_name:", collection.sort_by(by_name))
    print_collection("Сортировка стратегией by_gpa:", collection.sort_by(by_gpa, reverse=True))
    print_collection("Сортировка стратегией lambda по курсу:", collection.sort_by(lambda student: student_to_dict(student)["course"]))


def scenario_5_callable_objects(collection):
    print_header("СЦЕНАРИЙ 5: CALLABLE-ОБЪЕКТЫ КАК СТРАТЕГИИ")

    bonus_strategy = GpaBonusStrategy(0.2)
    short_info_strategy = ShortInfoStrategy()

    print("\nCallable-стратегия GpaBonusStrategy:")
    for item in collection.apply(bonus_strategy):
        print(item)

    print("\nCallable-стратегия ShortInfoStrategy:")
    for item in collection.apply(short_info_strategy):
        print(item)

    print("\nФабрика функций make_bonus_strategy(0.3):")
    factory_strategy = make_bonus_strategy(0.3)
    for item in collection.apply(factory_strategy):
        print(item)


def main():
    collection = create_collection()

    scenario_1_sorting_and_filtering(collection)
    scenario_2_map_lambda_factory(collection)
    scenario_3_chain(collection)
    scenario_4_strategy_replacement(collection)
    scenario_5_callable_objects(collection)


if __name__ == "__main__":
    main()
