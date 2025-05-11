# Тест на создание ветки

# Задание 1: Типы переменных
"""Создай переменные следующих типов:
целое число
дробное число
строка
булево значение
список
и выведи их типы с помощью type()."""

# Ответ:


def task_1():
    age = 31
    height = 1.75
    last_name = 'Kulov'
    human = True
    food_like = ['nuttella', 'plov', 'pizza']

    print(type(age))
    print(type(height))
    print(type(last_name))
    print(type(human))
    print(type(food_like))


# Задание 2:
"""Булевы значения
Напиши программу, которая сравнивает два числа,
и выводит True, если первое больше,
и False — если нет."""

# Ответ:


def task_2():
    age_1 = 31
    age_2 = 25
    print(age_1 > age_2)
    print(age_1 < age_2)
    print(age_1 >= age_2)


# Задание 3:
"""Задание 3: 
Спроси у пользователя его имя и возраст.
Посчитай, сколько лет ему будет через 5 лет,
и выведи результат."""

# Ответ:


def task_3():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    future_age = age + 5
    print(f"Hello {name}, in 5 years you will be {future_age} years old.")


# Задание 4:
"""Суть: изменяемый список элементов

🔧 Задание:
Создай список из 5 фильмов, которые тебе
нравятся.

Выведи 1-й и 3-й фильм.
Добавь ещё один фильм в конец.
Удали второй фильм."""

# Ответ:


def task_4():
    movies = ['Inception', 'Interstellar', 'The Matrix', 'Avatar', 'Titanic']
    print(movies[0])
    print(movies[3])
    movies.append("The Fast and the Furious")
    movies.pop(3)


# Задание 5
"""Кортежи (tuple)

📌 Суть: список, который нельзя изменить

🔧 Задание:
Создай кортеж с координатами своей локации (город, улица).

Выведи обе координаты по отдельности."""

# Ответ:


def task_5():
    location = ("San Diego", "11548 Windcrest Ln")
    print('City:', location[0])
    print('Street:', location[1])


# Задание 6
"""Словари (dict)

📌 Суть: структура данных в формате "ключ: значение"

🔧 Задание:
Создай словарь с информацией о себе: имя, возраст, город.

Выведи фразу: Меня зовут Азамат, мне 30 лет, я из Сан-Диего.
Измени город на другой.
"""
# Ответ:


def task_6():
    profile = {
        'name': 'Azamat',
        'age': 31,
        'city': "San Diego"
    }
    print(
        f"My name is {profile['name']}, I am {profile['age']} yers old, I am leave in {profile['city']}")

    profile['city'] = "Los Angeles"
    print("City updated:", profile['city'])


# Задание 7
"""Множества (set)

📌 Суть: набор уникальных элементов, без повторов

🔧 Задание:
Создай множество из имён людей, с которыми ты работал.
Добавь пару имён (в том числе повторяющихся) 
и выведи список — чтобы увидеть, 
что повторы не сохраняются."""

# Ответ:


def task_7():
    customers = {'Bob', 'Michael', 'John', 'Tom'}
    customers.add('Ariana')
    customers.add('Michael')
    print(customers)


# Задание 8
"""Калькулятор (сложение двух чисел)
Попроси ввести два числа и выведи их сумму:"""

# Ответ:


def task_8():
    a = int(input("Enter your age: "))
    b = int(input("Enter your wife age: "))
    result = a + b

    print(
        f"Your age is {a}, your wife age is {b}, and tpgether will be {result}) ")


# Задание 9
"""Калькулятор площади прямоугольника
Спроси у пользователя ширину и высоту, 
выведи площадь:"""

# Ответ:


def task_9():
    weight = int(input("Enter the width: "))
    heoght = int(input("Enter the height: "))
    area = weight * heoght
    print(f"The area of the rectangle is {area}")


# Задание 10
"""Определи тип данных ввода
Попроси пользователя ввести значение и 
попробуй определить, это число или нет:"""

# Ответ:


def task_10():
    number = input("Enter a number: ")
    if number.isdigit():
        print("This is a number")
    else:
        print("This is not a number")


# Задание 11
"""Преобразователь температуры
Пусть пользователь введёт температуру в Цельсиях — 
выведи в Фаренгейтах:"""

# Ответ:


def task_11():
    celsius = float(input("Enter youtr temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit}")


# Задание 12
"""Задай 3 вопроса (можно любые). Подсчитай, 
сколько правильных ответов ввёл пользователь."""

# Ответ:


def task_12():
    question_1 = input("What is the capital of France? ")
    question_2 = input("What is 2 + 2? ")
    question_3 = input("What is the color of the sky? ")

    correct_answers = 0

    if question_1.lower() == "paris":
        correct_answers += 1
    if question_2 == "4":
        correct_answers += 1
    if question_3.lower() == "blue":
        correct_answers += 1

    print(f"You got {correct_answers} out of 3 questions right.")


# Задание 13
"""Попроси ввести возраст. 
Если возраст меньше 18 — напиши "Доступ запрещён", 
если больше или равно — "Добро пожаловать!":"""

# Ответ:


def task_13():
    age = int(input("Enter your age: "))
    if age < 18:
        print("Access denied")
    else:
        print("Welcome!")


# Задание 14
"""Пусть пользователь вводит сумму в долларах, 
а программа переводит её в рубли по курсу 
(например, 1 доллар = 0.92 рубли)."""

# Ответ:


def task_14():
    rubles = int(input("Enter the amount in rubles: "))
    dollars = rubles / 82
    euros = rubles / 85
    print(f"{rubles} rubles is equal to {dollars:.2f} dollars and {euros:.2f} euros")


# Задание
"""  Сравнить два списка с разным порядком"""


def task_15():
    fruits = [
        {
            'my_fruits': 'apple',
            'other_fruits': 777
        },
        {
            'my_fruits': 'banana',
            'other_fruits': 555
        }
    ]

    print(len(fruits))

    print(fruits[1]['my_fruits'])
# Задание


# Проверка пуша 05.09.25

# Test 2

# Отступ
# Отступ
# Отступ
# Отступ
# Отступ
# Отступ
# Отступ
# Отступ
# Отступ

# Это подсказал Чат GPT
# как лучше организовать код для выбора задания
tasks = {
    name.replace("task_", ""): func
    for name, func in globals().items()
    if callable(func) and name.startswith("task_")
}

# Выбор задания
choice = input("Enter the task number: ")

# Запуск
if choice in tasks:
    tasks[choice]()
else:
    print("Invalid task number.")
