import numpy
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr


def mass(n):
    a = []
    l = list(range(1, 1000))
    random.shuffle(l)
    j = 0

    for i in range(n):
        a.append(numpy.random.random_integers(1, 1000, l[j]))
        j += 1
    for k in range(len(a)):
        if k % 2 == 0:
            a[k] = insertion_sort(a[k])
        else:
            a[k] = insertion_sort(a[k])
            a[k] = a[k][::-1]
    return a
