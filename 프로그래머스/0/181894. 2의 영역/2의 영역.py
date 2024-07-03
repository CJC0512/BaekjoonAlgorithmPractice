def solution(arr):
    positions = [i for i, x in enumerate(arr) if x == 2]
    
    if not positions:
        return [-1]
    
    return arr[positions[0]:positions[-1] + 1]