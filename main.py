import os

import numpy
from dotenv import load_dotenv
from terminaltables import AsciiTable

from superjob_statistics import collect_sj_statistics
from hh_statistics import collect_hh_statistics


def get_statistics_table(vacancies_statistics, title):
    table_data = [[
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]]
    for language, value in vacancies_statistics.items():
        table_data.append([
            language,
            f"{value['vacancies_found']}",
            f"{value['vacancies_processed']}",
            f"{value['average_salary']}"
        ])
    table = AsciiTable(table_data, title)
    return table


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPER_JOB_SECRET_KEY')
    languages = ['JavaScript', 'Go', 'Python', 'Java', 'PHP', 'C++', 'CSS', 'Ruby']
    superjob_vacancies_statistics = collect_sj_statistics(
        superjob_secret_key,
        languages
        )
    headhunter_vacancies_statistics = collect_hh_statistics(languages)
    superjob_table = get_statistics_table(
        superjob_vacancies_statistics,
        'SuperJob Moscow'
    )
    headhuter_table = get_statistics_table(
        headhunter_vacancies_statistics,
        'HeadHunter Moscow'
    )
    print(superjob_table.table)
    print(headhuter_table.table)

if __name__ == '__main__':
    main()
