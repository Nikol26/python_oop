class AppError(Exception):
    """Базовое исключение приложения."""
    pass


class StudentNotFoundError(AppError):
    """Студент не найден."""
    pass


class DuplicateStudentError(AppError):
    """Студент с таким именем и группой уже существует."""
    pass


class ValidationError(AppError):
    """Ошибка проверки данных."""
    pass
