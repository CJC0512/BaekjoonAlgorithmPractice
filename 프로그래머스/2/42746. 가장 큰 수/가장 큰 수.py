def solution(numbers):
    str_num = list(map(str, numbers))
    sorted_numbers = sorted(str_num, key=lambda x : x * 4, reverse=True)
    
    answer = ''.join(sorted_numbers)
    
    return answer if int(answer) != 0 else '0'