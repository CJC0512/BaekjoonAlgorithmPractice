def solution(myString, pat):
    converted_string = ''.join('B' if char == 'A' else 'A' for char in myString)
    
    return 1 if pat in converted_string else 0
