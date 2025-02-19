from zombie import *
from orge import *
from hero import *

# def battle(e1: Enemy, e2: Enemy):   
#     e1.talk()
#     e2.talk()

#     print(f'{e1.get_the_type_of_enemy()} health: {e1.enemy_health}')
#     print(f'{e2.get_the_type_of_enemy()} health: {e2.enemy_health}')

#     while e1.enemy_health > 0 and e2.enemy_health > 0:
#         print("----------------------")
#         e1.special_attack()
#         e2.special_attack()
#         e1.enemy_health -= e2.enemy_damage # e1 is attacking e2 and that is why e2's health is decreasing
#         e2.enemy_health -= e1.enemy_damage # e2 is attacking e1 and that is why e1's health is decreasing
#         print(f'{e1.get_the_type_of_enemy()} health: {e1.enemy_health}')
#         print(f'{e2.get_the_type_of_enemy()} health: {e2.enemy_health}')
    
#     print("----------------------")
#     if e1.enemy_health > 0:
#         print(f'{e1.get_the_type_of_enemy()} has won!')
#     else:
#         print(f'{e2.get_the_type_of_enemy()} has won!')


def hero_battle(hero: Hero, enemy: Enemy):   

    print(f"Hero's health: {hero.health_points}")
    print(f"{enemy.get_the_type_of_enemy()}'s health: {enemy.enemy_health}")

    while hero.health_points > 0 and enemy.enemy_health > 0:
        print("----------------------")
        enemy.special_attack()
        hero.health_points -= enemy.enemy_damage
        print(f"Hero's health: {hero.health_points}")
        hero.attack()
        enemy.enemy_health -= hero.attack_damage
        print(f"{enemy.get_the_type_of_enemy()}'s health: {enemy.enemy_health}")
    
    print("----------------------")
    if hero.health_points > 0:
        print('The hero wins!')
    else:
        print(f'{enemy.get_the_type_of_enemy()} has won!')

zombie = Zombie(30, 1)
orge = Orge(30, 1)

# battle(zombie, orge)

hero = Hero(30, 1)

weapon = Weapon('Sword', 50)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, orge)
