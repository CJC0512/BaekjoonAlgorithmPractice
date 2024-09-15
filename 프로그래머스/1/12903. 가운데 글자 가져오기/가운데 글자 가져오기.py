def solution(s):
    length = len(s)
    mid = length // 2 
    
    if length % 2 == 0:
        answer = s[mid-1:mid+1]
    else:
        answer = s[mid]
    
    return answer