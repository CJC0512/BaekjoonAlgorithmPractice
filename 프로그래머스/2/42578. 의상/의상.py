def solution(clothes):
    answer = 1
    type = {clo[1] for clo in clothes}    
    dress = {}
    for key in type:
        dress[key] = []
    
    for clo in clothes:
        dress[clo[1]].append(clo[0])
        
    for key in type:
        answer *= len(dress[key]) + 1
    
    print(dress)
    return answer - 1