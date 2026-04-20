import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)
print(values)

small = random_numbers(5, low=0, high=20)


def selection_sort(seznam):
    seznam = seznam.copy()
    delka = len(seznam)

    for pozice in range(delka):
        index_minima = pozice

        for dalsi in range(pozice + 1, delka):
            if seznam[dalsi] < seznam[index_minima]:
                index_minima = dalsi

        seznam[pozice], seznam[index_minima] = seznam[index_minima], seznam[pozice]

    return seznam


# testik
print(selection_sort([5, 1, 4, 2, 8]))
print(selection_sort(values))
