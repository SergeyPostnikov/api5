import requests
from collections import defaultdict
from service_functions import predict_salary


def get_vacancies(text: str) -> list[dict]:
    url = "https://api.hh.ru/vacancies/"
    page = 0
    pages = defaultdict(list)
    programming_development = 1.221
    moscow_city_id = 1
    days = 30
    payload = {
        "specialization": programming_development,
        "area": moscow_city_id,
        "period": days,
        "text": text,
        "per_page": 100, 
        "page": page
    }
    pages_number = 1
    while page < pages_number:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        vacancies = response.json()
        pages['items'] += vacancies['items']
        pages['found'] = vacancies['found']
        pages_number = vacancies['pages']
        payload['page'] = page
        page += 1
    return pages


def predict_rub_salary(vacancy: dict) -> float:
    salary = vacancy.get('salary')
    if not salary or salary['currency'] != 'RUR':
        return None
    payment_floor = salary.get('from')
    payment_top = vacancy.get('to')
    return predict_salary(payment_floor=payment_floor, payment_top=payment_top)


def get_statistic() -> dict:
    langs = ['python', 'Java', 'Javascript', 'PHP']
    statistic = {}
    for lang in langs:
        vacancies = get_vacancies(text=lang)
        total = 0
        vacancies_processed = 0
        for vacancy in vacancies.get('items'):
            salary = predict_rub_salary(vacancy) 
            if salary:
                total += salary
                vacancies_processed += 1
        statistic[lang] = { 
            "vacancies_found": vacancies.get('found'),
            "vacancies_processed": vacancies_processed,
        }
        if vacancies_processed:
            statistic[lang]["average_salary"] = int(total // vacancies_processed)
    return statistic
