class Enemy:
    def __init__(self, type_of_enemy, enemy_health=10, enemy_damage=5):
        self.type_of_enemy: str = type_of_enemy
        self.enemy_health: int = enemy_health
        self.enemy_damage: int = enemy_damage

    def talk(self):
        print(f'I am a {self.type_of_enemy}. I will kill you')

    def walk(self):
        print(f'{self.type_of_enemy} is moving towards you')
    
    def attack(self):
        print(f'{self.type_of_enemy} will attack with the power of {self.enemy_damage}')