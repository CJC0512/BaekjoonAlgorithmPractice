def solution(id_pw, db):
    user_id, user_pw = id_pw
    
    for entry in db:
        db_id, db_pw = entry
        if db_id == user_id:
            if db_pw == user_pw:
                return "login"
            else:
                return "wrong pw"
    
    return "fail"