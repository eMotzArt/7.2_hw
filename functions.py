import json

def json_file_to_mem(file_name: str) -> list:
    '''Декодирует json файл в переменную-словарь

    Принимает аргументом строку с названием файла, открывает,
    декодирует файл с помощью json.load, сохраняет результат словарём в переменную content
    возращает словарь content
    :param file_name: имя файла (str)
    :return: content (list)
    '''
    with open(file_name) as file:
        content = json.load(file)
    return content

def get_student_by_pk(list_: list, pk: int) -> dict | bool:
    '''Ищет студента в списке-словарей по личному номеру

    Принимает аргументами список-словарей с данными студентов (list_) и личный номер для поиска (pk),
    перебирает его, выискивая совпадение личного номера для поиска (pk) и содержащийся в словаре закрепленный номер,
    после найденного совпадения возвращает соответствующий словарь из списка
    В случае ненахождения возвращает False
    :param list_: список словарей студентов (list)
    :param pk: номер для поиска (int)
    :return: item (dict) словарь с данным о студенте
    :return: False в случае отсутствия подходящего словаря
    '''
    for item in list_:
        if item['pk'] == pk:
            return item
    return False

def student_info(student: dict) -> tuple:
    '''Формирует три строки для вывода информации о студенте

    Принимает аргументом словарь с данным о студенте, на основе которых формирует три строки:
    строка о имени, строка о имеющихся навыках, строка о изучаемых навыках,
    возвращает три строки кортежем
    :param student: словарь с данными о студенте (dict)
    :return: кортеж из трех строк (tuple)
    '''
    name_info = f"Студент {student['full_name']}"
    skills_info = f"Знает: {(', '.join(student['skills'])).rstrip()}"
    learns_info = f"Хочет изучить: {(', '.join(student['learns'])).rstrip()}"

    return name_info, skills_info, learns_info

def get_profession_by_title(list_:list, title: str) -> dict | bool:
    '''Ищет словарь с данными о профессии по названию професии в списке-словарей профессий

    Принимает аргументами список словарей профессий (list_) и название професии для поиска (title),
    ищет в списке подходящий словарь, при нахождении возвращает найденный словарь
    В случае ненахождения возвращает False
    :param list_: список словарей с профессиями (list)
    :param title: название профессии для поиска (str)
    :return: словарь с данными о профессии (dict)
    :return: False в случае отсутствия подходящего словаря
    '''

    for item in list_:
        if item['title'] == title:
            return item
    return False

def check_fitness(student: dict, profession: dict) -> dict:
    '''Проверяет "пригодность" навыков студента по отношению к требуемым навыкам для профессии

    Принимает аргументами словарь с данными о студенте (student) и описание профессии с требованиями к студенту (profession),
    уникализирует имеющиеся навыки и требуемые навыки в два множества, сравнивает множества, вычисляет % пригодности,
    возвращает словарь с подходящими навыками (has), с отсутствующими, но требуемыми навыками (lacks), % пригодности (fit_percent)
    :param student:
    :param profession:
    :return:
    '''
    student_skills = set(student['skills'])
    prof_skills = set(profession['skills'])
    check_result = {
        "has": list(student_skills.intersection(prof_skills)),
        "lacks": list(prof_skills.difference(student_skills)),
        "fit_percent": round(100 / len(prof_skills) * len(student_skills.intersection(prof_skills)))
    }

    return check_result