import pandas
import os
import numpy as np
from openpyxl import load_workbook

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset.xlsx")
is_reading = False  # Флаг "читаемости", который включается после начала таблицы


def xl_2_list(file):
    data = []  # Пустой список, для сохранения извлеченных из файла данные
    workbook = load_workbook(file)
    page = workbook.active
    for row in page.iter_rows(values_only=True):
        if isinstance(row[0], int):

            item = {
                "ID": row[0],
                "x1": row[1],
                "x2": row[2],
                "x3": row[3],
                "Class": row[4],
            }  # {'ID': 1, 'x1': 'Цифра', 'x2': 'АК-74', 'x3': 'Патруль', 'Class': 'Свой'}
            data.append(item)
    return data


def get_X(file):
    data = []  # Пустой список, для сохранения извлеченных из файла данные
    workbook = load_workbook(file)
    page = workbook.active
    for row in page.iter_rows(values_only=True):
        if (row[0] == None) & (
            row[4] == "?"
        ):  # находим объект Х по пустому ID и символу ? в поле Класса
            item = {
                "ID": row[0],
                "x1": row[1],
                "x2": row[2],
                "x3": row[3],
                "Class": row[4],
            }  # {'ID': None, 'x1': 'Мультикам', 'x2': 'АК-74', 'x3': 'Бег', 'Class': '?'}
            data.append(item)

    return data


def find_classes(list):
    c_n_names = []  # the list of classes' names
    for obj in list:  # obj - словарь объекта
        if obj["Class"] not in c_n_names:  # если Свой/Враг нет в классе
            c_n_names.append(obj["Class"])  # то добавляем его в список
        else:
            continue

    # ПОЛУЧАЕМ СПИСОК СПИСКОВ ОБЪЕКТОВ ПО КЛАССАМ
    c_n_list = []  # Список объектов класса С
    for c in c_n_names:  # с - Класс (Свой/Враг)
        classes = []  # список названий классов

        for ob in list:  # ob - словарь объекта
            if (
                ob["Class"] == c
            ):  # Если значение класса из списка соответсвует текущему значнеию в словаре классов
                classes.append(ob)  # добавляем его в список
            c_n_list.append(classes)
    return c_n_list


def calc_priori_P(in_data):
    total_len = len(in_data)
    for obj in find_classes(in_data):
        print(
            f"Апприорная вероятность класса C{find_classes(in_data).index(obj) + 1}:",
            len(obj) / total_len,
        )

def calc_cond_P(X,in_data):
    # X = {'ID': None, 'x1': 'Мультикам', 'x2': 'АК-74', 'x3': 'Бег', 'Class': '?'}
    # in_data = [1[8{5}], 2[8{5}]]
    dict = {}
    for x in X: # p - параметр объекта Х
        count = 0
        for c in in_data: # c - список объектов класса 
            for obj in c: # obj - объект класса с
                for p in obj: # p - параметр объекта класса с
                    if x == p: # сравненение параметра объекта Х и параметра объекта класса 
                        count += 1
                        dict[x] = count
        print(dict)
                        



dataset = xl_2_list(file_path)
obj_x = get_X(file_path)
sorted_ds = find_classes(dataset)
# calc_priori_P(dataset)
calc_cond_P(obj_x, sorted_ds)


# [{'ID': 1, 'x1': 'Цифра', 'x2': 'АК-74', 'x3': 'Патруль', 'Class': 'Свой'}
#  {'ID': 2, 'x1': 'Цифра', 'x2': 'АК-74', 'x3': 'Бег',     'Class': 'Свой'}
# ...]

# print(xl_2_list(file_path))
