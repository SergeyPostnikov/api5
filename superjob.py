import requests
import os

from dotenv import load_dotenv


def get_vacancies() -> list:
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': os.getenv('API_SUPERJOB')}
    payload = {
        't': '4',
        'keyword': 'python'}
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("objects")


def predict_rub_salary(vacancy: dict) -> float: #fixit
    salary = vacancy['salary']
    if salary is not None and salary['currency'] == 'RUR':
        if salary.get('payment_from') and salary.get('payment_to'):
            return (salary.get('payment_to') - salary.get('payment_from')) / 2
        elif not salary.get('payment_to'):
            return salary.get('payment_from') * 1.2
        elif salary.get('payment_from') is None:
            return salary.get('payment_to') * 0.8
    return None
 

def predict_rub_salary_for_superJob(vacancy):
    pass


if __name__ == '__main__':
    from pprint import pprint
    load_dotenv()
    vacancies = get_vacancies()
    for vacancy in vacancies:
        print(vacancy.get("profession"), vacancy.get("payment_from"))
