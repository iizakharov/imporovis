# Бинарный поиск

import random

a = 2400
list = []
for i in range(a):
    list.append(i)

nomber = random.randint(1, a)


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(list, nomber))