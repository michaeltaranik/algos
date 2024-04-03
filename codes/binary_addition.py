def full_adder(a,b,c):
    #return (carry, sum)
    if a == b == c == 1:
        return (1,1)
    elif a == b == 1 or a == c == 1 or b == c == 1:
        return (1,0)
    elif a == b == c == 0:
        return (0,0)
    else:
        return (0,1)
    
def binary_addition(A,B):
    c = 0
    if len(A) > len(B):
        B = [0] * (len(A) - len(B)) + B
    else:
        A = [0] * (len(B) - len(A)) + A
    j = len(B) - 1
    while j >= 0:
        c, A[j] = full_adder(A[j], B[j], c)
        j -= 1
    return [c] + A if c == 1 else A


#print(binary_addition([1,0,1,1],[1,1,0,1])) 
#print(binary_addition([1,0,1,1,1],[1,1,0,0]))
#print(binary_addition([1,1,1,1,1,1,1,1,1,1], [1]))
#print(binary_addition([1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]))
#print(binary_addition([1], [1]))

def max_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

#print (max_three(1,2,3))
#print (max_three(2,1,3))
# print (max_three(0, 1, 0))