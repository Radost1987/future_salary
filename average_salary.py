import numpy


def predict_salary(salary_from, salary_to):
    if salary_to is None:
        salary = salary_from * 1.2
    elif salary_from is None:
        salary = salary_to * 0.8
    else:
        salary = (salary_from + salary_to) / 2
    return salary


def predict_average_salary(salary_list):
    avg_salary = int(numpy.average(salary_list))
    return avg_salary
