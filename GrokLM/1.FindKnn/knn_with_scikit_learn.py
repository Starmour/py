from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os

data = []  # Пустой список, для сохранения извлеченных из файла данные
PARAMS = []
CLASSES = []

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "source.txt")  # Путь к файлу

is_reading = False  # Флаг "читаемости", который включается после начала таблицы

with open(file_path, "r", encoding="utf-8") as file:  # Безопасное открытие файла
    for line in file:  # Построчнй перебор файла
        clean_line = line.strip()  # Удаление пробеов по краям текущей строки

        # Начало чтения после заголовка таблицы
        if clean_line.startswith("ID"):  # Если чтрока начинается с "ID"
            is_reading = True  # то флаг переключается в True
            continue  # переход на новую строку

        # Остановка чтения, если встретили пустую строку или текст вне таблицы
        if is_reading and not clean_line:  # если флаг включен и строка пустая
            break  # то прервать цикл

        if is_reading:  # При включении флага
            row = clean_line.split()  # Разделяем строку по пробельным символам на ряды
            if len(row) >= 4:  # Если количество рядов в строке больше либо равно 4,
                obj_par = (
                    []
                )  # создаем масисив для хранеия параметров объетов из выборки
                obj_par.append(float(row[1]))  # 1-й параметр объекта
                obj_par.append(float(row[2]))  # 2-й параметр объекта
                PARAMS.append(
                    obj_par
                )  # массив с параметрами добавляем в массив параметров всех объектов
                CLASSES.append(row[3])  # создаем массив классов
# for row in PARAMS:
#     print(row)  # построчный вывод значений каждой записи сллваря
# for type in CLASSES:
#     print(type)


X = np.array(PARAMS)  # зачем метод np
y = np.array(CLASSES)  # зачем метод np

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

new_object = [[4.0, 3.5]]
prediction = knn.predict(new_object)

print(f"Предсказанный класс для точки {new_object[0]}: {prediction[0]}")
