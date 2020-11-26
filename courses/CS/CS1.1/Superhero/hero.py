from random import choice
from ability import Ability
from armor import Armor
from weapon import Weapon
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.damage = 0
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return "This match was a lame DRAW"
        """Challengee goes first"""
        while self.current_health > 0 and opponent.current_health > 0: 
            heromove = self.attack()
            opponentmove = opponent.attack()
            self.take_damage(opponentmove)
            opponent.take_damage(heromove)
        if self.current_health > 0:
            return f"{self.name} wins!!"
        else:
            return f"{opponent.name} wins!!"
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    def add_armor(self, armor):
        self.armors.append(armor)
    def defend(self, damage):
        Damage_taken = 0
        total_damage_protection = 0
        if self.current_health != 0:
            if len(self.armors) != 0:
                for armor in self.armors:
                    total_damage_protection += armor.block()
        if total_damage_protection < damage:
            Damage_taken = damage - total_damage_protection
        return Damage_taken
        
    def take_damage(self,damage):
        DT = self.defend(damage)
        self.current_health -= DT

    def is_alive(self):
        if self.current_health == 0 or self.current_health < 0:
            return False
        else:
            return True
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())