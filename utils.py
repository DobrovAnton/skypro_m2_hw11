"""
Модуль 2. Домашнее задание №11
Приложение на Flask.
"""

import json

# База данных кандидатов.
__candidates_data = []


def load_candidates_from_json(path):
    """
    Загружает базу данных по кандидатам из json файла
    и преобразует в словарь.
    :param path:
    :return: обработанная база данных кандидатов.
    """
    global __candidates_data
    with open(path, 'r', encoding='utf-8') as file:
        __candidates_data = json.load(file)
        return __candidates_data


def get_candidate(candidate_id):
    """
    Загружает данные о кандидате по указанному id.
    :param candidate_id: id, по которому необходимо осуществить поиск.
    :return: данные о кандидате.
    """
    for candidate in __candidates_data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'Кандидат не найден'}


def get_candidates_by_name(candidate_name):
    """
    Загружает данные о кандидатах по указанному имени.
    :param candidate_name: имя, по которому необходимо осуществить поиск.
    :return: имя (имена) кандидата, совпадающие с запросом.
    """
    return [candidate for candidate in __candidates_data if
            candidate_name.strip().lower() in candidate['name'].strip().lower()]


def get_candidates_by_skill(skill_name):
    """
    Загружает данные о кандидатах по запрашиваемому навыку.
    :param skill_name: навык, по которому необходимо осуществить поиск.
    :return: имя (имена) кандидата с соответствующим навыком.
    """
    candidates = []
    for candidate in __candidates_data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
