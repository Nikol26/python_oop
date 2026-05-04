import sys
import importlib.util
from pathlib import Path


LAB03_DIR = Path(__file__).resolve().parents[1] / "lab03"

if str(LAB03_DIR) not in sys.path:
    sys.path.insert(0, str(LAB03_DIR))

spec = importlib.util.spec_from_file_location("lab03_models_for_lab05", LAB03_DIR / "models.py")
lab03_models = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab03_models)

BachelorStudent = lab03_models.BachelorStudent
MasterStudent = lab03_models.MasterStudent
PhDStudent = lab03_models.PhDStudent


def get_field(obj, name):
    """Возвращает значение поля объекта по имени."""
    return getattr(obj, f"_{name}", getattr(obj, name, None))


def by_name(student):
    """Стратегия сортировки по имени студента."""
    return get_field(student, "name")


def by_gpa(student):
    """Стратегия сортировки по среднему баллу GPA."""
    return get_field(student, "gpa")


def by_course_and_gpa(student):
    """Стратегия сортировки по курсу и GPA одновременно."""
    return (get_field(student, "course"), get_field(student, "gpa"))


def is_high_gpa(student):
    """Фильтр: выбирает студентов с GPA выше или равным 4.7."""
    return get_field(student, "gpa") >= 4.7


def is_bachelor(student):
    """Фильтр: выбирает только бакалавров."""
    return isinstance(student, BachelorStudent)


def make_gpa_filter(min_gpa):
    """Фабрика функций: создаёт фильтр по минимальному GPA."""
    def filter_fn(student):
        return get_field(student, "gpa") >= min_gpa
    return filter_fn


def student_to_string(student):
    """Преобразует объект студента в строку."""
    return (
        f"{student.__class__.__name__}: "
        f"{get_field(student, 'name')} | "
        f"ID: {get_field(student, 'student_id')} | "
        f"Курс: {get_field(student, 'course')} | "
        f"GPA: {get_field(student, 'gpa')} | "
        f"Статус: {get_field(student, 'status')}"
    )


def student_to_dict(student):
    """Преобразует объект студента в словарь."""
    return {
        "type": student.__class__.__name__,
        "name": get_field(student, "name"),
        "student_id": get_field(student, "student_id"),
        "course": get_field(student, "course"),
        "gpa": get_field(student, "gpa"),
        "status": get_field(student, "status"),
    }


def add_bonus_gpa(student):
    """Обработчик: добавляет студенту временный бонус GPA для вывода."""
    old_gpa = get_field(student, "gpa")
    new_gpa = min(old_gpa + 0.1, 5.0)

    return (
        f"{get_field(student, 'name')} | "
        f"старый GPA: {old_gpa:.2f} | "
        f"новый GPA с бонусом: {new_gpa:.2f}"
    )


def make_bonus_strategy(bonus):
    """Фабрика функций: создаёт обработчик для добавления бонуса к GPA."""
    def bonus_strategy(student):
        old_gpa = get_field(student, "gpa")
        new_gpa = min(old_gpa + bonus, 5.0)
        return f"{get_field(student, 'name')}: {old_gpa:.2f} -> {new_gpa:.2f}"
    return bonus_strategy


class GpaBonusStrategy:
    """Callable-стратегия для начисления бонуса к GPA."""

    def __init__(self, bonus):
        self._bonus = bonus

    def __call__(self, student):
        old_gpa = get_field(student, "gpa")
        new_gpa = min(old_gpa + self._bonus, 5.0)
        return f"{get_field(student, 'name')} получил бонус {self._bonus:.2f}: {old_gpa:.2f} -> {new_gpa:.2f}"


class ShortInfoStrategy:
    """Callable-стратегия для краткого вывода информации о студенте."""

    def __call__(self, student):
        return f"{get_field(student, 'name')} | GPA: {get_field(student, 'gpa')} | Курс: {get_field(student, 'course')}"
