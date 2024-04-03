def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_array = [7,8,9,3,5,2,1,0,0,0,0,4,5,3,6,-90]
insertion_sort(my_array)
print("Sorted array:", my_array)
