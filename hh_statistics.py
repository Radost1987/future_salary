import requests
from itertools import count

from average_salary import predict_salary, predict_average_salary


def download_hh_vacancies(language):
    url = 'https://api.hh.ru/vacancies'
    vacancies_list = []
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
        vacancies_list.extend(page_data['items'])
        if page == page_data['pages'] - 1:
            break
    return number_founded_vacancies, vacancies_list
    number_founded_vacancies = page_data['found']


def predict_rub_salary_hh(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        return vacancy['salary']['from'], vacancy['salary']['to']


def collect_hh_statistics():
    languages = ['JavaScript', 'Go', 'Python', 'Java', 'PHP', 'C++', 'CSS', 'Ruby']
    language_statistics = {}
    for language in languages:
        hh_vacancies = download_hh_vacancies(language)[1]
        number_founded_vacancies = download_hh_vacancies(language)[0]
        salary_list = []
        for vacancy in hh_vacancies:
            if predict_rub_salary_hh(vacancy):
                salary_from = predict_rub_salary_hh(vacancy)[0]
                salary_to = predict_rub_salary_hh(vacancy)[1]
                salary = predict_salary(salary_from, salary_to)
                salary_list.append(salary)
        average_salary = predict_average_salary(salary_list)
        vac_processed = len(salary_list)
        language_statistics[language] = {
            'vacancies_found': number_founded_vacancies,
            'vacancies_processed': vac_processed,
            'average_salary': average_salary
        }
    return language_statistics


if __name__ == '__main__':
    print(collect_hh_statistics())
