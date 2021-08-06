# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def person_info(**kwargs):
    print(f'{kwargs.get("name")} {kwargs.get("surname")} из города {kwargs.get("address")}. '
          f'Телефон: {kwargs.get("phone")}, e-mail: {kwargs.get("email")}.')


person_info(surname='Timofeev', name='Nil', e_mail='timofeevnil@mail.ru',
            phone='9037860883', address='Moscow')
