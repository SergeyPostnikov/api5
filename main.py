from terminaltables import AsciiTable
from dotenv import load_dotenv
from hh import get_statistic as get_hh_statistic  
from sj import get_statistic as get_sj_statistic


def get_table(title: str, statistic: dict) -> AsciiTable.table:
    table_data = [
        [
            'Язык программирования', 
            'Вакансий найдено', 
            'Вакансий обработано',  
            'Средняя зарплата'
        ]
    ]
    for lang in statistic:
        table_data.append([
            f'{lang}', 
            f'{statistic[lang]["vacancies_found"]}',
            f'{statistic[lang]["vacancies_processed"]}',
            f'{statistic[lang]["average_salary"]}'
            ])

    table = AsciiTable(table_data, title)
    return table.table


if __name__ == '__main__':
    load_dotenv()
    print(get_table('SuperJob', statistic=get_sj_statistic()))
    print(get_table('HeadHunter', statistic=get_hh_statistic()))
