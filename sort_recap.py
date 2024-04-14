def heapify(arr, parent, end):
    largest = parent
    left = parent * 2 + 1
    right = parent * 2 + 2

    if left < end and arr[left] > arr[largest]:
        largest = left

    if right < end and arr[right] > arr[largest]:
        largest = right

    if parent != largest:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        heapify(arr, largest, end)


def heap_sort(arr):
    end = len(arr)

    for i in range(end // 2, -1, -1):
        heapify(arr, i, end)

    for j in range(end - 1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j)
    return arr


# print(heap_sort([90,10,30,20,50,70,40,30,40,100,50]))


def partition_(arr, low, high):
    j = low - 1
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[high] = arr[high], arr[j + 1]
    return j + 1


def quick_sort_(arr, low, high, decreasing):
    if low < high:
        pivot_index = partition_(arr, low, high, decreasing)
        quick_sort_(arr, low, pivot_index - 1, decreasing)
        quick_sort_(arr, pivot_index + 1, high, decreasing)
    return arr


def quick_sorted(arr):
    return quick_sort_(arr, 0, len(arr) - 1, False)


# print(quick_sorted([90,10,30,20,50,70,40,30,40,100,50]))


def max_heapify(arr, parent, end):
    largest = parent
    left = parent * 2 + 1
    right = parent * 2 + 2

    if left < end and arr[left] > arr[largest]:
        largest = left

    if right < end and arr[right] > arr[largest]:
        largest = right

    if parent != largest:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        max_heapify(arr, largest, end)


def max_heap_insert(arr, x):
    arr.append(x)
    end = len(arr)
    for i in range(end // 2 - 1, -1, -1):
        max_heapify(arr, i, end)
    return arr


H = [3, 7, 3, 2, 9, 5, 9, 8, 5, 2, 9, 4, 7, 3, 9]

# arr = (max_heap_insert([], 3))
# print(arr)
# arr = (max_heap_insert(arr, 7))
# print(arr)
# arr = (max_heap_insert(arr, 3))
# print(arr)
# arr = (max_heap_insert(arr, 2))
# print(arr)
# arr = (max_heap_insert(arr, 9))
# print(arr)
# arr = (max_heap_insert(arr, 5))
# print(arr)
# arr = (max_heap_insert(arr, 9))
# print(arr)
# arr = (max_heap_insert(arr, 8))
# print(arr)
# arr = (max_heap_insert(arr, 5))
# print(arr)
# arr = (max_heap_insert(arr, 2))
# print(arr)
# arr = (max_heap_insert(arr, 9))
# print(arr)
# arr = (max_heap_insert(arr, 4))
# print(arr)
# arr = (max_heap_insert(arr, 7))
# print(arr)
# arr = (max_heap_insert(arr, 3))
# print(arr)
# arr = (max_heap_insert(arr, 9))
# print(arr)

# def rotate_inplace(arr, k):
#     previous = len(arr) - 1
#     current = previous - k
#     end = len(arr)
#     copy_prev = arr[previous]
#     while end > 0:
#         copy_current = arr[current]
#         arr[current] = copy_prev
#         previous = current
#         copy_prev = copy_current
#         current = current - k
#         if current < 0:
#             current = len(arr) + current
#         end -= 1
#     return arr


# exercise 243
def reversing(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_inplace(arr, k):
    n = len(arr)
    k = k % n
    reversing(arr, 0, k - 1)
    reversing(arr, k, n - 1)
    reversing(arr, 0, n - 1)
    return arr


# print(rotate_inplace([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0))
# print(rotate_inplace([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
# print(rotate_inplace([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
# print(rotate_inplace([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# print(rotate_inplace([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


# exercise 244
def increasing(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False


def decreasing(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False


def is_sorted(arr):
    if increasing(arr) == False and decreasing(arr) == False:
        return False
    else:
        return True


# print(is_sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(is_sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(is_sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(is_sorted([3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def square_root(n):
    min = -1
    max = n + 1
    if n == 3:
        return 1
    middle = (min + max) // 2
    while min < max:
        middle = (min + max) // 2
        if middle * middle > n:
            max = middle
        if middle * middle < n:
            min = middle + 1
        if middle * middle == n:
            return middle
    return middle


# print(square_root(0))
# print(square_root(1))
# print(square_root(3))
# print(square_root(9))
# print(square_root(10))
# print(square_root(13))
# print(square_root(24))
# print(square_root(100))
# print(square_root(169))


def original_elments(arr):
    count = 0
    n = len(arr) - 1
    i = 0
    quick_sort(arr, i, n, False)
    while i <= n:
        if (arr[i] != arr[i - 1] or i == 0) and (i == n or arr[i] != arr[i + 1]):
            count += 1
        i += 1
    return count


# print(original_elments([1,2,3,4,5,6])) #6
# print(original_elments([1,2,3,4,6,6])) #4
# print(original_elments([0])) #1
# print(original_elments([0,0])) #0
# print(original_elments([3, 2, 3, 3, 2])) #0
# print(original_elments([9, 8, 9, 6, 7, 1, 7])) #3


def reverse(arr, begin, end):
    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1
    return arr


def shift_right(arr, k):
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, len(arr) - 1)
    # reverse(arr, 0, len(arr) - 1)
    return arr


# print(shift_right([1,2,3,4,5,6,7,8,9], 1))

# Exercise 242
# def peapify(arr, parent, end, ascending):
#     if ascending:
#         largest = parent
#         left = parent * 2 + 1
#         right = parent * 2 + 2

#         if left < end and arr[left] > arr[largest]:
#             largest = left

#         if right < end and arr[right] > arr[largest]:
#             largest = right

#         if parent != largest:
#             arr[parent], arr[largest] = arr[largest], arr[parent]
#             peapify(arr, largest, end, ascending)
#     else:
#         smallest = parent
#         left = parent * 2 + 1
#         right = parent * 2 + 2

#         if left < end and arr[left] < arr[smallest]:
#             smallest = left

#         if right < end and arr[right] < arr[smallest]:
#             smallest = right

#         if parent != smallest:
#             arr[parent], arr[smallest] = arr[smallest], arr[parent]
#             peapify(arr, smallest, end, ascending)


# def peak_sort(arr, begin, end, ascending):

#     for i in range((end + begin) // 2, begin -1, -1):
#         peapify(arr, i, end, ascending)

#     for j in range(end - 1, begin - 1, -1):
#         arr[begin], arr[j] = arr[j], arr[begin]
#         peapify(arr, begin, j, ascending)

#     return arr


def partition(arr, begin, end, reversed):
    pivot = arr[end]
    j = begin - 1
    for i in range(begin, end):
        if reversed:
            if arr[i] >= pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
        elif reversed == False:
            if arr[i] <= pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[end] = arr[end], arr[j + 1]
    return j + 1


def quick_sort(arr, begin, end, reversed):
    if begin < end:
        pivot_index = partition(arr, begin, end, reversed)
        quick_sort(arr, begin, pivot_index - 1, reversed)
        quick_sort(arr, pivot_index + 1, end, reversed)
    return arr


def peak_order(arr):
    quick_sort(arr, 0, len(arr) // 2 - 1, False)
    quick_sort(arr, len(arr) // 2, len(arr) - 1, True)
    return arr


print(peak_order([9, 5, 3, 4, 6, 8, 7, 1, 0, 3, 8, 3, 2, 3, 5, 7, 9, 9]))

# A = [0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,9,8,1,3,4]
# print(peak_sort(A, len(A) // 2, len(A), False))
