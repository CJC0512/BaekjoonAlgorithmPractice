def solution(n, words):
    # 사람 수 10 >= n >= 2
    # 순서대로 말한 단어 수 100 >= words >= n
    # 단어 길이 2이상 50이하
    # 가장 먼저 탈락하는 사람의 번호 m
    # 그 사람이 탈락하는 k번째 차례
    
    m = 1
    turn = 1
    dup_words = [words[0]]
    
    # 탈락 조건: 중복 단어, 끝말잇기X 
    for i in range(1, len(words)):        
        if m == n:
            m = 0
            turn += 1
        m += 1
        
        if words[i] in dup_words or words[i-1][-1] != words[i][0]:
            return [m, turn]
        else: 
            dup_words.append(words[i])
            
    return [0,0]