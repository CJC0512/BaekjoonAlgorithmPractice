def solution(dots):
    answer = 0
    
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            for k in range(len(dots)):
                if k != i and k != j:
                    for l in range(k+1, len(dots)):
                        if l != i and l != j:
                            slope1 = (dots[j][1] - dots[i][1]) / (dots[j][0] - dots[i][0]) if dots[j][0] - dots[i][0] != 0 else float('inf')
                            slope2 = (dots[l][1] - dots[k][1]) / (dots[l][0] - dots[k][0]) if dots[l][0] - dots[k][0] != 0 else float('inf')
                            
                            if slope1 == slope2:
                                answer = 1
                                return answer
    
    return answer