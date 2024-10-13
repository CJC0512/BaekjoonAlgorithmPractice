def solution(participant, completion):
    answer = ''
    map = dict()
    
    for ptcp in participant:
        map[ptcp] = 0
        
    for ptcp in participant:
        map[ptcp] += -1
    
    for com in completion:
        map[com] += 1
    
    for key in map:
        if map[key] != 0:
            answer = key
    
    return answer