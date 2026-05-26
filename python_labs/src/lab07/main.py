from app import StudentApp
from cli import StudentCLI


def main() -> None:
    """Точка входа в приложение."""
    app = StudentApp("python_labs/src/lab07/data/students.json")
    cli = StudentCLI(app)
    cli.run()


if __name__ == "__main__":
    main()
