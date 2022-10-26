from terminaltables import AsciiTable
from dotenv import load_dotenv
from hh import get_statistic as get_hh_statistic  
from sj import get_statistic as get_sj_statistic

import os


def get_table(title: str, statistic: dict) -> AsciiTable.table:
    summary_table = [
        [
            'Язык программирования', 
            'Вакансий найдено', 
            'Вакансий обработано',  
            'Средняя зарплата'
        ]
    ]
    for lang in statistic:
        summary_table.append([
            f'{lang}', 
            f'{statistic[lang]["vacancies_found"]}',
            f'{statistic[lang]["vacancies_processed"]}',
            f'{statistic[lang]["average_salary"]}'
            ])

    table = AsciiTable(summary_table, title)
    return table.table


if __name__ == '__main__':
    load_dotenv()
    sj_statistic = get_sj_statistic(api_key=os.getenv('API_SUPERJOB'))
    hh_statistic = get_hh_statistic()
    print(get_table('SuperJob', statistic=sj_statistic))
    # print(get_table('HeadHunter', statistic=hh_statistic))
