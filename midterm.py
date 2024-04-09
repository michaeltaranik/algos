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
    min = -1
    max = n + 1
    middle = (min + max) // 2
    while min < max:
        middle = (min + max) // 2
        if middle * middle < n:
            min = middle + 1
        if middle * middle > n:
            max = middle
        if middle * middle == n:
            return middle
    return middle
     
# print(square_root(196))



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

def reverse(arr, begin, end):
    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1


def rotate_inplace(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr

# print(rotate_inplace([1,2,3,4,5,6,7,8,9], 4))


# Exercise 228
def binary_search_bound(arr, left, right, x):
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] > x:
            right = middle
        if arr[middle] < x:
            left = middle
        if arr[middle] == x:
            return arr[middle]
    return arr[middle]

def lower_bound(arr, x):
    left = -1
    right = len(arr)
    lower = binary_search_bound(arr, left, right, x)
    if lower < x:
        return "not found"
    else:
        return lower

# print(lower_bound([1,2,3,4,5,6,8,9], 7))
# print(lower_bound([1,2,3,4,5,6,7,8,9], 1))
# print(lower_bound([1,2,3,4,5,6,7,8,9], 100))
# print(lower_bound([1,2,3,4,5,6,7,8,9], 9))
# print(lower_bound([1,2,3,4,5,6,7,8,9], 0))
    

# Exercise 224
def partition_zero(arr):
    j = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    for i in range(j - 1, len(arr)):
        if arr[i] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr

# print(partition_zero([2, 5, 0, -1, 3, -7, 0, 3, -1, 10]))

# Exercise 208
def sort_special(arr):
    a = arr[0]
    d = c = b = a
    i = 1
    while arr[i] == a:
        i += 1
    b = arr[i]
    while arr[i] == a or arr[i] == b:
        i += 1
    c = arr[i]
    while arr[i] == a or arr[i] == b or arr[i] == c:
        i += 1
    d = arr[i]
    j = 0
    for i in range(0, len(arr)):
        if arr[i] == a:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    for i in range(0, len(arr)):
        if arr[i] == b:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    for i in range(0, len(arr)):
        if arr[i] == c:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    for i in range(0, len(arr)):
        if arr[i] == d:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1 
    return arr

  

# print(sort_special([1,2,3,4,1,2,3,4,1,2,3,4,2,1,3,4]))


# Exercise 205
def sum_of_three(arr, s):
    quick_sort(arr, 0, len(arr) - 1, False)
    for i in range(0, len(arr)):
        j = 0
        k = len(arr) - 1
        while j < k:
            if i == j:
                j += 1
            elif i == k:
                k -= 1
            elif arr[i] + arr[j] + arr[k] == s:
                return True
            elif arr[i] + arr[j] + arr[k] > s:
                 k -= 1
            else:
                j += 1
    return False  

# print(sum_of_three([1,3,8], 10))
# print(sum_of_three([1,3,8], 12))
# print(sum_of_three([8, 12, 3, 9, 1, 4], 10))

# Exercise 193
def maximal_distance(arr):
    if len(arr) < 2:
        return 0
    min = arr[0]
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return max - min 

# print(maximal_distance([1,2,3,4,5,6,7,8,9]))

# Queue
Q = [None]*100   # fixed-size array to store the elements in the queue

Front = 0        # points to the element that is in front of the queue

Back = 0         # points to the first element past the last in the
                 # queue, which is where you would enqueue the next
                 # element

def next(p):
    global Q
    p = p + 1
    if p == len(Q):
        p = 0
    return p

def is_empty():
    global Front, Back
    return Front == Back

def is_full():
    global Front, Back
    return next(Back) == Front

def enqueue(x):
    global Q, Front, Back
    if is_full():
        print('queue full')
    else:
        Q[Back] = x
        Back = next(Back)

def dequeue():
    global Q, Front, Back
    if is_empty():
        print('queue empty')
    else:
        x = Q[Front]
        Front = next(Front)
        return x



