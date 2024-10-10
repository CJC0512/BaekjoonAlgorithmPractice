import math

def solution(arrayA, arrayB):
    gcdA = arrayA[0]
    for num in arrayA[1:]:
        gcdA = math.gcd(gcdA, num)
    
    gcdB = arrayB[0]
    for num in arrayB[1:]:
        gcdB = math.gcd(gcdB, num)
    
    def can_divide_all(gcd, array):
        for num in array:
            if num % gcd == 0:
                return False
        return True
    
    resultA = gcdA if can_divide_all(gcdA, arrayB) else 0
    resultB = gcdB if can_divide_all(gcdB, arrayA) else 0
    
    return max(resultA, resultB)