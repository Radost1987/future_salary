import os

import requests
from dotenv import load_dotenv
from itertools import count

from average_salary import predict_salary, predict_average_salary


def download_sj_vacancies(language):
    load_dotenv()
    super_job_secret_key = os.getenv('SUPER_JOB_SECRET_KEY')
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': super_job_secret_key}
    vacancies_list = []
    for page in count(0):
        payload = {
            'town': '4',
            'keyword': f'Программист {language}',
            'page': page,
            'count': 100
        }
        page_response = requests.get(url, headers=headers, params=payload)
        page_response.raise_for_status()
        page_vacancies = page_response.json()
        vacancies_list.extend(page_vacancies['objects'])
        if not page_vacancies['more']:
            break
    return number_vacancies, vacancies_list


def predict_rub_salary_superjob(vacancy):
    if vacancy['currency'] == 'rub':
        if not vacancy['payment_from'] and not vacancy['payment_to']:
            pass
        else:
            salary_from = vacancy['payment_from']
            salary_to = vacancy['payment_to']
            salary = predict_salary(salary_from, salary_to)
            return vacancy['payment_from'], vacancy['payment_to']


def collect_sj_statistics():
    languages = ['JavaScript', 'Go', 'Python', 'Java', 'PHP', 'C++', 'CSS', 'Ruby']
def get_average_salary(vacancies):
    salary_list = []
    for vacancy in vacancies:
        salary = predict_rub_salary_superjob(vacancy)
        if salary:
            salary_list.append(salary)
    if salary_list:
        average_salary = int(numpy.average(salary_list))
    else:
        average_salary = 0
    vac_processed = len(salary_list)
    return average_salary, vac_processed


def collect_sj_statistics(super_job_secret_key, languages):
    language_statistics = {}
    for language in languages:
        number_founded_vacancies, sj_vacancies = download_sj_vacancies(
            super_job_secret_key,
            language
        )
        average_salary, vac_processed = get_average_salary(sj_vacancies)
        language_statistics[language] = {
            'vacancies_found': number_founded_vacancies,
            'vacancies_processed': vac_processed,
            'average_salary': average_salary
        }
    return language_statistics


if __name__ == '__main__':
    print(collect_sj_statistics())
