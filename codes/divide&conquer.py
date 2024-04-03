def binary_search(A, x):
    l = 0
    r = len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] == x:
            return True
        elif l == r:
            return False
        elif A[m] < x:
            l = m + 1
        else:
            r = m
    return False

#print(binary_search([1,2,3,4,5,6,7,8,9,10], 11))









