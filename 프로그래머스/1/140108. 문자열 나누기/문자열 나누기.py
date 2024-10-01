def solution(s):
    answer = 0 
    i = 0 
    
    while i < len(s): 
        x = s[i] 
        x_count = 1  
        other_count = 0  
        i += 1
        
        # x와 다른 글자들의 개수를 세면서 비교
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            i += 1
            
            # x의 개수와 x가 아닌 글자의 개수가 같아지면 분리
            if x_count == other_count:
                break
        
        # 분리된 문자열의 개수를 증가
        answer += 1
    
    return answer
