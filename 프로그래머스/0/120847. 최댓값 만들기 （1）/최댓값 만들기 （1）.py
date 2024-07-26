def solution(numbers):
    numbers.sort()
    
    max1 = numbers[-1]
    max2 = numbers[-2]
    
    answer = max1 * max2
    
    return answer