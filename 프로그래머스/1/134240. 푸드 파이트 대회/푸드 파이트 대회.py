def solution(food):
    answer = ''
    
    for i in range(1, len(food)):  # 0번 음식은 물이므로 제외
        answer += str(i) * (food[i] // 2)
    
    answer += '0'
    
    # 대칭을 위해 앞에서 쌓은 음식을 뒤집어서 붙이기
    answer += answer[:-1][::-1]
    
    return answer
