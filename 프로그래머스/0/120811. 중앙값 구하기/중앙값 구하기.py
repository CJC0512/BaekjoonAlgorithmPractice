def solution(array):
    array.sort()
    middle_index = len(array) // 2
    
    return array[middle_index]
