def solution(answers):
    score = { 1: 0, 2: 0, 3: 0}
    
    supoja_1 = [1, 2, 3, 4, 5]
    supoja_2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    supoja_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == supoja_1[i % 5]:
            score[1] += 1
        if answers[i] == supoja_2[i % 8]:
            score[2] += 1
        if answers[i] == supoja_3[i % 10]:
            score[3] += 1
    
    answer = []
    for stu, sco in score.items():
        if sco == max(score.values()):
            answer.append(stu)
    
    return sorted(answer)