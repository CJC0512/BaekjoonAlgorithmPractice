def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        sorted_array = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(sorted_array[commands[i][2]-1])

    return answer