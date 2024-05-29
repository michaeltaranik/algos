import random


def selection(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    L = []
    R = []
    M = []
    for i in range(len(arr)):
        if arr[i] > pivot:
            R.append(arr[i])
        elif arr[i] < pivot:
            L.append(arr[i])
        else:
            M.append(arr[i])
    if k < len(L):
        return selection(L, k)
    if len(L) + len(M) <= k:
        return selection(R, k - (len(L) + len(M)))
    else:
        return pivot


def find_median(arr):
    if len(arr) % 2 == 0:
        return (selection(arr, (len(arr) - 1) // 2) + selection(arr, len(arr) // 2)) / 2
    else:
        return selection(arr, len(arr) // 2)


B = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(find_median(A))
# print(find_median(B))
# print(selection(A, len(A) - 1))


def sort_e_top(arr):
    median = find_median(arr)
    print(median)
    even = 0
    i = 0

    while i < len(arr) and even < len(arr):

        if arr[i] >= median and arr[even] < median:
            arr[i], arr[even] = arr[even], arr[i]
            even += 2

        elif arr[i] >= median and arr[even] > median:
            even += 2

        i += 1

    return arr


# print(sort_e_top([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(sort_e_top([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(sort_e_top([9, 1, 3, 2, 5, 7, 6, 3, 2, 8, 0, 8, 5, 43, 2, 456, 7, 88]))
