def solution(myString, pat):
    myString_lower = myString.lower()
    pat_lower = pat.lower()
    
    if pat_lower in myString_lower:
        return 1
    else:
        return 0
