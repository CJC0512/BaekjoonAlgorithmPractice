def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def generate_setOfnums(numbers, current, num_set):
    if current:
        num_set.add(int(current))
        
    for i in range(len(numbers)):
        generate_setOfnums(numbers[:i] + numbers[i+1:], current + numbers[i], num_set)
    
    
def solution(numbers):
    num_set = set()
    generate_setOfnums(numbers, "", num_set)
    print(num_set)
    
    count = 0
    for s in num_set:
        if is_prime(s):
            count += 1
    
    return count