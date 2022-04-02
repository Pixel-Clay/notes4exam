from csv import reader
from json import dump

file_csv = 'csv_parser_listifizer.csv'  # путь к csv файлу
file_json = 'csv_parser_listifizer.json'  # путь к json файлу

with open(file_csv) as csvfile:
    days = {}
    # парсим csv таблицу
    csvreader = reader(csvfile, delimiter='^')
    for row in csvreader:
        # пропускаем строку-заголовок
        if row[0] == 'id':
            continue

        date = row[1]  # 1 столбик - столбик с датой, нумерация с 0
        if date not in days.keys():
            days[date] = []
        days[date].append(row[3])  # 3 столбик - столбик с предсказанием погоды, нумерация с 0
    # сортировка видов погоды
    days_sorted = {}
    for day in days.keys():
        # сортировка по обратному алфавитному порядку
        weather_sorted = days[day]
        weather_sorted.sort(reverse=True)
        days_sorted[day] = weather_sorted
    # запись в файл json
    with open(file_json, 'w') as jsonfile:
        dump(days_sorted, jsonfile)
