import os
from openpyxl import load_workbook

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset.xlsx")


def xl_2_list(file):
    data = []  # Пустой список, для сохранения извлеченных из файла данные
    workbook = load_workbook(file)
    page = workbook.active
    for row in page.iter_rows(values_only=True):
        # if isinstance(row[0], int):
        item = {
            "ID": row[0],
            "x1": row[1],
            "x2": row[2],
            "x3": row[3],
            "Class": row[4],
        }  # {'ID': 1, 'x1': 'Цифра', 'x2': 'АК-74', 'x3': 'Патруль', 'Class': 'Свой'}

        data.append(item)

    return data


def get_params(in_data):
    data = []
    for item in in_data:
        if isinstance(item["ID"], int):
            data.append(item)
    return data


def get_X(in_data):
    for item in in_data:
        if item["Class"] == "?":
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

    return cond_P_dict


def calc_Bayes_P(priori_P_list, cond_P_dict):
    #  priori_P_list = {'Свой': 0.5, 'Враг': 0.5}
    #  cond_P_dict = {'Свой': {'АК-74': 0.75, 'Бег': 0.25, 'Мультикам': 0.25}, 'Враг': {'Мультикам': 0.5, 'Бег': 0.5, 'АК-74': 0.25}}
    bayes_P_dict = {}
    full_P = 0
    for c in priori_P_list:  # {'Свой': 0.5, 'Враг': 0.5}
        bayes_P = 1 * priori_P_list[c]
        # print(priori_P_list[c])
        # print(cond_P_dict[c])
        for b in cond_P_dict[c]:
            bayes_P *= cond_P_dict[c][b]
        full_P += bayes_P
        bayes_P_dict[c] = bayes_P

    for b in bayes_P_dict:
        bayes_P_dict[b] = round(bayes_P_dict[b] / full_P * 100, 2)
    return bayes_P_dict


dataset = xl_2_list(file_path)  # получаем список из файла
params = get_params(dataset)  # из списка получаем объекты с параметрами
obj_x = get_X(dataset)  # из списка получаем искомый объект
sorted_ds = find_classes(params)  # сортируем список объектов с параметрами по классам
priori_P = get_priori_P(sorted_ds)  # из сортированного сптска получаем априорные вероятности
cond_P = calc_cond_P(obj_x, sorted_ds)  # Получаем условные вероятности
bayes_P = calc_Bayes_P(priori_P, cond_P)  # Считаем вероятности по Байесу
print("\nАПРИОРНЫЕ ВЕРОЯТНОСТИ:\n\t", priori_P)
print("\nУСЛОВНЫЕ ВЕРОЯТНОСТИ:\n\t", cond_P)
print("\nВЕРОЯТНОСТЬ ПО БАЙЕСУ:\n\t", bayes_P)
