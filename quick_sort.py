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


def sorted(arr, reversed):
    return quick_sort(arr, 0, len(arr) - 1, reversed)

print(sorted([8, 2, 5, -12, 2, 11, -15, -8, -1, 12], False))
