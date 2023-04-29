def get_birthdays(data):
    """
    Функция для вывода информации о людях, чьи дни рождения приходятся на
    месяц, значение которого введено с клавиатуры
    """
    month = int(input('Введите месяц: '))

    birthdays = []
    for person in data:
        if person['birthdate'][1] == month:
            birthdays.append(person)

    if len(birthdays) == 0:
        print('Нет людей с таким днем рождения')
    else:
        print('Люди, у которых день рождения в выбранном месяце:')
        for person in birthdays:
            print(f"{person['surname']} {person['name']}: "
                  f"{person['birthdate'][0]}.{person['birthdate'][1]}.{person['birthdate'][2]}")
