import requests
from itertools import count

from salary import predict_salary, get_average_salary


def download_sj_vacancies(super_job_secret_key, language):
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
    number_vacancies = page_vacancies['total']
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
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        salary = predict_salary(salary_from, salary_to)
        return salary


def collect_sj_statistics(super_job_secret_key, languages):
    language_statistics = {}
    for language in languages:
        number_founded_vacancies, sj_vacancies = download_sj_vacancies(
            super_job_secret_key,
            language
        )
        average_salary, vac_processed = get_average_salary(
            sj_vacancies,
            predict_rub_salary_superjob
        )
        language_statistics[language] = {
            'vacancies_found': number_founded_vacancies,
            'vacancies_processed': vac_processed,
            'average_salary': average_salary
        }
    return language_statistics
