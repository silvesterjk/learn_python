from enemy import Enemy
import random

class Orge(Enemy): # Orge is a child class of Enemy
    def __init__(self, enemy_health, enemy_damage):
        super().__init__(type_of_enemy='Orge', 
                         enemy_health=enemy_health, 
                         enemy_damage=enemy_damage)
        self.undead = True

    def talk(self):
        return "*Growling....*"
    
    def attack(self): # Method overriding
        print(f'{self.get_the_type_of_enemy()} will attack with the power of {self.enemy_damage}')
        print(f'{self.talk()}')

    def spread_bad_smell(self): # New method
        print(f'{self.get_the_type_of_enemy()} is spreading bad smell!')

    def special_attack(self):
        did_sattack_work = random.random() < 0.2 # 20% chance of True
        if did_sattack_work:
            print(f'{self.get_the_type_of_enemy()} has successfully infected you!')
            self.enemy_health += 20 
            print(f"Zombie's health is now {self.enemy_health}")
        else:
            print(f'{self.get_the_type_of_enemy()} tried to infect you but failed!')