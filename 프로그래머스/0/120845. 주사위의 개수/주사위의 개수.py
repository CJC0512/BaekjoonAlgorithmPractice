def solution(box, n):
    num_in_width = box[0] // n
    num_in_height = box[1] // n
    num_in_depth = box[2] // n
    
    answer = num_in_width * num_in_height * num_in_depth
    
    return answer