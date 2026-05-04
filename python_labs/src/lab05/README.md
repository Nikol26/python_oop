# Лабораторная работа №5 — Функции как аргументы. Стратегии и делегаты

## 1. Цель работы

Освоить передачу функций как аргументов в другие функции и методы.

В ходе лабораторной работы были изучены:

- функции как аргументы;
- функции высшего порядка;
- встроенные функции `map()`, `filter()`, `sorted()`;
- `lambda`-выражения;
- фабрики функций;
- замыкания;
- паттерн «Стратегия»;
- callable-объекты;
- интеграция функционального стиля с объектно-ориентированным кодом.

Лабораторная работа построена на основе предыдущих работ:

- ЛР-1 — класс предметной области;
- ЛР-2 — коллекция объектов;
- ЛР-3 — иерархия классов студентов.

---

## 2. Реализованные функции и стратегии

В лабораторной работе используется предметная область **студенты**.

Создана коллекция `StrategyStudentCollection`, которая поддерживает:

- сортировку через функции-стратегии;
- фильтрацию через функции-предикаты;
- обработку элементов через произвольную функцию;
- цепочку операций.

---

### 2.1. Стратегии сортировки

В файле `strategies.py` реализованы функции-стратегии сортировки.

### `by_name(student)`

Сортирует студентов по имени.

Используется для алфавитной сортировки коллекции.

### `by_gpa(student)`

Сортирует студентов по среднему баллу `GPA`.

Используется для поиска студентов с лучшей успеваемостью.

### `by_course_and_gpa(student)`

Сортирует студентов сразу по двум признакам:

- курс;
- GPA.

Это демонстрирует стратегию сортировки по нескольким атрибутам одновременно.

---

### 2.2. Функции-фильтры

В лабораторной работе реализованы функции-фильтры.

### `is_high_gpa(student)`

Фильтрует студентов, у которых `GPA >= 4.7`.

### `is_bachelor(student)`

Фильтрует только студентов типа `BachelorStudent`.

Для проверки типа используется `isinstance()`.

---

### 2.3. Использование `filter()`

Фильтрация реализуется через встроенную функцию `filter()`.

В коллекции это используется в методе:

```python
def filter_by(self, predicate):
    return StrategyStudentCollection(list(filter(predicate, self._items)))@'
```
Метод принимает функцию-предикат и возвращает новую коллекцию с подходящими объектами.

---

### 2.4. Использование map()

Для преобразования объектов используется встроенная функция map().

Функция map() применяет переданную функцию к каждому элементу коллекции.

В лабораторной работе map() используется для преобразования студентов:

- в строки
- в словари
- в список имён

Пример:
```python
strings = list(map(student_to_string, collection))
dictionaries = list(map(student_to_dict, collection))
names = list(map(lambda student: student_to_dict(student)["name"], collection))
```

---

### 2.5. Lambda-выражения

lambda — это короткая функция без имени.

Используется, когда функция нужна один раз.

Пример:
```python

names = list(map(lambda student: student_to_dict(student)["name"], collection))
collection.sort_by(lambda student: student_to_dict(student)["course"])
```
---

### 2.6. Фабрики функций

Фабрика функций — это функция, которая возвращает другую функцию.

Пример:
```python

def make_gpa_filter(min_gpa):
    def filter_fn(student):
        return student._gpa >= min_gpa
    return filter_fn
```

Использование:
```python
gpa_filter = make_gpa_filter(4.6)
filtered = collection.filter_by(gpa_filter)
```

---

### 2.7. Паттерн «Стратегия»

Стратегия — это способ менять поведение программы без изменения кода.

В работе стратегии передаются как функции.

Пример:
```python
collection.sort_by(by_name)
collection.sort_by(by_gpa)
collection.sort_by(lambda student: student._course)
```

Коллекция не знает, какая стратегия используется.

---

### 2.8. Callable-объекты

Callable-объект — это объект, который можно вызвать как функцию.

Для этого используется метод __call__().

Пример:
```python
class GpaBonusStrategy:
    def __init__(self, bonus):
        self._bonus = bonus

    def __call__(self, student):
        return student._gpa + self._bonus
```
Использование:
```python

strategy = GpaBonusStrategy(0.2)
collection.apply(strategy)
```
---

## 3. Коллекция StrategyStudentCollection

Коллекция содержит методы:

- add(item) — добавляет объект
- get_all() — возвращает все объекты
- sort_by(key_func) — сортирует через функцию
- filter_by(predicate) — фильтрует через функцию
- apply(func) — применяет функцию ко всем элементам

---

## 4. Демонстрация работы

Сценарий 1 — сортировка и фильтрация

<img width="911" height="1091" alt="image" src="https://github.com/user-attachments/assets/414a7cec-3453-4463-ba4a-909dd3a837b6" />


Показана сортировка:

- по имени
- по GPA
- по курсу и GPA

И фильтрация:

- по GPA
- по типу

---

Сценарий 2 — map, lambda и фабрики

<img width="1264" height="1083" alt="image" src="https://github.com/user-attachments/assets/809a812e-ae8d-4146-90f4-6ae4526483ca" />

Показано:

- map() для преобразования
- lambda
- фабрика функций

---

Сценарий 3 — цепочка операций

<img width="928" height="280" alt="image" src="https://github.com/user-attachments/assets/af7f34a3-9c72-4a2e-a715-a39e4690e500" />

filter → sort → apply

---

Сценарий 4 — замена стратегии

<img width="912" height="697" alt="image" src="https://github.com/user-attachments/assets/f1c39bde-7c55-48cd-8e65-e64f577de671" />

Передаём разные функции без изменения коллекции

---

Сценарий 5 — callable-объекты

<img width="913" height="687" alt="image" src="https://github.com/user-attachments/assets/75b90400-7b0e-4974-bc9a-a3a328461a42" />

Используются классы как функции

---

## 5. Вывод

В работе изучено:

- функции как аргументы
- map, filter, sorted
- lambda
- фабрики функций
- замыкания
- паттерн Стратегия
- callable-объекты

Функции позволяют менять поведение программы без изменения кода коллекции.
