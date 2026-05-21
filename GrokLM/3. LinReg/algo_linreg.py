import numpy as np
import random


def linear_regression(xs, ys, lr=0.01, epochs=1000):
    w_0 = random.random()
    w_1 = random.random()
    for epoch in range(epochs):
        i = random.randint(0, len(xs) - 1)
        print("i = ", i)
        x_1 = xs[i]
        print("x_1 =", x_1)
        y_1 = ys[i]
        print("y_1 =", y_1)
        w_0, w_1 = square_trick(w_0, w_1, x_1, y_1, lr=lr)
        print(w_1, w_0)
        # input("Press Enter\n\t>")

    return w_0, w_1


def absolute_trick(w_0, w_1, x_1, y, lr):
    predicted_y = w_0 + w_1 * x_1
    if y > predicted_y:
        w_1 += lr * x_1
        w_0 += lr
    else:
        w_1 -= lr * x_1
        w_0 -= lr
    return w_1, w_0


# y = w_0 + w_1 * x_1; bp = w_0, ppr = w_1, nr = x_1, p =
def square_trick(w_0, w_1, x_1, y, lr):
    predicted_y = w_0 + w_1 * x_1
    w_0 += lr * (y - predicted_y)  # y-interceprion
    w_1 += lr * x_1 * (y - predicted_y)  # slope

    return w_1, w_0

initial_X = [
    [1, 1, 2, 0, 0, 1],
    [1, 2, 2, 1, 0, 2],
    [1, 3, 1, 2, 0, 2],
    [1, 5, 3, 1, 1, 3],
    [1, 4, 2, 0, 0, 3],
    [1, 7, 3, 3, 1, 3],
    [1, 1, 1, 0, 0, 1],
    [1, 8, 2, 2, 1, 2],
    [1, 2, 3, 1, 0, 1],
    [1, 6, 2, 4, 0, 3],
]
initial_y = [13, 21, 25, 43, 28, 54, 12, 52, 20, 43]

xs = np.array(initial_X)
ys = np.array(initial_y)
new_x = [4,2,1,0,2]
lr = 0.01
linear_regression(xs, ys, lr, epochs=10)
