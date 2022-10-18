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


def get_statistic() -> dict:
    langs = ['python', 'Java', 'Javascript', 'PHP']
    statistic = {}
    for lang in langs:
        statistic[lang] = get_vacancies(text=lang)["found"]
    return statistic


def get_python_salary() -> list:
    vacancies = []
    for vacancy in get_vacancies('python').get('items'):
        if vacancy['salary'] is not None:
            vacancies.append(
                {'from': vacancy['salary'].get('from'),
                'to': vacancy['salary'].get('to'), 
                'currency': vacancy['salary'].get('currency'), 
                'gross': vacancy['salary'].get('gross')})
        else:
            vacancies.append(None)
    return vacancies


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_python_salary())
