import os
import math  # Импорт библиотеки для работы с математическими функциями
data = [] # Пустой список, для сохранения извлеченных из файла данные
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "source.txt") # Путь к файлу
# file_path = r".//source.txt" # Путь к файлу
is_reading = False # Флаг "читаемости", который включается после начала таблицы

with open(file_path, "r", encoding="utf-8") as file: # Безопасное открытие файла
    for line in file: # Построчнй перебор файла
        clean_line = line.strip() # Удаление пробеов по краям текущей строки
        
        # Начало чтения после заголовка таблицы
        if clean_line.startswith("ID"): # Если чтрока начинается с "ID"
            is_reading = True # то флаг переключается в True
            continue # переход на новую строку
            
        # Остановка чтения, если встретили пустую строку или текст вне таблицы
        if is_reading and not clean_line: # если флаг включен и строка пустая
            break # то прервать цикл
            
        if is_reading: # При включении флага
            row = clean_line.split() # Разделяем строку по пробельным символам на ряды
            if len(row) >= 4: # Если количество рядов в строке больше либо равно 4, 
                item = { # то формируем словарь из ключей и значений  
                    "ID": int(row[0]),
                    "x1": float(row[1]),
                    "x2": float(row[2]),
                    "Class": row[3]
                }
                data.append(item) # и добавляем словарь в список словарей
for row in data:
    print(row) # построчный вывод значений каждой записи сллваря



P = {'x1': 4.0, 'x2': 3.5} # Объект для предсказания с входными данными
k = 5

# добавляем в словарь item списка data новый ключ dist со значением равным эвклидовому растоянию от точки выборки до точки объекта  
for item in data:
    item['dist'] = math.sqrt((item['x1'] - P['x1'])**2 + (item['x2'] - P['x2'])**2)

sorted_data = sorted(data, key=lambda x: x['dist']) # сортировка сравнение словарей в списке data по значеию ключа dist при помощи лямбда функции

neighbors = sorted_data[:k] # отбор значений в отсортированном списке от 0 до k (не включая)

# 4. Подсчет голосов за классы
votes = {} # создание словаря голосов
for n in neighbors: # пробегаем по отсортированному списку, где n - это словарь с ключами и значениями
    cls = n['Class'] # переменной cls присваиваем значение с ключом Class в словаре n
    votes[cls] = votes.get(cls, 0) + 1 # запись в словарь голосов количества ключей равных значениям переменной cls (если таких нет - 0, и запись в словарь, если есть, то + 1 )

print("\nVotes: ", votes)
prediction = max(votes, key=votes.get) # сравнение значений, полученных по ключам словаря votes

print(f"\nПредсказанный класс: {prediction} \n")
# print(f"Соседи: {[(n['ID'], n['Class'], round(n['dist'], 2)) for n in neighbors]} \n")
print("Соседи:")
for n in neighbors:
    print(n["ID"], ",", n["Class"], ",", round (n['dist'], 2))
    print(f"{[(n['ID'], n['Class'], round(n['dist'], 2))]}")
# for row in data:
#     print(row)