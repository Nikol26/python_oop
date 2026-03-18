from validate import (
    validate_name,
    validate_student_id,
    validate_course,
    validate_gpa,
    validate_status
)


class Student:
    MAX_COURSE = 6
    ACTIVE_STATUS = "active"
    EXPELLED_STATUS = "expelled"

    def __init__(self, name, student_id, course, gpa, status=ACTIVE_STATUS):
        self._name = validate_name(name)
        self._student_id = validate_student_id(student_id)
        self._course = validate_course(course, self.MAX_COURSE)
        self._gpa = validate_gpa(gpa)
        self._status = validate_status(status, self.ACTIVE_STATUS, self.EXPELLED_STATUS)

    @property
    def name(self):
        return self._name

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if self._status != self.ACTIVE_STATUS:
            raise ValueError("Cannot change GPA for an expelled student.")
        self._gpa = validate_gpa(value)

    @property
    def status(self):
        return self._status

    def promote(self):
        if self._status != self.ACTIVE_STATUS:
            raise ValueError("Cannot promote an expelled student.")
        if self._course >= self.MAX_COURSE:
            raise ValueError(f"Cannot promote student beyond course {self.MAX_COURSE}.")
        self._course += 1

    def expel(self):
        if self._status == self.EXPELLED_STATUS:
            raise ValueError("Student is already expelled.")
        self._status = self.EXPELLED_STATUS

    def __str__(self):
        return (
            f"Student: {self._name} | "
            f"ID: {self._student_id} | "
            f"Course: {self._course} | "
            f"GPA: {self._gpa:.2f} | "
            f"Status: {self._status}"
        )

    def __repr__(self):
        return (
            f"Student(name={self._name!r}, "
            f"student_id={self._student_id!r}, "
            f"course={self._course!r}, "
            f"gpa={self._gpa!r}, "
            f"status={self._status!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id
    