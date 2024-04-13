import random


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

        

A = [1,2,1,2,1,2,1,2,3,0]
B = [9,8,6,3,8,0,1,2,4,2]

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



        
