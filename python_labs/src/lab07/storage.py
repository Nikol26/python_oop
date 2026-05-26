import json
from pathlib import Path

from models import Student


def save(students: list[Student], filepath: str) -> None:
    """Сохранить список студентов в JSON-файл."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [student.to_dict() for student in students]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load(filepath: str) -> list[Student]:
    """Загрузить список студентов из JSON-файла."""
    path = Path(filepath)

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Student.from_dict(item) for item in data]
