def array_remove_pos(A,i):
    A[i] = A[len(A) - 1]
    A.pop()
    return A

A = [7, 5, 2, 3, 5, 7, 3, 4, 2, 1]
#print(len(A))
#array_remove_pos(A,7)
#print(A)

def array_remove_value(A,x):
    array_remove_value_stable(A,x)

def array_remove_value_stable(A,x):
    i = 0
    j = 0
    while i < len(A):
        if A[i] != x:
            A[j] = A[i]
            j += 1
        i += 1
    for k in range(i - j):
       A.pop()


#A = [0, 5, 2, 3, 5, 0, 3, 4, 2, 1]
#print(A)
#print(len(A))
#array_remove_value_stable(A,7)
#print(len(A))
#print(A)