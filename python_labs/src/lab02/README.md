# Лабораторная работа №2: Коллекция объектов (Python)

## Выбранная предметная область

**Студенты**

Реализованный класс коллекции: **StudentCollection**

Коллекция для хранения и управления объектами `Student` из ЛР-1. Реализует контейнер для группы студентов с возможностью добавления, удаления, поиска, сортировки и фильтрации.

---

## Краткое описание класса

`StudentCollection` — это контейнерный класс для управления коллекцией студентов.  
Внутри хранит список объектов `Student`.

### Основные возможности

| Функция | Описание |
|---------|----------|
| Хранение | Список объектов `Student` |
| Управление | Добавление, удаление, доступ по индексу |
| Поиск | По `student_id` |
| Сортировка | По имени |
| Фильтрация | Получение активных студентов |
| Итерация | Поддержка цикла `for` |
| Защита | Проверка типа и дубликатов |

---

## Методы коллекции

### Базовые операции

| Метод | Описание |
|-------|----------|
| add(item) | Добавить студента |
| remove(item) | Удалить студента |
| remove_at(index) | Удалить по индексу |
| get_all() | Получить список |

### Поиск

| Метод | Описание |
|-------|----------|
| find_by_id(student_id) | Поиск по ID |

### Магические методы

| Метод | Описание |
|-------|----------|
| __len__ | Количество |
| __iter__ | Итерация |
| __getitem__ | Индексация |
| __str__ | Вывод |

### Сортировка

| Метод | Описание |
|-------|----------|
| sort_by_name() | Сортировка по имени |

### Фильтрация

| Метод | Описание |
|-------|----------|
| get_active() | Только активные |

---

## Демонстрация работы

В demo.py реализованы сценарии:

1. Добавление объектов
   <img width="852" height="195" alt="image" src="https://github.com/user-attachments/assets/164feb25-3259-4c84-ab62-d8c46379fecb" />
   
2. Поиск по ID
   <img width="1028" height="148" alt="image" src="https://github.com/user-attachments/assets/15cf6c56-135f-465e-b2e3-98830f23d928" />

3. len() и индексация
   <img width="954" height="168" alt="image" src="https://github.com/user-attachments/assets/e7e2f9b4-07be-4e16-92a8-3ae8c8d3a00d" />

4. Сортировка
   <img width="913" height="200" alt="image" src="https://github.com/user-attachments/assets/f3687844-facc-4634-9ddf-22195d45247b" />

5. Фильтрация
   
    <img width="769" height="165" alt="image" src="https://github.com/user-attachments/assets/4ab97a9f-078a-4bf6-b40d-4fb69f122fcc" />

6. Удаление
   
    <img width="779" height="176" alt="image" src="https://github.com/user-attachments/assets/d483d285-b513-4e7b-a55d-34c345047f14" />

7. Дубликаты
    
    <img width="727" height="149" alt="image" src="https://github.com/user-attachments/assets/02463028-0e2d-4798-a3e7-4a41902b0913" />

8. Проверка типа
    
    <img width="730" height="121" alt="image" src="https://github.com/user-attachments/assets/88bd8b15-d17b-46c9-81ed-97322a0aacf5" />

---

## Итог

Реализован контейнер `StudentCollection`, который:
- хранит объекты
- управляет ими
- поддерживает поиск, сортировку и фильтрацию

Показана разница между моделью (`Student`) и коллекцией.
'@ | Set-Content python_labs\src\lab02\README.md -Encoding UTF8
