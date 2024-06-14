def solution(hp):
    general = hp // 5
    remaining_hp = hp % 5
    
    soldier = remaining_hp // 3
    remaining_hp = remaining_hp % 3
    
    worker = remaining_hp
    
    return general + soldier + worker