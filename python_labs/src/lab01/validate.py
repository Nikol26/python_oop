def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    if len(name) < 2 or len(name) > 50:
        raise ValueError("Name length must be between 2 and 50 characters.")
    return name


def validate_student_id(student_id):
    if not isinstance(student_id, str):
        raise TypeError("Student ID must be a string.")
    student_id = student_id.strip()
    if not student_id:
        raise ValueError("Student ID cannot be empty.")
    if len(student_id) < 3 or len(student_id) > 20:
        raise ValueError("Student ID length must be between 3 and 20 characters.")
    return student_id


def validate_course(course, max_course):
    if not isinstance(course, int):
        raise TypeError("Course must be an integer.")
    if course < 1 or course > max_course:
        raise ValueError(f"Course must be between 1 and {max_course}.")
    return course


def validate_gpa(gpa):
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA must be a number.")
    gpa = float(gpa)
    if gpa < 0 or gpa > 5:
        raise ValueError("GPA must be between 0 and 5.")
    return gpa


def validate_status(status, active, expelled):
    if not isinstance(status, str):
        raise TypeError("Status must be a string.")
    status = status.strip().lower()
    if status not in {active, expelled}:
        raise ValueError(f"Status must be '{active}' or '{expelled}'.")
    return status
