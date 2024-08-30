def solution(name, yearning, photo):
    score_dict = {}

    for i in range(len(name)):
        person = name[i]        
        score = yearning[i]      
        score_dict[person] = score 

    
    answer = []
    for p in photo:
        total_score = 0
        for person in p:
            if person in score_dict:  
                total_score += score_dict[person]
        answer.append(total_score)
    
    return answer
