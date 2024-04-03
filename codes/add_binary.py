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
    
def reverse_string(s):
    j = len(s) - 1
    reversed = ""
    while j >= 0:
        reversed += s[j]
        j -= 1
    return reversed
#print (reverse_string("hello"))
    
def addBinary(A,B):
    c = 0
    i = 0
    if len(A) > len(B):
        B = "0" * (len(A) - len(B)) + B
    else:
        A = "0" * (len(B) - len(A)) + A
    sum = ""
    next_el = ""
    j = len(B) - 1
    while j >= 0:
        c, next_el = full_adder(A[j], B[j], c)
        sum += next_el
        j -= 1
        i += 1
    return [c] + A if c == 1 else A

print(addBinary("1011", "1101"))

