import requests
import os

from dotenv import load_dotenv


def get_vacancies(text: str) -> list:
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': os.getenv('API_SUPERJOB')}
    payload = {
        't': '4',
        'keyword': text,
        }
    response = requests.get(
        url, 
        params=payload, 
        headers=headers
        )
    response.raise_for_status()
    return response.json()


def predict_rub_salary_for_superJob(vacancy: dict) -> float:
    if vacancy['currency'] == 'rub':
        payment_floor = vacancy.get('payment_from')
        payment_top = vacancy.get('payment_to')
        if payment_floor and payment_top:
            return (payment_top - payment_floor) / 2
        elif not payment_top and payment_floor:
            return payment_floor * 1.2
        elif payment_top and not payment_floor:
            return payment_top * 0.8
    return None 


def get_statistic() -> dict:
    langs = ['python', 'Java', 'Javascript', 'PHP']
    statistic = {}
    for lang in langs:
        vacancies = get_vacancies(text=lang)
        total = 0
        vacancies_processed = 0
        for vacancy in vacancies.get("objects"):
            salary = predict_rub_salary_for_superJob(vacancy) 
            if salary is not None:
                total += salary
                vacancies_processed += 1
        statistic[lang] = { 
            "vacancies_found": vacancies["total"],
            "vacancies_processed": vacancies_processed,
            "average_salary": total // vacancies_processed
        }
    return statistic


if __name__ == '__main__':
    from pprint import pprint
    load_dotenv()
    # vacancies = get_vacancies('python')
    # for vacancy in vacancies.get("objects"):
        # pprint(vacancy.get("profession"), 'От', vacancy.get("payment_from"), 'До', vacancy.get("payment_to"))
        # pprint(predict_rub_salary_for_superJob(vacancy))
    pprint(get_statistic())
    # pprint(get_vacancies('aburvalg', 26))
