import random

# from sorting_algos import *


def selection(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    L = []
    R = []
    M = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            L.append(arr[i])
        elif arr[i] > pivot:
            R.append(arr[i])
        else:
            M.append(arr[i])
    if len(L) > k:
        return selection(L, k)
    if len(L) + len(M) <= k:
        return selection(R, (k - len(L) - len(M)))
    else:
        return pivot


def find_median(arr):
    if len(arr) % 2 == 0:
        return (selection(arr, len(arr) // 2) + selection(arr, len(arr) // 2) - 1) / 2
    else:
        return selection(arr, len(arr) // 2)


# Exercise 253
def better_algo_x(arr, k):
    count = 0
    for i in range(0, k + 1):
        count = count + selection(arr, i)
    return count


# Exercise 254
def find_difference(arr, x):
    assert len(arr) > 0
    i = 0
    j = i + 1
    while i < len(arr) and j < len(arr):
        if arr[j] - arr[i] > x:
            i += 1
        if arr[j] - arr[i] < x:
            j += 1
        else:
            return True
    return False


A = [1, 2, 1, 2, 1, 2, 1, 2, 3, 0]
B = [9, 8, 6, 3, 8, 0, 1, 2, 4, 2]

# print(find_median(A))
# print(better_algo_x(B,2))

# print(find_difference([1,2,3,4,5,6,7,8,9], 4))


# Exercise 206
# Question 1:
# this algorithm returns True if there exist two elements of an array
# which difference is greater than x and False otherwise
# complexity is quadratic, worst_case scenario is when
# there is no such difference, then the algo has to iterate
# one loop inside another
# Question 2:
# we first sort the array and then we have to check the difference between the first
# and last elements in the array return False if diff. is less and True otherwise
def better_algo_x_206(arr, x):
    sorted(arr)
    if arr[len(arr) - 1] - arr[0] > x:
        return True
    else:
        return False


# Exercise 269:
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
# print(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(sort_e_top([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(sort_e_top([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2]))
# Exercise 266
def better_algo_x_266(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    for j in range(0, len(arr)):
        if arr[j] == sum - arr[j]:
            return True
    return False


# print(better_algo_x_266([1, 2, 10, 1, 6]))


def heapify(arr, parent, end):
    left = 2 * parent + 1
    right = 2 * parent + 2
    largest = parent

    if left < end and arr[left] > arr[largest]:
        largest = left

    if right < end and arr[right] > arr[largest]:
        largest = right

    if largest != parent:
        arr[largest], arr[parent] = arr[parent], arr[largest]
        heapify(arr, largest, end)


def heap_sort(arr):
    end = len(arr)

    for i in range(end // 2 - 1, -1, -1):
        heapify(arr, i, end)

    for j in range(end - 1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j)

    return arr


# print(heap_sort([9, 4, 6, 7, 87, 3, 1, 2, 32, 4, 5, 6, 4, 35, 25, 35, 2]))


def find_extremum(arr, begin, end, max):
    extremum = begin
    for i in range(begin + 1, end):
        if max:
            if arr[i] > arr[extremum]:
                extremum = i
        else:
            if arr[i] < arr[extremum]:
                extremum = i
    return extremum


A = [1, 3, 2, 6, 2, 1, 4, 7, 8, 0]
# print(find_extremum(A, 0, len(A), True))


def selection_sort(arr):
    j = 0
    end = len(arr)
    for i in range(0, end):
        min = find_extremum(arr, j, end, False)
        arr[j], arr[min] = arr[min], arr[j]
        j += 1
    return arr


# print(selection_sort([9, 4, 6, 7, 87, 3, 1, 2, 32, 4, 5, 6, 4, 35, 25, 35, 2]))
# print(selection_sort(A))


def max_heapify(arr):
    end = len(arr)
    for i in range(end // 2 - 1, -1, -1):
        heapify(arr, i, end)
    return arr, len(arr)


# H = [3, 7, 3, 2, 9, 5, 9, 8, 5, 2, 9, 4, 7, 3, 9]
# print(max_heapify(H))


# Exercise 241
# def high_power_run(arr, h, t):
#     max = 0
#     current = 0
#     for i in range(0, len(arr) - 1):
#         current = 0
#         for j in range(i, t + i):
#             if j + 1 < len(arr) and arr[j] < arr[j + 1]:
#                 current = current + (arr[j + 1] - arr[j])
#         if current > max:
#             max = current
#     # print(max)
#     if max >= h:
#         return True
#     return False


def high_power_run(arr, h, t):
    i = 0
    j = t
    current = 0

    for p in range(i, j):
        if arr[p] < arr[p + 1]:
            current = current + (arr[p + 1] - arr[p])

    maximum = current

    while j < len(arr) - 1:
        if arr[j] < arr[j + 1]:
            current += arr[j + 1] - arr[j]

        if arr[i] < arr[i + 1]:
            current -= arr[i + 1] - arr[i]

        maximum = max(maximum, current)
        j += 1
        i += 1

    if maximum >= h:
        return True

    return False


# print(high_power_run([10, 6, 1, 3, 2, 1, 3, 4, 6, 5, 6, 4, 3, 4], 6, 5))
# print(high_power_run([10, 6, 1, 3, 2, 1, 3, 4, 6, 5, 6, 4, 3, 4], 7, 5))


# Exercise 191
# def find_square(arr):


# Exercise 240
# def maximal_step_k_length(arr, k):
#     current = 0
#     max = current
#     i = 0
#     while i < len(arr) - 1:
#         if arr[i] - arr[i + 1] == k:
#             current += 1
#         else:
#             current = 0
#         if current > max:
#             max = current
#         i += 1
#     return max


def maximal_step_k_length(arr, k):
    current = 1
    maximum = current
    i = 0
    while i < len(arr) - 1:
        if arr[i] - arr[i + 1] == k:
            current += 1
            if current > maximum:
                maximum = current
        else:
            current = 1
        i += 1

    return maximum


# print(maximal_step_k_length([2, 4, 5, 6, 8, 6, 4, 2, 0, 2, 4, 6, 10, 3, 1], 2))


# Exercise 243
def reverse_list(arr, begin, end):
    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1
    return arr


def left_rotation(arr, k):
    reverse_list(arr, 0, k - 1)
    reverse_list(arr, k, len(arr) - 1)
    reverse_list(arr, 0, len(arr) - 1)
    return arr


# print(left_rotation([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# Exercise 227
def partition_mine(arr, begin, end):
    j = begin - 1
    pivot = arr[end]
    for i in range(begin, end):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[end] = arr[end], arr[j + 1]
    return j + 1


def quick_sort_mine(arr, begin, end):
    if begin < end:
        pivot_index = partition_mine(arr, begin, end)
        quick_sort_mine(arr, 0, pivot_index - 1)
        quick_sort_mine(arr, pivot_index + 1, end)
    return arr


# Y = [9, 5, 3, 1, 34, 56, 8, 6, 4, 0, 2, 5, 99]
# print(quick_sort_mine(Y, 0, len(Y) - 1))


# Exercise 206
def sum_of_three(arr, s):
    quick_sort_mine(arr, 0, len(arr) - 1)
    for i in range(len(arr)):
        target = s - arr[i]
        j = i + 1
        k = len(arr) - 1
        while j < k:
            if arr[j] + arr[k] < target:
                k -= 1
            elif arr[j] + arr[k] > target:
                j += 1
            else:
                return True
    return False


# sum_3 = [1, 2, 3, 4, 5, 6, 8, 9, 11]
# print(sum_of_three(sum_3, 29))


# Exercise 193
def maximal_distance(arr):
    if len(arr) < 2:
        return 0

    high = low = arr[0]

    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]

        if arr[i] < low:
            low = arr[i]

    return high - low


# Exercise 194
def bst_height(t):
    if t == 0:
        return 0
    return 1 + max(bst_height(t.left) + bst_height(t.right))


# Exercise 190
def better_algo_x_190(arr):
    i = 0
    j = 1
    current = 0
    maximum = current
    while j < len(arr):
        if arr[j - 1] <= arr[j]:
            current = arr[j] - arr[i]
            j += 1
        else:
            i = j
            j = i + 1

        maximum = max(current, maximum)

    return maximum


# print(better_algo_x_190([1, 2, 0, 3, 4, 5, 6, 7, 1, 2, 10]))
