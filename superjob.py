import requests
import os

from dotenv import load_dotenv


def get_vacancies(keyword: str, page: int) -> list:
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': os.getenv('API_SUPERJOB')}
    payload = {
        't': '4',
        'keyword': 'python',
        'page': page}
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("objects")


def predict_rub_vacancy_for_superJob(vacancy: dict) -> float:
    if vacancy['currency'] == 'rub':
        payment_floor = vacancy.get('payment_from')
        payment_top = vacancy.get('payment_to')
        if payment_floor and payment_top:
            return f"{(payment_top - payment_floor) / 2=}"
        elif not payment_top and payment_floor:
            return f"{payment_floor * 1.2=}"
        elif payment_top and not payment_floor:
            return f"{payment_top * 0.8=}"
    return None 


if __name__ == '__main__':
    from pprint import pprint
    load_dotenv()
    vacancies = get_vacancies('python', 1)
    for vacancy in vacancies:
        # pprint(vacancy.get("profession"), 'От', vacancy.get("payment_from"), 'До', vacancy.get("payment_to"))
        pprint(predict_rub_vacancy_for_superJob(vacancy))
