def num_og_el(A):
    hash_map = {}
    for i in range(0, len(A)):
        if A[i] in hash_map:
            hash_map[A[i]] += 1
        else:
            hash_map[A[i]] = 1
    x = 0 
    for key in hash_map.keys():
        if hash_map[key] == 1:
            x += 1
    return x

#print(num_og_el([1, 2, 3, 2, 4, 8]))
#print(num_og_el([1, 2, 3, 2, 4, 4, 8]))


def algo_x(A,x):
    i = len(A) - 1
    j = 0
    while i >= 0:
        if j == i:
            j = 0
            i = i - 1
        elif A[i] - A[j] > x or A[j] - A[i] > x:
            return True
        else:
            j = j + 1
    return False

#print(algo_x([1, 2, 3, 4, 5], 3))

def better_algo_x(A, x):
    A.sort()
    i = 0
    j = len(A) - 1
    if A[j] - A[i] > x:
        return True
    return False

#print(better_algo_x([1, 2, 3, 4, 5], 3))
#print(better_algo_x([1,4,1,2,1,2,12,21,1,1], 10))


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

#print(sorted([8, 2, 5, -12, 2, 11, -15, -8, -1, 12], False))

def mountain_sort(A):
    quick_sort(A, 0, len(A)//2, False)
    quick_sort(A, len(A)//2, len(A) - 1, True)
    return A

#print(mountain_sort([8, 2, 5, -12, 2, 11, -15, -8, -1, 12]))


def square_root(n):
    def binary_search(low, high):
        while low <= high:
            middle = (high + low) // 2
            if middle * middle > n:
                high = middle
            elif middle * middle <= n and (middle + 1) * (middle + 1) > n :
                return middle
            else:
                low = middle + 1
    sqrt = binary_search(0, n)
    return sqrt
     
#print(square_root(196))



def find_the_difference(A, x):
    i = len(A) - 2
    j = len(A) - 1
    while i >= 0 and j > i:
        diff = A[j] - A[i]
        if diff > x:
            j -= 1
        elif diff < x:
            i -= 1
        elif diff == x:
            return True
    return False


#print(find_the_difference([1,2,3,4,5,8,10,15], 0))


def increasing_or_decreasing(A):
    flat = 0
    increasing = 0
    decreasing = 0
    previous_flat = 0
    previous_increasing = 0
    previous_decreasing = 0
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            increasing += 1
            flat = 0
            decreasing = 0
        elif A[i] < A[i - 1]:
            increasing = 0
            flat = 0
            decreasing += 1
        else:
            increasing = 0
            flat += 1
            decreasing = 0
        previous_increasing = increasing if increasing > previous_increasing else previous_increasing
        previous_decreasing = decreasing if decreasing > previous_decreasing else previous_decreasing
        previous_flat = flat if flat > previous_flat else previous_flat
    if previous_increasing == previous_decreasing != 0:
        return "equal"
    elif previous_increasing > previous_flat and previous_increasing > previous_decreasing:
        return "increasing"
    elif previous_decreasing > previous_flat and previous_decreasing > previous_increasing:
        return "decreasing"
    else:
        return "flat"

# print(increasing_or_decreasing([1,1,1,1,1]))
# print(increasing_or_decreasing([1,20,11,10,1,0]))
# print(increasing_or_decreasing([1,2,3,2,8,10,1,0]))
# print(increasing_or_decreasing([1]))
# print(increasing_or_decreasing([1,1,1,1,1]))
# print(increasing_or_decreasing([1,2,1,2,1]))
# print(increasing_or_decreasing([1,2,1,2,10,1]))
    
def find_sum_el(A):
    max_index = 0
    for i in range(0, len(A)):
        if A[i] > A[max_index]:
            max_index = i
    sum = 0
    for j in range(0, len(A)):
        if j != max_index:
            sum = sum + A[j]
    if A[max_index] == sum:
        return True
    return False

#print(find_sum_el([1,2,3,4,0,0,0,0,0,0,11,0,0,0,1,1])) 




# git commit -m "midterm"