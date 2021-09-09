import random
from game import *
from team import *

class Heroes:
    
    def __init__(self,heroes_list):
        self.name = heroes_list[0]
        self.base_health = heroes_list[1]
        self.max_health = heroes_list[2]
        self.current_health = heroes_list[3]
        self.min_damage = heroes_list[4]
        self.max_damage = heroes_list[5]
        self.category = heroes_list[6]
        self.level = heroes_list[7]
        self.stun_seconds = heroes_list[8]
        self.heal_amount = heroes_list[9]
        self.spell_damage = heroes_list[10]
        self.status = heroes_list[11]

    # returns a value of self.stun_heal_spell_attack()
    def heal_or_damage_or_stun(self,):
        return self.stun_heal_spell_attack()
            
    # returns a value between self.min_damage and self.max_damage
    def attack(self):
        attack_damage = random.randrange(10 * self.level + self.min_damage, 10 * self.level + self.max_damage)
        return attack_damage
   
    # returns a value of self.spell_damage based on level
    def spell(self,):
        return self.spell_damage + (self.spell_damage * 0.1 * self.level)
    
    # returns a tuple of name and value
    def stun_heal_spell_attack(self):
        heroe_dict = {"stun" : self.stun_seconds,
                   "heal" : self.heal_amount,
                   "spell": self.spell(),
                   "attack": self.attack()
                   }
        my_dict = {}
        for key, value in heroe_dict.items():
            if value == 0:
                pass
            else:
                my_dict[key] = value
        my_dict["none"] = 0
        random_choice = random.choice(list(my_dict.items()))
        return random_choice
        
    # increase the level of the lowest health heroe and heals him as well by 5-10 percent of his max_health
    def increase_level(self):
        self.level += 1
        self.max_health += + (self.base_health * 0.1 * self.level)
        self.current_health += (self.base_health * 0.1 * self.level)
        
    #  returns the status of the heroe    
    def set_status(self,):
        if self.status > 0:
            return "stunned"
        else:
            return "OK"
            

        




