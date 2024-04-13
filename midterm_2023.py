# Exercise 1
def partition(arr, begin, end, decreasing):
    j = begin - 1
    pivot = arr[end]
    for i in range(begin, end):
        if decreasing:
            if arr[i] >= pivot:
                j +=1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[i] <= pivot:
                j +=1
                arr[i], arr[j] = arr[j], arr[i]
    arr[end], arr[j + 1] = arr[j + 1], arr[end]
    return j + 1

def quick_sort(arr, begin, end, decreasing):
    if begin < end:
        pivot_index = partition(arr, begin, end, decreasing)
        quick_sort(arr, begin, pivot_index - 1, decreasing)
        quick_sort(arr, pivot_index + 1, end, decreasing)
    return arr


def mountain_sort(arr):
    quick_sort(arr, 0, len(arr) // 2 - 1, False)
    quick_sort(arr, len(arr) // 2, len(arr) - 1, True)
    return arr


A = [8, 2, 5, -12, 2, 11, -15, -8, -1, 12]
# print(quick_sort(A, 0, len(A) - 1), False)
# print(mountain_sort(A))



# Exercise 2
# Question 1:
# Algo_x returns number of original elements in the array, i.e. elements
# that we can encounter only once 
# arr = [1,2,3,4,4,4], x = 3 (1,2,3 = x, 4 has copies)
# Question 2:
# comlexity of the algorithm is quadratic, there is also a difference 
# between best-case and worst-case scenario, namely best-case is when 
# all elements of the array are the same, in this case complexity is linear
# because in principle while-loop is not being used.
# Worst-case, on the other hand, is when all elements are unique,
# then while-loop is going through the whole cycle, thus complexity is quadratic.

def better_algo_x(arr):
    quick_sort(arr, 0, len(arr) - 1, False)
    count = 0
    for i in range(0, len(arr)):
        if (i == 0 or arr[i - 1] != arr[i]) and (i == len(arr) - 1 or arr[i + 1] != arr[i]):
            count += 1
    return count

# print(better_algo_x([5,1,2,3,2,3,10,0]))

# Exercise 3:
# Question 1:
# algo_y returns the biggest amount of revenue within a period of 10 days
# complexity of this algo is always quadratic because there are 2 for-loops,
# that you cannot exit before they are finished, there is no difference
# between best- and worst-case scenario
class Transaction:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

def print_all_transactions(arr_of_trans):
    i = 0
    while i < len(arr_of_trans):
        print(arr_of_trans[i].date, arr_of_trans[i].amount)
        i += 1


def partition_trans(arr, begin, end):
    j = begin - 1
    pivot = arr[end].date
    for i in range(begin, end):
        if arr[i].date <= pivot:
            j +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[end], arr[j + 1] = arr[j + 1], arr[end]
    return j + 1

def quick_sort_trans(arr, begin, end):
    if begin < end:
        pivot_index = partition_trans(arr, begin, end)
        quick_sort_trans(arr, begin, pivot_index - 1)
        quick_sort_trans(arr, pivot_index + 1, end)
    return arr


def better_algo_y(trans):
    quick_sort_trans(trans, 0, len(trans) - 1)
    i = 0
    j = 0
    current = 0
    max = current
    while i < len(trans):
        if trans[i].date - trans[j].date <= 10:
            current = current + trans[i].amount
            i += 1
            if current > max:
                max = current
        else:
            current = current - trans[j].amount
            j += 1
    return max

accounting_system = [Transaction(12, 100),
                     Transaction(23, 450),
                     Transaction(10, 300), 
                     Transaction(15, 900),
                     Transaction(30, 1000),
                     Transaction(34, 200),
                     Transaction(1, 100)]

# print_all_transactions(quick_sort_trans(accounting_system, 0, len(accounting_system) - 1))
# print(better_algo_y(accounting_system))



# Exercise 5:
def square_root(n):
    low = 0
    high = n + 1
    middle = (low + high) //2

    while low + 1 < high:
        middle = (low + high) // 2

        if middle * middle < n:
            low = middle
            
        elif middle * middle > n:
            high = middle

        else:
            return middle
        
    if middle * middle > n:
        return middle - 1
    else:
        return middle


def check_square_root(arr):
    i = 0
    while i < len(arr):
        print(square_root(arr[i]))
        i += 1

square_roots = [0, 1, 2, 3, 9, 10, 11, 25]
check_square_root(square_roots)


# Exercise 4:















