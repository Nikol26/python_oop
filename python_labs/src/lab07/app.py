from exceptions import DuplicateStudentError, StudentNotFoundError, ValidationError
from models import Student
import storage


class StudentApp:
    """Бизнес-логика приложения для работы со студентами."""

    def __init__(self, filepath: str) -> None:
        self.__filepath = filepath
        self.__students: list[Student] = storage.load(filepath)

    def add_student(self, full_name: str, group: str, course: int, gpa: float) -> None:
        """Добавить студента."""
        try:
            student = Student(full_name, group, course, gpa)
        except ValueError as error:
            raise ValidationError(str(error))

        if student in self.__students:
            raise DuplicateStudentError("такой студент уже есть")

        self.__students.append(student)

    def get_all_students(self) -> list[Student]:
        """Вернуть всех студентов."""
        return list(self.__students)

    def find_student(self, full_name: str) -> Student:
        """Найти студента по ФИО."""
        query = full_name.strip().lower()

        for student in self.__students:
            if student.full_name.lower() == query:
                return student

        raise StudentNotFoundError("студент не найден")

    def delete_student(self, full_name: str) -> None:
        """Удалить студента по ФИО."""
        student = self.find_student(full_name)
        self.__students.remove(student)

    def filter_by_gpa(self, min_gpa: float) -> list[Student]:
        """Отфильтровать студентов по минимальному GPA."""
        if min_gpa < 2.0 or min_gpa > 5.0:
            raise ValidationError("GPA должен быть от 2.0 до 5.0")

        return [student for student in self.__students if student.gpa >= min_gpa]

    def sort_students(self, strategy: str) -> list[Student]:
        """Отсортировать студентов по выбранной стратегии."""
        if strategy == "name":
            return sorted(self.__students, key=lambda student: student.full_name)
        if strategy == "course":
            return sorted(self.__students, key=lambda student: student.course)
        if strategy == "gpa":
            return sorted(self.__students, key=lambda student: student.gpa, reverse=True)

        raise ValidationError("неизвестная стратегия сортировки")

    def promote_student(self, full_name: str) -> None:
        """Перевести студента на следующий курс."""
        student = self.find_student(full_name)

        try:
            student.promote()
        except ValueError as error:
            raise ValidationError(str(error))

    def update_student_gpa(self, full_name: str, new_gpa: float) -> None:
        """Изменить GPA студента."""
        student = self.find_student(full_name)

        try:
            student.update_gpa(new_gpa)
        except ValueError as error:
            raise ValidationError(str(error))

    def save(self) -> None:
        """Сохранить данные в файл."""
        storage.save(self.__students, self.__filepath)
