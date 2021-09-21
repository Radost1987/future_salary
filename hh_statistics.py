import requests
from itertools import count

from salary_calculator import predict_salary, get_average_salary


def download_hh_vacancies(language):
    url = 'https://api.hh.ru/vacancies'
    moscow_id = 1
    founded_vacancies = []
    for page in count(0):
        payload = {
            'text': f'Программист {language}',
            'area': moscow_id,
            'period': 30,
            'page': page,
            'per_page': 100
        }
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        page_vacancies = page_response.json()
        founded_vacancies.extend(page_vacancies['items'])
        if page == page_vacancies['pages'] - 1:
            break
    founded_vacancies_number = page_vacancies['found']
    return founded_vacancies_number, founded_vacancies


def predict_rub_salary_hh(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
        salary = predict_salary(salary_from, salary_to)
        return salary


def collect_hh_statistics(languages):
    language_statistics = {}
    for language in languages:
        founded_vacancies_number, hh_vacancies = download_hh_vacancies(language)
        average_salary, vac_processed = get_average_salary(
            hh_vacancies,
            predict_rub_salary_hh
        )
        language_statistics[language] = {
            'vacancies_found': founded_vacancies_number,
            'vacancies_processed': vac_processed,
            'average_salary': average_salary
        }
    return language_statistics
