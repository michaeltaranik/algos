class algos:
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    #print(fibonacci(10))

    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact
    #print(factorial(5))

    def unique(uniq_string):
        for j in range (0, len(uniq_string)):
            for i in range (j+1, len(uniq_string)):
                if uniq_string[i] == uniq_string[j]:
                    return False 
        return True
    #print(unique('unique'))

    def determinant(A):
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    #print(determinant([[1, 2], [3, 4]]))

    def compress_string(s):
        j = 0
        count = 1
        compressed = ""
        for i in range(1, len(s)):
            if s[i] == s[j]:
                j += 1 
                count += 1
            else:
                if count < 3:
                    compressed += s[j] * count
                    j += 1
                    count = 1
                else:
                    compressed += s[j] + str(count)
                    j += 1
                    count = 1
        if count < 3:
            compressed += s[j] * count  
        else:
            compressed += s[j] + str(count)
        return compressed
    #print(compress_string("abcdef"))             
    #print(compress_string("aabbccdd"))





