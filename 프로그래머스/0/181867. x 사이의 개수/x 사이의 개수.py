def solution(myString):
    split_strings = myString.split('x')
    lengths = [len(part) for part in split_strings]
    
    return lengths
