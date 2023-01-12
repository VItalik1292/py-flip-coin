import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0,
              5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    result_in_percents = {}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            head_rand = random.randint(0, 1)
            if head_rand == 0:
                head += 1
        result[head] += 1
        # if head in result:
        #     result[head] += 1
        # else:
        #     result[head] = 1

    for i in range(11):
        result_in_percents[i] = result[i] / 10000 * 100

    return result_in_percents


def draw_gaussian_distribution_graph() -> None:
    x_points = []
    y_points = []
    for index in range(len(flip_coin())):
        x_points.append(index)
        y_points.append(flip_coin[index])

    plt.plot(x_points, y_points)
    plt.show()
