def solution(A, B):
    if len(A) != len(B):
        return -1
    
    if A == B:
        return 0

    for i in range(len(A)):
        shifted_A = A[-1] + A[:-1]
        if shifted_A == B:
            return i + 1
        A = shifted_A
    
    return -1