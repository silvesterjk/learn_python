class Enemy:
    def __init__(self, type_of_enemy, enemy_health=10, enemy_damage=5):
        self.__type_of_enemy: str = type_of_enemy
        self.enemy_health: int = enemy_health
        self.enemy_damage: int = enemy_damage

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. I will kill you')

    def walk(self):
        print(f'{self.__type_of_enemy} is moving towards you')
    
    def attack(self):
        print(f'{self.__type_of_enemy} will attack with the power of {self.enemy_damage}')

    def get_the_type_of_enemy(self):
        return self.__type_of_enemy
    

# SELF VS. SUPER
"""
1. We use self when we're referring to a aruguments within the different methods of a Class.
2. When inheriting form an another class we use Super()__init__ to pull data from a different class
3. 
"""

