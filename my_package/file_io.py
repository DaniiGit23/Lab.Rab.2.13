def input_data():
    """
    Функция для ввода данных в список из словарей заданной структуры
    """
    data = []
    while True:
        person = {}

        person['surname'] = input('Введите фамилию: ')
        person['name'] = input('Введите имя: ')
        person['phone_number'] = input('Введите номер телефона: ')

        birthdate = input('Введите дату рождения через пробел (день месяц год): ')
        birthdate = birthdate.split()
        birthdate = [int(i) for i in birthdate]
        person['birthdate'] = birthdate

        data.append(person)

        add_more = input('Хотите добавить еще одного человека? (да/нет) ')
        if add_more.lower() == 'нет':
            break

    # Сортировка по фамилии и имени
    data = sorted(data, key=lambda x: (x['surname'], x['name']))

    return data