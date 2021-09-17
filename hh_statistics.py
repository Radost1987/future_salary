import requests
from itertools import count

from average_salary import predict_salary, predict_average_salary


def download_hh_vacancies(language):
    url = 'https://api.hh.ru/vacancies'
    founded_vacancies = []
    for page in count(0):
        payload = {
            'text': f'Программист {language}',
            'area': '1',
            'period': 30,
            'page': page,
            'per_page': 100
        }
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        page_data = page_response.json()
        founded_vacancies.extend(page_data['items'])
        if page == page_data['pages'] - 1:
            break
    number_founded_vacancies = page_data['found']
    return number_founded_vacancies, founded_vacancies


def predict_rub_salary_hh(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
        salary = predict_salary(salary_from, salary_to)
        return salary


def get_average_salary(vacancies):
    salary_list = []
    for vacancy in vacancies:
        salary = predict_rub_salary_hh(vacancy)
        if salary:
            salary_list.append(salary)
    if salary_list:
        average_salary = int(numpy.average(salary_list))
    else:
        average_salary = 0
    vac_processed = len(salary_list)
    return average_salary, vac_processed


def collect_hh_statistics(languages):
    language_statistics = {}
    for language in languages:
        number_founded_vacancies, hh_vacancies = download_hh_vacancies(language)
        average_salary, vac_processed = get_average_salary(hh_vacancies)
        language_statistics[language] = {
            'vacancies_found': number_founded_vacancies,
            'vacancies_processed': vac_processed,
            'average_salary': average_salary
        }
    return language_statistics


if __name__ == '__main__':
    print(collect_hh_statistics())
