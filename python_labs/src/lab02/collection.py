from model import Student


class StudentCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Student):
            raise TypeError("Можно добавлять только объекты Student.")

        for student in self._items:
            if student.student_id == item.student_id:
                raise ValueError("Студент с таким ID уже существует.")

        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def get_all(self):
        return list(self._items)

    def find_by_id(self, student_id):
        for student in self._items:
            if student.student_id == student_id:
                return student
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def remove_at(self, index):
        del self._items[index]

    def sort_by_name(self):
        self._items.sort(key=lambda student: student.name)

    def get_active(self):
        new_collection = StudentCollection()
        for student in self._items:
            if student.status == Student.ACTIVE_STATUS:
                new_collection.add(student)
        return new_collection

    def __str__(self):
        return "\n".join(str(student) for student in self._items)
