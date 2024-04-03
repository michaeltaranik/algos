def partition(arr, low, high):
    pivot = arr[high]
    j = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j + 1], arr[high] = arr[high], arr[j + 1]
    return j + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, pivot_index + 1, high)
        quick_sort(arr, low, pivot_index - 1)
    return arr

def sorted(arr):
    return quick_sort(arr, 0, len(arr) - 1)


print(sorted([9,4,6,7,87,3,1,2,32,4,5,6,4,35,25,35,2]))

