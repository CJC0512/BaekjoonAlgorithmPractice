import numpy as np

def solution(data, col, row_begin, row_end):
    data_sorted = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    result = 0
    
    for i in range(row_begin-1, row_end):
        S_i = sum(x % (i+1) for x in data_sorted[i])
        result ^= S_i  
        
    return result