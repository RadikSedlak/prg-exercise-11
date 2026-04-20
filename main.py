import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(seznam):
    values = seznam.copy()
    n = len(values)

    for i in range(n):
        min_i = i

        for j in range(i + 1, n):
            if values[j] < values[min_i]:
                min_i = j

        values[i], values[min_i] = values[min_i], values[i]

    return values


def bubble_sort(seznam):
    values = seznam.copy()

    plt.ion()
    plt.show()

    for i in range(len(values)):
        for j in range(len(values) - 1):

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

            # vizualizace
            index_highlight1 = j
            index_highlight2 = j + 1

            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

    plt.ioff()
    plt.show()

    return values


# testy
values = random_numbers(10)

print(selection_sort([5, 1, 4, 2, 8]))
print(selection_sort(values))

print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort(values))