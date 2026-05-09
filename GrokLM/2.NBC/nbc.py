import pandas
import os
import numpy as np
from openpyxl import load_workbook
from collections import Counter

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

    return item


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


def get_priori_P(sorted_ds):  #
    priori_P = {}
    classes_count = len(sorted_ds)  # 2
    for obj in sorted_ds:
        priori_P[obj[1]["Class"]] = 1 / classes_count
    return priori_P

    # print(
    #     f"Апприорная вероятность класса C{find_classes(in_data).index(obj) + 1}:",
    #     len(obj) / total_len,
    # )


def calc_cond_P(X, in_data):
    # X = {'ID': None, 'x1': 'Мультикам', 'x2': 'АК-74', 'x3': 'Бег', 'Class': '?'}
    # in_data = [1[4{5}], 2[4{5}]]
    cond_P_list = []
    cond_P_dict = {}
    for c in in_data:  # c - список объектов класса
        dict = []
        duples = {}

        for obj in c:  # obj - объект класса с
            for x in X:  # p - параметр объекта Х
                for p in obj:  # p - параметр объекта класса с
                    if X.get(x) == obj.get(
                        p
                    ):  # сравненение параметра объекта Х и параметра объекта класса
                        dict.append(X.get(x))
        for el in dict:
            if duples.get(el):
                duples[el] += 1
            else:
                duples[el] = 1

        for d in duples:
            duples[d] /= len(c)
        cond_P_list.append(duples)

        for cp in cond_P_list:
            cond_P_dict[c[1]["Class"]] = cp

    # print(cond_P_dict)
    return cond_P_dict


def calc_Bayes_P(priori_P_list, cond_P_dict):
    #  priori_P_list = {'Свой': 0.5, 'Враг': 0.5}
    #  cond_P_dict = {'Свой': {'АК-74': 0.75, 'Бег': 0.25, 'Мультикам': 0.25}, 'Враг': {'Мультикам': 0.5, 'Бег': 0.5, 'АК-74': 0.25}}
    bayes_P_list = {}
    for c in priori_P_list:  # {'Свой': 0.5, 'Враг': 0.5}
        bayes_P = 1 * priori_P_list[c]
        print(c)
        # print(priori_P_list[c])
        # print(cond_P_dict[c])
        for b in cond_P_dict[c]:
            bayes_P *= cond_P_dict[c][b]
        print(bayes_P)
    # return None


dataset = xl_2_list(file_path)
obj_x = get_X(file_path)
sorted_ds = find_classes(dataset)
priori_P = get_priori_P(sorted_ds)
cond_P = calc_cond_P(obj_x, sorted_ds)
# print("\nАПРИОРНЫЕ ВЕРОЯТНОСТИ:\n\t", priori_P)
# print("\nУСЛОВНЫЕ ВЕРОЯТНОСТИ:\n\t", cond_P)

calc_Bayes_P(priori_P, cond_P)
