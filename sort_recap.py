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
        arr[0], arr[j] =  arr[j], arr[0] 
        heapify(arr, 0, j)
    return arr

#print(heap_sort([90,10,30,20,50,70,40,30,40,100,50]))

def partition(arr, low, high):
    j = low - 1
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[high] = arr[high], arr[j + 1]
    return j + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr

def quick_sorted(arr):
    return quick_sort(arr, 0, len(arr) - 1)

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
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_inplace(arr, k):
    n = len(arr)
    k = k % n  
    reverse(arr, 0, k - 1) 
    reverse(arr, k, n - 1)  
    reverse(arr, 0, n - 1) 
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




