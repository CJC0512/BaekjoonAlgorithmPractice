def solution(x):
    answer = True
    x_list = list(str(x))
    x_len = len(x_list)
    x_sum = 0
    for i in range(x_len):
        x_sum += int(x_list[i])
        
    if x % x_sum != 0:
        answer = False
                  
    
    return answer