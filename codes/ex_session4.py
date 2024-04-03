def find_peak(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

#print(find_peak([1,2,7,8,9]))
#print(find_peak([1,2,1,0,-3]))

def better_algo_x(n):
    if n == 0:
        return 0
    min = 1
    max = n + 1
    while min < max:
        mid = (min + max) // 2
        if mid*mid < n:
            min = mid + 1
        elif mid*mid > n:
            max = mid
        else:
            return mid
    return min - 1

#print(better_algo_x(16))
#print(better_algo_x(15))
#print(better_algo_x(2048))

def min(A):
    min = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
    return min

def max(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max

#print(min([1, 10, 20, 30, -1, 40, 50]))
#print(max([1, 10, 20, 30, -1, 40, 50]))

def palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

#print(palindrome("abba"))
#print(palindrome("ciao!"))

def lps(s):
    def find_substring(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    longest = ""
    for i in range(len(s)):
        odd = find_substring(i, i)
        even = find_substring(i, i+1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest

#print(lps("racecarlevel"))

def md(arr):
    arr_md = []
    for i in arr:
        for j in arr:
            arr_md.append(abs(i-j))
    return max(arr_md)

#print(md([1, 2, 3, 4, 5]))
#print(md([10, -3, 4, 11, 0, 9]))


def partition_even_odd(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1
    return arr

#print(partition_even_odd([-1,1,7,5,-2,1,2,7,7,5,5,1,1,4,1]))



























