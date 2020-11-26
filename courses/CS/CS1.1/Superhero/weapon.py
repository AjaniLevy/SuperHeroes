from ability import Ability
from random import randint
class Weapon(Ability):
    def attack(self):
        half_damage = self.max_damage // 2 
        randomvalue = randint(half_damage, self.max_damage)
        return randomvalue
        