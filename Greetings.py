from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.now().date()

    # Знаходимо перше понеділок після поточної дати
    start_date = current_date + timedelta(days=(0 - current_date.weekday()) % 7)

    # Знаходимо кінцеву дату, яка є першим понеділком після тижня
    end_date = start_date + timedelta(days=7)

    # Створюємо словник, де ключами є дні тижня, а значеннями - списки імен користувачів
    birthdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Проходимо по кожному користувачу і додаємо його до відповідного дня тижня в словнику birthdays
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Перевіряємо, чи день народження користувача потрапляє в діапазон тижня
        if start_date <= birthday < end_date:
            # Визначаємо день тижня дня народження
            weekday = birthday.strftime("%A")

            # Додаємо ім'я користувача до відповідного дня тижня
            if weekday == "Saturday" or weekday == "Sunday":
                # Якщо день народження на вихідних, додаємо в понеділок
                birthdays["Monday"].append(name)
            else:
                birthdays[weekday].append(name)

    # Виводимо список користувачів по днях тижня
    for weekday, names in birthdays.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

# Старий код
users = [
    {"name": "John", "birthday": datetime(1990, 3, 15)},
    {"name": "Emily", "birthday": datetime(1992, 5, 20)},
    {"name": "David", "birthday": datetime(1985, 7, 10)},
    {"name": "Sarah", "birthday": datetime(1995, 9, 8)},
    {"name": "Michael", "birthday": datetime(1988, 11, 25)},
    {"name": "Jessica", "birthday": datetime(1993, 2, 12)},
    {"name": "Daniel", "birthday": datetime(1987, 4, 30)},
    {"name": "Laura", "birthday": datetime(1991, 6, 5)},
    {"name": "Alex", "birthday": datetime(1994, 8, 18)},
    {"name": "Olivia", "birthday": datetime(1996, 10, 2)},
    {"name": "Jacob", "birthday": datetime(1989, 12, 20)},
    {"name": "Sophia", "birthday": datetime(1997, 1, 8)},
    {"name": "William", "birthday": datetime(1998, 3, 17)},
    {"name": "Ava", "birthday": datetime(1986, 5, 23)},
    {"name": "James", "birthday": datetime(1999, 7, 11)},
    {"name": "Mia", "birthday": datetime(1992, 9, 28)},
    {"name": "Benjamin", "birthday": datetime(1993, 11, 5)},
    {"name": "Charlotte", "birthday": datetime(1987, 1, 15)},
    {"name": "Daniel", "birthday": datetime(1994, 3, 22)},
    {"name": "Harper", "birthday": datetime(1996, 5, 2)}
]

get_birthdays_per_week(users)
