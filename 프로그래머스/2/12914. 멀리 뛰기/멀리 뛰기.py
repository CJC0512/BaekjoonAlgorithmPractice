def solution(n):
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2 
    
    for i in range(3, n + 1):
        current = (prev1 + prev2) % 1234567 
        prev2, prev1 = prev1, current 
    
    return current