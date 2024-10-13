def solution(phone_book):
    phone_hash = dict()
    
    for number in phone_book:
        phone_hash[number] = True

    for number in phone_book:
        for i in range(1, len(number)): 
            if number[:i] in phone_hash:
                return False  

    return True  