def predict_salary(salary_from, salary_to):
    if not salary_to:
        salary = salary_from * 1.2
    elif not salary_from:
        salary = salary_to * 0.8
    else:
        salary = (salary_from + salary_to) / 2
    return salary
