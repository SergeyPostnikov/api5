import requests
from collections import defaultdict
from service_functions import predict_salary


def get_vacancies(text: str, api_key: str) -> defaultdict:
    url = 'https://api.superjob.ru/2.0/vacancies/'
    moscow_city_id = '4'
    page = 0
    next_page_exists = True
    vacancies = defaultdict(list)
    vacancies["total"] = 0
    headers = {'X-Api-App-Id': api_key}
    payload = {
        't':  moscow_city_id,
        'keyword': text,
        'count': 100,
        'page': page
        }

    while next_page_exists:
        response = requests.get(
            url, 
            params=payload, 
            headers=headers
            )
        response.raise_for_status()
        vacancies["objects"] += response.json().get("objects")
        vacancies["total"] = int(response.json().get("total"))
        next_page_exists = response.json().get("more")
        payload['page'] += 1
    return vacancies


def predict_rub_salary_for_superJob(vacancy: dict) -> float:
    payment_floor = vacancy.get('payment_from')
    payment_top = vacancy.get('payment_to')
    if vacancy['currency'] != 'rub':
        return None 
    return predict_salary(payment_floor=payment_floor, payment_top=payment_top)


def get_statistic(api_key: str) -> dict:
    langs = ['python', 'Java', 'Javascript', 'PHP']
    statistic = {}
    for lang in langs:
        vacancies = get_vacancies(text=lang, api_key=api_key)
        total = 0
        vacancies_processed = 0
        for vacancy in vacancies.get("objects"):
            salary = predict_rub_salary_for_superJob(vacancy) 
            if salary:
                total += salary
                vacancies_processed += 1
        statistic[lang] = { 
            "vacancies_found": vacancies["total"],
            "vacancies_processed": vacancies_processed,
        }
        if vacancies_processed:
            statistic[lang]["average_salary"] = int(total // vacancies_processed)
    return statistic
