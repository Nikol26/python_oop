from app import StudentApp
from exceptions import AppError


class StudentCLI:
    """Консольный интерфейс приложения."""

    def __init__(self, app: StudentApp) -> None:
        self.__app = app

    def run(self) -> None:
        """Запустить CLI-приложение."""
        print("Данные автоматически загружены.")

        while True:
            self.__print_menu()

            try:
                choice = int(input("Выберите пункт: "))
            except ValueError:
                print("Ошибка: введите число")
                continue

            try:
                if choice == 1:
                    self.__add_student()
                elif choice == 2:
                    self.__show_students(self.__app.get_all_students())
                elif choice == 3:
                    self.__find_student()
                elif choice == 4:
                    self.__delete_student()
                elif choice == 5:
                    self.__filter_students()
                elif choice == 6:
                    self.__sort_students()
                elif choice == 7:
                    self.__promote_student()
                elif choice == 8:
                    self.__update_gpa()
                elif choice == 0:
                    self.__app.save()
                    print("Данные сохранены. Выход.")
                    break
                else:
                    print("Ошибка: такого пункта меню нет")
            except AppError as error:
                print(f"Ошибка: {error}")

    def __print_menu(self) -> None:
        """Вывести меню."""
        print("\n" + "=" * 50)
        print("ЛР-7 — Консольное приложение")
        print("=" * 50)
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Найти студента")
        print("4. Удалить студента")
        print("5. Фильтр по GPA")
        print("6. Сортировка")
        print("7. Перевести на следующий курс")
        print("8. Обновить GPA")
        print("0. Выход")

    def __show_students(self, students: list) -> None:
        """Вывести студентов таблицей."""
        if not students:
            print("Список пуст")
            return

        print("-" * 78)
        print(f"{'№':<4} {'ФИО':<28} {'Группа':<14} {'Курс':<8} {'GPA':<6}")
        print("-" * 78)

        for index, student in enumerate(students, start=1):
            print(
                f"{index:<4} "
                f"{student.full_name:<28} "
                f"{student.group:<14} "
                f"{student.course:<8} "
                f"{student.gpa:<6}"
            )

        print("-" * 78)

    def __add_student(self) -> None:
        """Добавить студента через ввод."""
        full_name = input("ФИО: ")
        group = input("Группа: ")
        course = int(input("Курс: "))
        gpa = float(input("GPA: "))

        self.__app.add_student(full_name, group, course, gpa)
        print("Студент добавлен")

    def __find_student(self) -> None:
        """Найти студента через ввод."""
        full_name = input("Введите ФИО для поиска: ")
        student = self.__app.find_student(full_name)
        self.__show_students([student])

    def __delete_student(self) -> None:
        """Удалить студента с подтверждением."""
        full_name = input("Введите ФИО для удаления: ")
        student = self.__app.find_student(full_name)

        answer = input(f'Удалить "{student.full_name}"? (y/n): ').strip().lower()

        if answer == "y":
            self.__app.delete_student(full_name)
            print("Студент удалён")
        else:
            print("Удаление отменено")

    def __filter_students(self) -> None:
        """Отфильтровать студентов по GPA."""
        min_gpa = float(input("Минимальный GPA: "))
        students = self.__app.filter_by_gpa(min_gpa)
        self.__show_students(students)

    def __sort_students(self) -> None:
        """Отсортировать студентов."""
        print("Сортировать по:")
        print("1. ФИО")
        print("2. Курсу")
        print("3. GPA")

        choice = int(input("Выберите стратегию: "))

        if choice == 1:
            students = self.__app.sort_students("name")
        elif choice == 2:
            students = self.__app.sort_students("course")
        elif choice == 3:
            students = self.__app.sort_students("gpa")
        else:
            print("Ошибка: такой стратегии нет")
            return

        self.__show_students(students)

    def __promote_student(self) -> None:
        """Перевести студента на следующий курс."""
        full_name = input("Введите ФИО: ")
        self.__app.promote_student(full_name)
        print("Студент переведён на следующий курс")

    def __update_gpa(self) -> None:
        """Обновить GPA студента."""
        full_name = input("Введите ФИО: ")
        new_gpa = float(input("Новый GPA: "))

        self.__app.update_student_gpa(full_name, new_gpa)
        print("GPA обновлён")
