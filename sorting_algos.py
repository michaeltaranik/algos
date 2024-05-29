import random


# def partition(arr, low, high):
#     pivot = arr[high]
#     j = low - 1
#     for i in range(low, high):
#         if arr[i] <= pivot:
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[j + 1], arr[high] = arr[high], arr[j + 1]
#     return j + 1


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         quick_sort(arr, pivot_index + 1, high)
#         quick_sort(arr, low, pivot_index - 1)
#     return arr


# def sorted(arr):
#     return quick_sort(arr, 0, len(arr) - 1)


# print(sorted([9,4,6,7,87,3,1,2,32,4,5,6,4,35,25,35,2]))


def select(arr, k):
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

    if len(L) > k:
        return select(L, k)

    elif len(L) + len(M) <= k:
        return select(R, k - (len(L) + len(M)))

    else:
        return pivot


# print(select([3, 2, 1, 4], 1))


def merge_sort(arr):
    if len(arr) > 1:
        left = arr[: len(arr) // 2]
        right = arr[len(arr) // 2 :]
        merge_sort(left)
        merge_sort(right)
        j = i = k = 0
        while j < len(right) and i < len(left):
            if right[j] < left[i]:
                arr[k] = right[j]
                k += 1
                j += 1
            elif right[j] >= left[i]:
                arr[k] = left[i]
                k += 1
                i += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

    return arr


def partition(arr, begin, end):
    j = begin - 1
    pivot = arr[end]
    for i in range(begin, end):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[end] = arr[end], arr[j + 1]
    return j + 1


def quick_sort(arr, begin, end):
    if begin < end:
        pivot_index = partition(arr, begin, end)
        quick_sort(arr, begin, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr


def heapify(arr, parent, end):
    largest = parent
    left = parent * 2 + 1
    right = parent * 2 + 2

    if left < end and arr[left] > arr[largest]:
        largest = left

    if right < end and arr[right] > arr[largest]:
        largest = right

    if largest != parent:
        arr[largest], arr[parent] = arr[parent], arr[largest]
        heapify(arr, largest, end)


def heap_sort(arr):
    end = len(arr)

    for i in range(end // 2, -1, -1):
        heapify(arr, i, end)

    for j in range(end - 1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j)

    return arr


to_sort = [9, 3, 2, 4, 6, 2, 55, 3, 63, 5, 35, 54, 25, 35, 45]
print(merge_sort(to_sort))
print(quick_sort(to_sort, 0, len(to_sort) - 1))
print(heap_sort(to_sort))
