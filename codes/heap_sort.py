def heap_sort(A):
    def heapify(A):
        start = len(A) // 2 - 1
        for i in range(start, -1, -1):
            sift_down(A, i, len(A))

    def sift_down(A, start, end):
        root = start
        while root * 2 + 1 < end:
            child = root * 2 + 1
            if child + 1 < end and A[child] < A[child + 1]:
                child += 1
            if child < end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return

    heapify(A)
    end = len(A)
    while end > 1:
        A[end - 1], A[0] = A[0], A[end - 1]
        end -= 1
        sift_down(A, 0, end)
    return A