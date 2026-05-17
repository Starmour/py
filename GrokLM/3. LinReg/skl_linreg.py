from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import numpy as np


def analyt_predict(x_array, y_array, new_X):
    matrix_X = np.array(x_array)
    matrix_y = np.array(y_array)
    ones_array = np.ones((matrix_X.shape[0], 1))
    X = np.hstack((ones_array, matrix_X.reshape(-1, 1)))
    y = matrix_y
    new_X = np.array([new_X])
    ones_array = np.ones((new_X.shape[0], 1))
    new_X = np.hstack((ones_array, new_X.reshape(-1, 1)))
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(new_X)

    return y_pred


hours = 6
initial_X = [1, 2, 3, 4, 5]
initial_y = [64, 71, 74, 82, 84]
predict = analyt_predict(initial_X, initial_y, hours)
print("Prediction of score for 6 hours preparing is", predict[0], "points")
