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


# [{'ID': 1, 'x1': 'Цифра', 'x2': 'АК-74', 'x3': 'Патруль', 'Class': 'Свой'}
#  {'ID': 2, 'x1': 'Цифра', 'x2': 'АК-74', 'x3': 'Бег',     'Class': 'Свой'}
# ...]


def find_elem(in_data):
    lit = []
    for i in in_data:  #  i - словарь
        for el in i.values():  # el - входящее слово, i.values() - список значений
            if el in list:
                continue
            else:
                lit.append(el)
    for n in lit:
        print(n)
        
# def find_elem(el, in_data):
#     list = {}
#     count = 0
#     for i in in_data:  #  i - словарь
#         if el in i.values():  # el - входящее слово, i.values() - список значений
#             count += 1
#             list.update({el: count})
#             continue
#         else:
#             list[el] = count
#     return list


# print(xl_2_list(file_path))
find_elem(xl_2_list(file_path))
# print(find_elem("Свой", xl_2_list(file_path)))

#     if line.startswith("№"):  # Если чтрока начинается с "ID"
#         is_reading = True  # то флаг переключается в True
#         if is_reading:  # если флаг включен и строка пустая
#             break  # то прервать цикл

#         if is_reading:  # При включении флага
#             row = clean_line.split()  # Разделяем строку по пробельным символам на ряды
#             if len(row) >= 4:  # Если количество рядов в строке больше либо равно 4,
#                 item = {  # то формируем словарь из ключей и значений
#                     "ID": int(row[0]),
#                     "x1": float(row[1]),
#                     "x2": float(row[2]),
#                     "Class": row[3],
#                 }
#                 data.append(item)  # и добавляем словарь в список словарей

# print(data)


# def process_email(text):
#     text = text.lower()
#     return list(set(text.split()))


# emails["words"] = emails["text"].apply(process_email)
# sum(emails["spam"]) / len(emails)

# model = {}  # создаем пучстой словарь

# for (
#     index,
#     row,
# ) in (
#     emails.iterrows()
# ):  # Перебираем кортежи из индексов (номеров) строк и их содержимых
#     # print(row)
#     for word in row["words"]:  # перебираем содержимое строк в столбце words
#         if word not in model:  # если слова нет в словаре
#             model[word] = {
#                 "spam": 1,
#                 "ham": 1,
#             }  # то добавляем в словарь model ключ с содержимым word и значением {'spam' : 1, 'ham': 1} Сглаживание Лапласа, чтобы избежать нулевого количества и случайно не разделить на 0
#         if word in model:
#             if row["spam"]:  # если в стобце spam - 1 то верется True, если 0, то False
#                 model[word][
#                     "spam"
#                 ] += 1  # если в стобце spam - 1 то значение spam увеличивается на 1
#             else:
#                 model[word][
#                     "ham"
#                 ] += 1  # если в стобце spam - 0 то значение ham увеличивается на 1
# # print(f'{model['sale']}')


# def predict_naive_bayes(email):
#     total = len(emails)
#     num_spam = sum(emails["spam"])
#     num_ham = total - num_spam
#     email = email.lower()
#     words = set(email.split())
#     spams = [1.0]
#     hams = [1.0]
#     for word in words:
#         if word in model:
#             spams.append(model[word]["spam"] / num_spam * total)
#             hams.append(model[word]["ham"] / num_ham * total)
#     prod_spams = np.long(np.prod(spams) * num_spam)
#     prod_hams = np.long(np.prod(hams) * num_ham)
#     return prod_spams / (prod_spams + prod_hams)

#  print(predict_naive_bayes("dffsaf asdfvfbdvs asfvbd sefaewbnl, gbrn,"))
