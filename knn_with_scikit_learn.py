from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 1. Подготовка данных (Матрица признаков X и вектор ответов y)
# Координаты (x1, x2)
X = np.array([
    [1.0, 2.0], [1.5, 1.0], [2.0, 2.5], [2.5, 1.5], [3.0, 2.0],
    [5.5, 6.0], [6.0, 5.5], [6.5, 6.5], [7.0, 5.0], [7.5, 6.0],
    [8.5, 3.0], [9.0, 2.5]
])

# Классы
y = np.array(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C'])

# 2. Инициализация и обучение модели
# n_neighbors=5 — это ваш параметр k
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# 3. Предсказание для новой точки P = (4.0, 3.5)
P = np.array([[4.0, 3.5]])
prediction = knn.predict(P)

print(f"Предсказанный класс для точки {P[0]}: {prediction[0]}")