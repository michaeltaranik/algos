def insort(A):
    for i in range(len(A) - 1):
        if A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]




A = [8, 6, 3, 9, 12, 4, 13]
insort(A)
print(A)