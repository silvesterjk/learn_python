from weapon import Weapon

class Hero:
    def __init__(self, health_points, attack_damage):
        self.name = 'Hero'
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equiped = False
        self.weapon: Weapon = None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equiped: # If there is a weapon and weapon is not equiped
            self.attack_damage += self.weapon.attack_increase # Increase the attack damage
            self.is_weapon_equiped = True

    def attack(self):
        print(f'{self.name} attacks with the power of {self.attack_damage}')

    # def is_alive(self):
    #     return self.health > 0

    # def __str__(self):
    #     return f'{self.name} has {self.health} health and wields a {self.weapon}'

# EXAMPLE USAGE:

# sword = Weapon('Sword', 10)
# hero = Hero('Hero', 100, sword)
# print(hero) # Hero has 100 health and wields a Sword

# axe = Weapon('Axe', 15)
# orc = Hero('Orc', 150, axe)
# print(orc) # Orc has 150 health and wields a Axe
# hero.attack(orc) # Hero attacks Orc for 10 damage!
# print(orc) # Orc has 140 health and wields a Axe
# print(orc.is_alive()) # True
# orc.attack(hero) # Orc attacks Hero for 15 damage!
# print(hero) # Hero has 85 health and wields a Sword
# print(hero.is_alive()) # True

# And so on.