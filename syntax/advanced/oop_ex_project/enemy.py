class Enemy():
    type_of_enemy: str
    enemy_health: int = 100
    enemy_damage: int = 10

    def talk(self):
        print(f'I am a {self.type_of_enemy}. I will kill you')

    def walk(self):
        print(f'{self.type_of_enemy} is moving towards you')
    
    def attack(self):
        print(f'{self.type_of_enemy} will attack with the power of {self.enemy_damage}')