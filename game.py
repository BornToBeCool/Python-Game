import random
from heroes import *
from team import *


class Game:
    def __init__(self,):
        self.teams = []
        self.round = 0

    #read the CSV file line by line and save the data
    def load_heroes_from_file(self,):
        f = open("heroes.csv", "r")
        file = f.readlines()
        f.close()

    #for loop that split every line by coma    
        heroes_list_str = []
        for line in file:
            heroes_list_str.append(line.split(","))

    #for loop that deletes all the spaces from every element 
        heroes_list_str_striped = []
        for heroe_list in heroes_list_str:
            heroe_striped = []
            for heroe in heroe_list:
                element = heroe.strip()
                heroe_striped.append(element)
            heroes_list_str_striped.append(heroe_striped)
            
    #for loop that changes string numberics into ingeters (Only numerics)
        list_converted = []
        for heroe_list in heroes_list_str_striped:
            heroe_converted = heroe_list
            heroe_converted = [int(x) if x.isdigit() else x for x in heroe_converted]
            list_converted.append(heroe_converted)
        return list_converted
    
    # asking from the user the game mode
    def AP_or_AR(self,):
        print("Welcome to DOTA: \n")
        mode_selection = input("Type 1 for AP mode: " + "Type 2 for AR mode: \n")
        while mode_selection != "1" and mode_selection != "2":
            print(" ")
            print("You have not selected the right number. Try again: \n")
            mode_selection = input("Type 1 for AP mode: " + "Type 2 for AR mode: \n")
        if mode_selection == "1":
            self.AP_mode()
        else:
            self.AR_mode()
        
    # picking 10 random heroes/elements and returns them   
    def random_heroes(self,):
        all_heroes = self.load_heroes_from_file()        
        random_heroes = []
        for i in range(10):
            random_choice = random.choice(all_heroes)
            random_heroes.append(random_choice)
            all_heroes.remove(random_choice)
        return random_heroes 
            
    #create heroes and place then randomly in to teams     
    def AR_mode(self,):
        random_heroes = self.random_heroes()
        random.shuffle(random_heroes)
        teamA = []
        teamB = []
        for i in random_heroes:
            if len(teamA) < 5:
                teamA.append(Heroes(i))
            else:
                teamB.append(Heroes(i))
       
        self.teams.append(Team(teamA))
        self.teams.append(Team(teamB))
        
    #asking from the user to pick heroes then create them and the place them into teams. team1 first then team2
    def AP_mode(self,):
        random_heroes = self.random_heroes()
        list_heroe_names = []
        for i in random_heroes:
            list_heroe_names.append(i[0])
            
        numeric_list_heroe_names = []
        counter = 1
        numeric_list_heroe_names.append("Type: ")
        for i in list_heroe_names:
            numeric_heroe = str(counter) + " for " + i
            numeric_list_heroe_names.append(numeric_heroe)
            counter += 1
        print("AP mode selected: \n")
        print(numeric_list_heroe_names)
        
        teamA = []
        teamB = []
        
        counter = 0
        while counter < 10:
            user_choice = int(input("Select one of the above heroes: \n"))
            if user_choice < 1 or user_choice > 10:
                print("You have not selected the right number. Try again: \n")
                user_choice = int(input("Select one of the above heroes: "))
            if len(teamA) < 5:
                teamA.append(Heroes(random_heroes[user_choice - 1]))
            else:
                teamB.append(Heroes(random_heroes[user_choice - 1]))
            counter += 1
            
        self.teams.append(Team(teamA))
        self.teams.append(Team(teamB))
        
    
    #calculate and applydamage one team to the other
    def calculate_and_apply_damages(self,):
        teamA = self.teams[0]
        teamB = self.teams[1]

        self.calculate_damages(teamA, teamB, "TeamA")
        self.calculate_damages(teamB, teamA, "TeamB")
        
        teamA.increase_level_heal_lowest_health_heroe()
        teamB.increase_level_heal_lowest_health_heroe()

    #calculate and applydamage one team to the other
    def calculate_damages(self, teamA , teamB, x):
        team_damages = []
        
        for heroe in teamA.alive_heroes:
            if heroe.set_status() == "OK":
                heroe_damage_amount = heroe.heal_or_damage_or_stun()
                if heroe_damage_amount[0] == "heal":
                    nameA = teamA.heal_heroe(heroe_damage_amount[1])
                    team_damages.append(heroe.name + " - " + str( heroe_damage_amount[1]) + "  "  + str( heroe_damage_amount[0]) + "  --> " + nameA)
                elif heroe_damage_amount[0] == "stun":
                    nameA = teamB.stun_heroe_taken(heroe_damage_amount[1])
                    team_damages.append(heroe.name + " - " + str( heroe_damage_amount[1]) + "  "  + str( heroe_damage_amount[0]) + "  --> " + nameA)
                elif heroe_damage_amount[0] == "spell" or heroe_damage_amount[0] == "attack":
                    nameA = teamB.damage_heroe_taken(heroe_damage_amount[1])
                    team_damages.append(heroe.name + " - " + str( heroe_damage_amount[1]) + "  "  + str( heroe_damage_amount[0]) + "  --> " + nameA)
                else: #heroe_damage_amount[0] == "none":
                    nameA = teamB.miss(heroe_damage_amount[1])
                    team_damages.append(heroe.name + " - " + str( heroe_damage_amount[1]) + "  "  + str( heroe_damage_amount[0]) + "  --> " + nameA)
            else:
                heroe.status -= 1     
        self.show_damages(team_damages,x)       
        teamA.add_and_remove_heroes_from_list()
        teamB.add_and_remove_heroes_from_list()  

    #print non stunned heroes damages
    def show_damages(self, my_list, team):
        print(team + " Damages")
        print(" ")
        for i in my_list:
            print(i)
        print(" ")
 
    #print heroes name, max_health, level and status  
    def printHeroes(self,):
        for team in self.teams:
            if team == self.teams[0]:
                print("TeamA")
                print(" ")
            else:
                print("TeamB")
                print(" ")
            for heroe in team.alive_heroes:
                print(heroe.name,  " " , end="")
                print(heroe.current_health,  " " , end="")
                print(heroe.level, " " , end="")
                print(heroe.set_status())
            print(" ")
            print(" ")
       
    #increase self.round by 1
    def game_round(self,):
        self.round += 1
        return self.round