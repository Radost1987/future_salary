import numpy


def predict_salary(salary_from, salary_to):
    if not salary_from and not salary_to:
        return None
    if not salary_to:
        salary = salary_from * 1.2
    elif not salary_from:
        salary = salary_to * 0.8
    else:
        salary = (salary_from + salary_to) / 2
    return salary


def get_average_salary(vacancies, rub_salary):
    salaries = []
    for vacancy in vacancies:
        salary = rub_salary(vacancy)
        if salary:
            salaries.append(salary)
    if salaries:
        average_salary = int(numpy.average(salaries))
    else:
        average_salary = 0
    vac_processed = len(salaries)
    return average_salary, vac_processed
