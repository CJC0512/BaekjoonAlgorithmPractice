def solution(elements):
    n = len(elements)
    unique_sums = set() 

    for start in range(n):
        current_sum = 0
        
        for length in range(1, n + 1): 
            current_sum += elements[(start + length - 1) % n]  
            unique_sums.add(current_sum)  

    return len(unique_sums) 
