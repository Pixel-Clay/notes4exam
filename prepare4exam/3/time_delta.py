# Функция принимает на вход словарь с локальными данными и словарь с данными на сервере
# Нужно дописать логику скачивания данных с сервера и прикрутить именованные аргументы
# local_data - данные из именованных аргументов, remote_data - данные на сервере
def prize(local_data, remote_data):
    timetable = {}

    for local in local_data.keys():
        for glob in remote_data.keys():
            if local == glob:
                local_date = local_data[local].split('.')
                remote_date = remote_data[glob].split('.')
                if local_date != remote_date and local_date[1] == remote_date[1]:
                    d1 = int(local_date[0])
                    d2 = int(remote_date[0])
                    delta = d1 - d2
                    if delta <= 31:
                        timetable[local] = delta
                        break
    return timetable


local_data = {
    'Carnatic': "25.07",
    'Magnoila': "08.08",
    'Mongolia': "09.08",
    'Beth': "26.07"
}

remote_data = {
    'Carnatic': "27.07",
    'Magnoila': "08.08",
    'Mongolia': "01.08",
    'Beth': "25.07",
    'Bay': "19.01"
}

print(prize(local_data, remote_data))
