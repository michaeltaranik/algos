def heapify(arr, parent, end, min_heap):
    largest = parent
    smallest = parent
    left = parent * 2 + 1
    right = parent * 2 + 2

    if min_heap:
        if left < end and arr[left] < arr[parent]:
            smallest = left

        if right < end and arr[right] < arr[smallest]:
            smallest = right

        if parent != smallest:
            arr[parent], arr[smallest] = arr[smallest], arr[parent]
            heapify(arr, smallest, end, min_heap)

    else:
        if left < end and arr[left] > arr[parent]:
            largest = left

        if right < end and arr[right] > arr[largest]:
            largest = right

        if parent != largest:
            arr[parent], arr[largest] = arr[largest], arr[parent]
            heapify(arr, largest, end, min_heap)
    

def heap_sort(arr, min_heap):
    end = len(arr)

    for i in range(end // 2 - 1, -1, -1):
        heapify(arr, i, end, min_heap)
    
    for i in range(end - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i, min_heap)

    return arr
    

# print(heap_sort([8, 2, 5, -12, 2, 11, -15, -8, -1, 12], True))
# print(heap_sort([60, 20, 40, 70, 30, 10], True))
# print(heap_sort([8, 2, 5, -12, 2, 11, -15, -8, -1, 12], False))
# print(heap_sort([60, 20, 40, 70, 30, 10], False))



def insert(value, arr, min_heap):
    arr.append(value)
    new_value_index = len(arr) - 1
    parent = (len(arr) - 1) // 2
    if min_heap:
        while arr[new_value_index] < arr[parent]:
            arr[new_value_index], arr[parent] = arr[parent], arr[new_value_index]
            new_value_index = parent
            parent = (parent - 1) // 2
        return arr
    else:
        while arr[new_value_index] > arr[parent]:
            arr[new_value_index], arr[parent] = arr[parent], arr[new_value_index]
            new_value_index = parent
            parent = (parent - 1) // 2
        return arr
        
H = [3,5,8,6,10,9,5,6,7,20,11,17,6,9,10]
heapify(H, 0, len(H), True)
print(insert(4, H, True))