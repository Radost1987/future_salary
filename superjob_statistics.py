import requests
from itertools import count

from salary_calculator import predict_salary, get_average_salary


def download_sj_vacancies(super_job_secret_key, language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': super_job_secret_key}
    moscow_id = 4
    founded_vacancies = []
    for page in count(0):
        payload = {
            'town': moscow_id,
            'keyword': f'Программист {language}',
            'page': page,
            'count': 100
        }
        page_response = requests.get(url, headers=headers, params=payload)
        page_response.raise_for_status()
        page_vacancies = page_response.json()
        founded_vacancies.extend(page_vacancies['objects'])
        if not page_vacancies['more']:
            break
    founded_vacancies_number = page_vacancies['total']
    return founded_vacancies_number, founded_vacancies


def predict_rub_salary_superjob(vacancy):
    if vacancy['currency'] == 'rub':
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        salary = predict_salary(salary_from, salary_to)
        return salary


def collect_sj_statistics(super_job_secret_key, languages):
    language_statistics = {}
    for language in languages:
        founded_vacancies_number, sj_vacancies = download_sj_vacancies(
            super_job_secret_key,
            language
        )
        average_salary, vac_processed = get_average_salary(
            sj_vacancies,
            predict_rub_salary_superjob
        )
        language_statistics[language] = {
            'vacancies_found': founded_vacancies_number,
            'vacancies_processed': vac_processed,
            'average_salary': average_salary
        }
    return language_statistics
