from terminaltables import AsciiTable


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


def predict_salary(payment_floor: int, payment_top: int) -> int | None:
    if not payment_floor and not payment_top:
        return None
    elif not payment_floor:
        return int(payment_top * 0.8)
    elif not payment_top:
        return int(payment_floor * 1.2)

    return (payment_top + payment_floor) // 2
