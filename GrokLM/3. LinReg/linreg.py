from matplotlib import pyplot as plt
import numpy as np
import random


def draw_line(slope, y_intercept, color="green", linewidth=0.7, starting=0, ending=8):
    x = np.linspace(starting, ending, 1000)
    plt.plot(
        x, y_intercept + slope * x, linestyle="-", color=color, linewidth=linewidth
    )


def plot_points(features, labels):
    X = np.array(features)
    y = np.array(labels)
    # plt.plot(features, labels)
    plt.scatter(X, y)
    plt.xlabel("hours")
    plt.ylabel("score")
    plt.show()


def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):
    predicted_price = base_price + price_per_room * num_rooms
    base_price += learning_rate * (price - predicted_price)
    price_per_room += learning_rate * num_rooms * (price - predicted_price)
    return price_per_room, base_price


def linear_regression(features, labels, learning_rate=0.01, epochs=1000):
    price_per_room = random.random()
    base_price = random.random()
    for epoch in range(epochs):
        i = random.randint(0, len(features) - 1)
        num_rooms = features[i]
        price = labels[i]
        price_per_room, base_price = square_trick(
            base_price, price_per_room, num_rooms, price, learning_rate=learning_rate
        )
        draw_line(price_per_room, base_price, "red", starting=0, ending=8)
        plot_points(features, labels)
        print("Price per room:", price_per_room)
        print("Base price:", base_price)
        return price_per_room, base_price
    return price_per_room, base_price


features = np.array([1, 2, 3, 4, 5])
labels = np.array([64, 71, 74, 82, 84])

print(features)
print(labels)
plot_points(features, labels)
linear_regression(features, labels, learning_rate = 0.01, epochs = 10000)

# def simple_trick(base_price, price_per_room, num_rooms, price):
#     small_random_1 = random.random() * 0.1
#     small_random_2 = random.random() * 0.1
#     predicted_price = base_price + price_per_room * num_rooms
#     if price > predicted_price and num_rooms > 0:
#         price_per_room += small_random_1
#         base_price += small_random_2
#     if price > predicted_price and num_rooms < 0:
#         price_per_room -= small_random_1
#         base_price += small_random_2
#     if price < predicted_price and num_rooms > 0:
#         price_per_room -= small_random_1
#         base_price -= small_random_2
#     if price < predicted_price and num_rooms < 0:
#         price_per_room -= small_random_1
#         base_price += small_random_2
#     return price_per_room, base_price


# def absolute_trick(base_price, price_per_room, num_rooms, price, learning_rate):
#     predicted_price = base_price + price_per_room * num_rooms
#     if price > predicted_price:
#         price_per_room += learning_rate * num_rooms
#         base_price += learning_rate
#     else:
#         price_per_room -= learning_rate * num_rooms
#         base_price -= learning_rate
#     return price_per_room, base_price


# def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):
#     predicted_price = base_price + price_per_room * num_rooms
#     price_per_room += learning_rate * num_rooms * (price - predicted_price)
#     base_price += learning_rate * (price - predicted_price)
#     return price_per_room, base_price


# We set the random seed in order to always get the same results.
# random.seed(0)


# def linear_regression(features, labels, learning_rate=0.01, epochs=1000):
#     price_per_room = 6
#     base_price = random.random()
#     for epoch in range(epochs):
#         # Uncomment any of the following lines to plot different epochs
#         # if epoch == 1:
#         # if epoch <= 10:
#         # if epoch <= 50:
#         # if epoch > 50:
#         if True:
#             draw_line(price_per_room, base_price, starting=0, ending=8)
#         i = random.randint(0, len(features) - 1)
#         num_rooms = features[i]
#         price = labels[i]
#         # Uncomment any of the 2 following lines to use a different trick
#         # price_per_room, base_price = absolute_trick(base_price,
#         price_per_room, base_price = square_trick(
#             base_price, price_per_room, num_rooms, price, learning_rate=learning_rate
#         )
#     draw_line(price_per_room, base_price, "red", starting=0, ending=8)
#     plot_points(features, labels)
#     print("Price per room:", price_per_room)
#     print("Base price:", base_price)
#     return price_per_room, base_price


# plt.ylim(0, 500)

# linear_regression(features, labels, learning_rate=0.01, epochs=1000)
