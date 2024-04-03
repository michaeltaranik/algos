def largest_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

print(largest_subarray_sum([1, 2, 3, 4, -9, 95]))
print(largest_subarray_sum([-6, -7, -3, -2]))

