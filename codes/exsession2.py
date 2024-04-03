class exercise_session_2:
    def count_lower(A,x):
        j = 0
        for i in range (0, len(A)):
            if A[i] < x:
                j = j + 1
        return j
    #print(count_lower([3, 2, 1, 1, 3, 2, 2, 3, 1], 10))

    def leap_year(y):
        if y % 400 == 0:
            return True
        if y % 100 == 0:
            return False
        if y % 4 == 0:
            return True
        else:
            return False
    #print(leap_year(2201))    
    
    def multiples_of_three(A):
        j = 0
        for i in A:
            if i % 3 == 0 and i != 0:
                j = j + 1
        return j
    #print(multiples_of_three([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]))
    #print(multiples_of_three([7, 2, 0]))

    def check_sorted(A):
        j = 0
        for i in range (1, len(A)):
            if A[j] <= A[i]:
                j = j + 1
            else:
                return False
        return True
    #print(check_sorted([43,51,50,51,70]))
    #print(check_sorted([50,50,50]))
    #print(check_sorted([1,2,3]))

    def find_peak(A):
        j = 0
        for i in range (1, len(A)):
            if A[j] <= A[i]:
                j = j + 1
            else:
                return A[j]
        return A[j]
    #print(find_peak([1,2,7,8,9]))
    #print(find_peak([1,2,3,2,1]))
    #print(find_peak([4,7,4]))
    #print(find_peak([7,4]))

    def partition_even_odd(A):
        j = 0
        for i in range (1, len(A)):
            if A[i] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                j = j + 1

    arr = [-1,1,7,5,-2,1,2,7,7,5,5,1,1,4,1]
    partition_even_odd(arr)
    #print(arr)

    arr1 = [-1,1,2,4,5,8,9,4,10,13]
    partition_even_odd(arr1)
    #print(arr1)

    def addTwoNumbers(self, 
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        l3 = [0] * max(l1, l2)
        inc = 0
        for i in range (0, len(l3)):
            if l1[i] + l2[i] >= 10 :
                l3 = l1[i] + l2[i] - 10 + inc
                inc = 1
            else :
                l3 = l1[i] + l2[i] + inc
                inc = 0
        
                

    






