import requests


def get_vacancies(text: str) -> dict:
    url = "https://api.hh.ru/vacancies/"
    payload = {
        "specialization": 1.221,
        "area": 1,
        "period": 30,
        "text": text
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def predict_rub_salary(vacancy: dict) -> float:
    salary = vacancy['salary']
    if salary is not None and salary['currency'] == 'RUR':
        if salary.get('from') and salary.get('to'):
            return (salary.get('to') - salary.get('from')) / 2
        elif salary.get('to') is None:
            return salary.get('from') * 1.2
        elif salary.get('from') is None:
            return salary.get('to') * 0.8
    return None


def get_statistic() -> dict:
    langs = ['python', 'Java', 'Javascript', 'PHP']
    statistic = {}
    for lang in langs:
        vacancies = get_vacancies(text=lang)
        total = 0
        vacancies_processed = 0
        for vacancy in vacancies.get('items'):
            salary = predict_rub_salary(vacancy) 
            if salary is not None:
                total += salary
                vacancies_processed += 1
        statistic[lang] = {
            "vacancies_found": vacancies["found"],
            "vacancies_processed": vacancies_processed,
            "average_salary": total // vacancies_processed
        }
    return statistic


def get_python_salary() -> list:
    vacancies = []
    for vacancy in get_vacancies('python').get('items'):
        if vacancy['salary'] is not None:
            vacancies.append({
                'from': vacancy['salary'].get('from'),
                'to': vacancy['salary'].get('to'), 
                'currency': vacancy['salary'].get('currency'), 
                'gross': vacancy['salary'].get('gross')})
        else:
            vacancies.append(None)
    return vacancies


if __name__ == '__main__':
    from pprint import pprint
    # pprint(get_python_salary())
    # for vacancy in get_vacancies('python').get('items'):
    #     print(predict_rub_salary(vacancy))
    pprint(get_statistic())
