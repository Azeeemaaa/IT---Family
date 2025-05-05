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
"""Задание 3: Строки и числа
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


choice = input("Enter the task number : ")

if choice == '1':
    task_1()
elif choice == '2':
    task_2()
elif choice == '3':
    task_3()
elif choice == '4':
    task_4()
elif choice == '5':
    task_5()
elif choice == '6':
    task_6()
elif choice == '7':
    task_7()
else:
    print("Invalid choice")
