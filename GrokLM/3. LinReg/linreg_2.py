from matplotlib import pyplot as plt
import numpy as np


def analyt_predict():
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
    X = np.array(initial_X)
    print("Numpy array initial_X:\n X =\n", X)
    y = np.array(initial_y).reshape(len(initial_y), 1)
    print("Numpy array initial_y:\n y =\n", y)
    X_trans = X.transpose()
    print("Transroned matrix X:\n Xt =\n", X_trans)
    XtX = np.dot(X_trans, X)
    print("Multiplied transponed matrix X and matrix X:\n XtX =\n", XtX)
    Xty = np.dot(X_trans, y)
    print("Multiplied transponed matrix X and matrix y:\n Xty =\n", XtX)
    inv_X = np.linalg.matrix_power(XtX, -1)
    print("Inversed multiplied transponed matrix X and matrix X (XtX):\n (XtX)^-1 =\n", inv_X)
    bw = np.dot(inv_X, Xty)
    print("Multiplied inversed matrix X (inv_X) and multiplied transponed matrix X and matrix y (Xty):\n (Xt*X)^-1 * Xty =\n", bw)
    b = bw[0, 0]
    print("Bias:\n b =", b)

    w_list = []
    for i in range(len(bw)):
        w = bw[i,0]
        w_list.append(w)
    new_x = [4,2,1,0,2]
    for i in range(len(new_x)):
        wx = w_list[i] * new_x[i]

    wx = 0
    for i in range(len(new_x)):
        wx += w_list[i] * new_x[i]
    print("Predicted y without bias: \n w1*x1 + w2x2 + w3x3 + w4x4 + w5x5 =", wx)
    y_new_x = wx + b
    print("Predicted y : \n b + w1*x1 + w2x2 + w3x3 + w4x4 + w5x5 =", y_new_x)
    # s = round(w * 6 + b, 2)
    # draw_line(w, b, "red", starting=0, ending=8)
    # plot_points(initial_X, y, h, s)


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


# print(s)
analyt_predict()
