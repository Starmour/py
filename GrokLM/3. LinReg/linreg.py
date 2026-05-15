from matplotlib import pyplot as plt
import numpy as np


def draw_line(slope, y_intercept, color="green", linewidth=0.7, starting=0, ending=8):
    x = np.linspace(starting, ending, 1000)
    plt.plot(
        x, y_intercept + slope * x, linestyle="-", color=color, linewidth=linewidth
    )


def plot_points(features, labels, h, s):
    X = np.array(features)
    y = np.array(labels)
    plt.plot(features, labels)
    plt.scatter(X, y, color="blue", s=5)
    plt.scatter(h, s, color="green", s=5)
    plt.annotate(f"{h}; {s}", (h, s), textcoords="offset points", xytext=(0, -15))
    plt.xlabel("hours")
    plt.ylabel("score")
    plt.show()


def analyt_predict(h):
    initial_X = np.array([1, 2, 3, 4, 5])
    ones = np.ones((initial_X.shape[0], 1))
    X = np.hstack((ones, initial_X.reshape(-1, 1)))
    print(X)
    y = np.array([64, 71, 74, 82, 84]).reshape(5, 1)
    X_trans = X.transpose()
    XtX = np.dot(X_trans, X)
    Xty = np.dot(X_trans, y)
    rev_X = np.linalg.matrix_power(XtX, -1)
    bw = np.dot(rev_X, Xty)
    b = bw[0, 0]
    w = bw[1, 0]
    s = round(w * 6 + b, 2)
    draw_line(w, b, "red", starting=0, ending=8)
    plot_points(initial_X, y, h, s)


# print(s)
analyt_predict(6)
