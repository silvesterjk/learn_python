from zombie import *
from orge import *

def battle(e1: Enemy, e2: Enemy):   
    e1.talk()
    e2.talk()

    print(f'{e1.get_the_type_of_enemy()} health: {e1.enemy_health}')
    print(f'{e2.get_the_type_of_enemy()} health: {e2.enemy_health}')

    while e1.enemy_health > 0 and e2.enemy_health > 0:
        print("----------------------")
        e1.special_attack()
        e2.special_attack()
        e1.enemy_health -= e2.enemy_damage # e1 is attacking e2 and that is why e2's health is decreasing
        e2.enemy_health -= e1.enemy_damage # e2 is attacking e1 and that is why e1's health is decreasing
        print(f'{e1.get_the_type_of_enemy()} health: {e1.enemy_health}')
        print(f'{e2.get_the_type_of_enemy()} health: {e2.enemy_health}')
    
    print("----------------------")
    if e1.enemy_health > 0:
        print(f'{e1.get_the_type_of_enemy()} has won!')
    else:
        print(f'{e2.get_the_type_of_enemy()} has won!')

zombie = Zombie(30, 10)
orge = Orge(50, 20)

battle(zombie, orge)