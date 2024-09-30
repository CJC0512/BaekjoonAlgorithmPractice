def count_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:  # 제곱수가 아닌 경우
                count += 1
    return count

def solution(number, limit, power):
    total_weight = 0
    
    for i in range(1, number + 1):
        divisors_count = count_divisors(i)
        if divisors_count > limit:
            total_weight += power
        else:
            total_weight += divisors_count
    
    return total_weight