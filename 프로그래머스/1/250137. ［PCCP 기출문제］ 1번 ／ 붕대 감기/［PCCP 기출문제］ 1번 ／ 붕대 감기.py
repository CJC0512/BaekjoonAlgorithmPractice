def solution(bandage, health, attacks):
    max_health = health
    time = 0
    bonus = 0
    attack_index = 0
    
    while health > 0:
        if attack_index < len(attacks) and time == attacks[attack_index][0]:
            health -= attacks[attack_index][1]
            if health <= 0:
                return -1
            attack_index += 1
            bonus = 0
        
        else:
            if health + bandage[1] > max_health:
                health = max_health
            else:
                health += bandage[1]
                
            if bonus == bandage[0]:
                if health + bandage[2] > max_health:
                    health = max_health
                else:
                    health += bandage[2]
                bonus = 0

        if time >= attacks[-1][0]:
            return health
        
        time += 1
        bonus += 1

