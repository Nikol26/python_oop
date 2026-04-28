import sys
import importlib.util
from pathlib import Path
from functools import cmp_to_key

from interfaces import Printable, Comparable


LAB03_DIR = Path(__file__).resolve().parents[1] / "lab03"

if str(LAB03_DIR) not in sys.path:
    sys.path.insert(0, str(LAB03_DIR))

spec = importlib.util.spec_from_file_location("lab03_models", LAB03_DIR / "models.py")
lab03_models = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab03_models)

BachelorStudent = lab03_models.BachelorStudent
MasterStudent = lab03_models.MasterStudent
PhDStudent = lab03_models.PhDStudent


def _field(obj, name):
    return getattr(obj, f"_{name}", getattr(obj, name, None))


class PrintableBachelorStudent(BachelorStudent, Printable, Comparable):
    def to_string(self) -> str:
        return (
            f"Бакалавр: {_field(self, 'name')} | "
            f"ID: {_field(self, 'student_id')} | "
            f"Курс: {_field(self, 'course')} | "
            f"GPA: {_field(self, 'gpa')} | "
            f"Направление: {_field(self, 'major')} | "
            f"Форма обучения: {_field(self, 'study_form')}"
        )

    def compare_to(self, other) -> int:
        if not isinstance(other, Comparable):
            raise TypeError("Объект должен реализовывать интерфейс Comparable")

        current_gpa = _field(self, "gpa")
        other_gpa = _field(other, "gpa")

        if current_gpa > other_gpa:
            return 1
        if current_gpa < other_gpa:
            return -1
        return 0


class PrintableMasterStudent(MasterStudent, Printable, Comparable):
    def to_string(self) -> str:
        return (
            f"Магистр: {_field(self, 'name')} | "
            f"ID: {_field(self, 'student_id')} | "
            f"Курс: {_field(self, 'course')} | "
            f"GPA: {_field(self, 'gpa')} | "
            f"Программа: {_field(self, 'program_name')} | "
            f"Область исследования: {_field(self, 'research_area')}"
        )

    def compare_to(self, other) -> int:
        if not isinstance(other, Comparable):
            raise TypeError("Объект должен реализовывать интерфейс Comparable")

        current_gpa = _field(self, "gpa")
        other_gpa = _field(other, "gpa")

        if current_gpa > other_gpa:
            return 1
        if current_gpa < other_gpa:
            return -1
        return 0


class PrintablePhDStudent(PhDStudent, Printable, Comparable):
    def to_string(self) -> str:
        return (
            f"Аспирант: {_field(self, 'name')} | "
            f"ID: {_field(self, 'student_id')} | "
            f"Курс: {_field(self, 'course')} | "
            f"GPA: {_field(self, 'gpa')} | "
            f"Тема: {_field(self, 'thesis_topic')} | "
            f"Научный руководитель: {_field(self, 'supervisor')}"
        )

    def compare_to(self, other) -> int:
        if not isinstance(other, Comparable):
            raise TypeError("Объект должен реализовывать интерфейс Comparable")

        current_gpa = _field(self, "gpa")
        other_gpa = _field(other, "gpa")

        if current_gpa > other_gpa:
            return 1
        if current_gpa < other_gpa:
            return -1
        return 0


class InterfaceStudentCollection:
    """Коллекция, которая умеет работать с объектами через интерфейсы."""

    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Printable):
            raise TypeError("Объект должен реализовывать интерфейс Printable")
        self._items.append(item)

    def get_all(self):
        return list(self._items)

    def get_printable(self):
        return [item for item in self._items if isinstance(item, Printable)]

    def get_comparable(self):
        return [item for item in self._items if isinstance(item, Comparable)]

    def sort_by_gpa(self, reverse=False):
        comparable_items = self.get_comparable()
        return sorted(
            comparable_items,
            key=cmp_to_key(lambda a, b: a.compare_to(b)),
            reverse=reverse
        )
