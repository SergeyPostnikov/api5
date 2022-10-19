import requests
import os

from dotenv import load_dotenv


def get_vacancies():
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': os.getenv('API_SUPERJOB')
        }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    from pprint import pprint
    load_dotenv()
    vacancies = get_vacancies()["objects"]
    for vacancy in vacancies:
        pprint(vacancy.get("profession"))