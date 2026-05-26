class Student:
    """Модель студента университета."""

    def __init__(self, full_name: str, group: str, course: int, gpa: float) -> None:
        full_name = full_name.strip()
        group = group.strip()

        if not full_name:
            raise ValueError("имя пустое")
        if not group:
            raise ValueError("группа пустая")
        if not isinstance(course, int) or not (1 <= course <= 6):
            raise ValueError("курс вне 1–6")
        if not isinstance(gpa, (int, float)) or not (2.0 <= float(gpa) <= 5.0):
            raise ValueError("GPA вне 2.0–5.0")

        self.__full_name = full_name
        self.__group = group
        self.__course = course
        self.__gpa = float(gpa)

    @property
    def full_name(self) -> str:
        """Вернуть ФИО студента."""
        return self.__full_name

    @property
    def group(self) -> str:
        """Вернуть группу студента."""
        return self.__group

    @property
    def course(self) -> int:
        """Вернуть курс студента."""
        return self.__course

    @property
    def gpa(self) -> float:
        """Вернуть средний балл студента."""
        return self.__gpa

    def promote(self) -> None:
        """Перевести студента на следующий курс."""
        if self.__course == 6:
            raise ValueError("студент уже на 6 курсе")
        self.__course += 1

    def update_gpa(self, new_gpa: float) -> None:
        """Обновить GPA студента."""
        if not isinstance(new_gpa, (int, float)) or not (2.0 <= float(new_gpa) <= 5.0):
            raise ValueError("GPA вне 2.0–5.0")
        self.__gpa = float(new_gpa)

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь для сохранения."""
        return {
            "full_name": self.__full_name,
            "group": self.__group,
            "course": self.__course,
            "gpa": self.__gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """Создать студента из словаря."""
        return cls(
            data["full_name"],
            data["group"],
            int(data["course"]),
            float(data["gpa"]),
        )

    def __str__(self) -> str:
        """Вернуть строковое представление студента."""
        return f"{self.__full_name} ({self.__group}, курс {self.__course}, GPA {self.__gpa})"

    def __eq__(self, other: object) -> bool:
        """Сравнить студентов по ФИО и группе."""
        return (
            isinstance(other, Student)
            and self.__full_name == other.__full_name
            and self.__group == other.__group
        )
