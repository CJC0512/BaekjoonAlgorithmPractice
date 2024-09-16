def solution(s):
    if len(s) not in [4, 6]:
        return False
    
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    
    return True
