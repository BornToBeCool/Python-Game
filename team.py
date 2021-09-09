import random

class Team:
    def __init__(self,team):
        self.alive_heroes = team #alive heroes in a list
        self.dead_heroes = [ ]  #dead heroes in a list
       
        

    # select a random heroe and apply damage to him
    def damage_heroe_taken(self, amount):
        random_heroe = random.choice(self.alive_heroes)
        random_heroe.current_health -= amount
        return random_heroe.name
        
    # select a random heroe and apply heal to him    
    def heal_heroe(self, amount):
        random_heroe = random.choice(self.alive_heroes)
        random_heroe.current_health += amount
        if random_heroe.current_health > random_heroe.max_health:
            random_heroe.current_health = random_heroe.max_health
        return random_heroe.name
        
    # select a random heroe and apply stun to him   
    def stun_heroe_taken(self, amount):
        random_heroe = random.choice(self.alive_heroes)
        random_heroe.status += amount
        return random_heroe.name
    
    # select a random heroe and apply zero damage to him   
    def miss(self, amount):
        random_heroe = random.choice(self.alive_heroes)
        return random_heroe.name
        
    #checking if any heroe is dead
    def check_heroes_health(self,):
        self.add_and_remove_heroes_from_list()

    #checking if any heroe is dead, place him to the dead list and delete him from the alive heroes
    def add_and_remove_heroes_from_list(self,):
        i = 0
        while i < len(self.alive_heroes):
            if self.alive_heroes[i].current_health <= 0:
                self.dead_heroes.append(self.alive_heroes[i])
                self.alive_heroes.remove(self.alive_heroes[i])
                i -= 1
            i += 1
            
    #checking the lowest health heroe from the team, apply heal to him and increase level by 1       
    def increase_level_heal_lowest_health_heroe(self,):
        if len(self.alive_heroes) > 0:
            lowest_health = self.alive_heroes[0]
            for heroe in self.alive_heroes:
                if heroe.current_health < lowest_health.current_health:
                    lowest_health = heroe
            lowest_health.level += 1
            lowest_health.current_health += (random.randint(5, 10)/100) * lowest_health.max_health
        

 

       













