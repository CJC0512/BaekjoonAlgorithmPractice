while(1):
    user_input = list(input())
    
    if user_input[0] == '0':
        break
    
    length = len(user_input)
    i = 0
    while(1):
        if user_input[i] != user_input[length - 1 - i]:
            print('no')
            break
        
        if i >= int(length/2):
            print('yes')
            break
        
        i += 1