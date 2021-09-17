from terminaltables import AsciiTable

from superjob_statistics import collect_sj_statistics
from hh_statistics import collect_hh_statistics


def get_statistics_table(vacancies_statistics, site_name):
    title = site_name
    table_data = [[
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]]
    for language, value in vacancies_statistics.items():
        table_data.append([language, f"{value['vacancies_found']}",
                       f"{value['vacancies_processed']}",
                       f"{value['average_salary']}"])
    table = AsciiTable(table_data, title)
    return table


def main():
    super_job_vacancies_statistics = collect_sj_statistics()
    head_hunter_vacancies_statistics = collect_hh_statistics()
    get_statistics_table(super_job_vacancies_statistics, 'SuperJob Moscow')
    get_statistics_table(head_hunter_vacancies_statistics, 'HeadHunter Moscow')

    print(superjob_table.table)
    print(headhuter_table.table)

if __name__ == '__main__':
    main()
