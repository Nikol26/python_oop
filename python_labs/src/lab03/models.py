from base import Student


class BachelorStudent(Student):
    def __init__(self, name, student_id, course, gpa, major, study_form, status=Student.ACTIVE_STATUS):
        super().__init__(name, student_id, course, gpa, status)
        self._major = major
        self._study_form = study_form

    @property
    def major(self):
        return self._major

    @property
    def study_form(self):
        return self._study_form

    def choose_elective(self, elective_name):
        return f"{self.name} выбрал электив: {elective_name}"

    def display(self):
        return f"Бакалавр: {self.name} | Направление: {self.major} | Форма обучения: {self.study_form}"

    def __str__(self):
        return (
            f"BachelorStudent: {self.name} | ID: {self.student_id} | "
            f"Course: {self.course} | GPA: {self.gpa:.2f} | "
            f"Major: {self.major} | Study form: {self.study_form} | Status: {self.status}"
        )


class MasterStudent(Student):
    def __init__(self, name, student_id, course, gpa, program_name, research_area, status=Student.ACTIVE_STATUS):
        super().__init__(name, student_id, course, gpa, status)
        self._program_name = program_name
        self._research_area = research_area

    @property
    def program_name(self):
        return self._program_name

    @property
    def research_area(self):
        return self._research_area

    def submit_research_plan(self):
        return f"{self.name} отправил исследовательский план по теме '{self.research_area}'"

    def display(self):
        return f"Магистр: {self.name} | Программа: {self.program_name} | Область: {self.research_area}"

    def __str__(self):
        return (
            f"MasterStudent: {self.name} | ID: {self.student_id} | "
            f"Course: {self.course} | GPA: {self.gpa:.2f} | "
            f"Program: {self.program_name} | Research area: {self.research_area} | Status: {self.status}"
        )


class PhDStudent(Student):
    def __init__(self, name, student_id, course, gpa, thesis_topic, supervisor, status=Student.ACTIVE_STATUS):
        super().__init__(name, student_id, course, gpa, status)
        self._thesis_topic = thesis_topic
        self._supervisor = supervisor

    @property
    def thesis_topic(self):
        return self._thesis_topic

    @property
    def supervisor(self):
        return self._supervisor

    def publish_article(self):
        return f"{self.name} опубликовал статью по теме '{self.thesis_topic}'"

    def display(self):
        return f"Аспирант: {self.name} | Тема: {self.thesis_topic} | Научрук: {self.supervisor}"

    def __str__(self):
        return (
            f"PhDStudent: {self.name} | ID: {self.student_id} | "
            f"Course: {self.course} | GPA: {self.gpa:.2f} | "
            f"Thesis: {self.thesis_topic} | Supervisor: {self.supervisor} | Status: {self.status}"
        )
