import random
import math
import time
#import pygame

class Boss:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def take_damage(self, amount):
        self.health -= amount

    def deal_damage(self, amount: int):
        return amount + (random.randint(-5, 3))

    def heal_damage(self, amount: int):
        self.health += amount
    
    def is_alive(self):
        return self.health > 0
    
class Player:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def take_damage(self, amount):
        self.health -= amount

    def deal_damage(self, enemy: Boss, amount: int):
        enemy.take_damage(amount)
    
    def heal_damage(self, amount: int):
        self.health += amount

    def is_alive(self):
        #print(f"Current health: {self.health}")
        return True if self.health > 0 else False
    
player = Player("Hero", 200, "Sword")
boss = Boss("Dragon", 300, "Claws")

player_damage = 20
player_special = 40
boss_damage = 30




Phealth_msg = (f"{player.name} has {player.health} health remaining.\n")

#running = True
#while running:
 #   for event in pygame.event.get():
  #      if event.type == pygame.QUIT:
   #         running = False
    
    #player attack input
    #player.deal_damage(boss, player_damage + (random.randint(-2, 5)))


def main():
    winner = play_game()
    if winner == 0:
        tie_msg = ("The Hero and the Dragon have both slain each other.")
        for char in tie_msg:
            print(char, end='', flush=True)
            time.sleep(0.5)
    else:
        win_msg = (f"The winner is the {winner}.")
        for char in win_msg:
            print(char, end='', flush=True)
            time.sleep(0.1)

def play_game():
    round = int (1)
    intro_msg = (f"The {player.name} enters the lair to face off against the {boss.name}.\n")
    for char in intro_msg:
        print(char, end='', flush=True)
        time.sleep(0.02)
    Phealth_msg = (f"{player.name} has {player.health} health remaining.\n")
    for char in Phealth_msg:
        print(char, end='', flush=True)
        time.sleep(0.02)
    Bhealth_msg = (f"{boss.name} has {boss.health} health remaining.\n")
    for char in Bhealth_msg:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print("")
    while player.is_alive() and boss.is_alive():
        print(f"-Round {round}-")
        play_round()
        round_results()
        round += 1
    if player.is_alive():
        return player.name
    elif boss.is_alive():
        return boss.name
    else:
        return 0
    
def play_round():
    player_pick = input("Player's turn: A = Attack, S = Special, H = heal, P = Surrender\n")
    if player_pick.lower() == 'a':
        player.deal_damage(boss, player_damage + (random.randint(-2, 5)))
        #boss.take_damage(damage)
        Att_msg = (f"{player.name} attacks the {boss.name}\n")
        for char in Att_msg:
            print(char, end='', flush=True)
            time.sleep(0.03)
    elif player_pick.lower() == 's':
        Pchance = random.randint (1, 5)
        if Pchance > 2:
            player.deal_damage(boss, player_special)
            Spc_msg = (f"{player.name} uses a special attack on the {boss.name}\n")
            for char in Spc_msg:
                print(char, end='', flush=True)
                time.sleep(0.03)
        else:
            Smiss_msg = (f"{player.name}'s special attack missed.\n")
            for char in Smiss_msg:
                print(char, end='', flush=True)
                time.sleep(0.03)
        
    elif player_pick.lower() == 'h':
        player.heal_damage(25 + (random.randint(0, 15)))
        Heal_msg = (f"{player.name} tends to their wounds.\n")
        for char in Heal_msg:
            print(char, end='', flush=True)
            time.sleep(0.03)
    elif player_pick.lower() == 'p':
        player.take_damage(player.health)
        Surr_msg = (f"{player.name} has surrendered!\n")
        for char in Surr_msg:
            print(char, end='', flush=True)
            time.sleep(0.03)
        return
    
    Bturn_msg = (f"{boss.name}'s turn:\n")
    for char in Bturn_msg:
        print(char, end='', flush=True)
        time.sleep(0.03)
    chance = random.randint (1, 3)
    if boss.health > 50:
        if chance != 1:
            Bdamage = boss.deal_damage(boss_damage)
            Batt_msg =(f"{boss.name} attacks {player.name}\n")
            for char in Batt_msg:
                print(char, end='', flush=True)
                time.sleep(0.03)
            player.take_damage(Bdamage)
        else:
            Bmiss_msg = (f"{boss.name} missed their attack.\n")
            for char in Bmiss_msg:
                print(char, end='', flush=True)
                time.sleep(0.03)
    else:
        des_chance = random.randint (1, 4)
        if des_chance > 1:
            Bdamage = boss.deal_damage(boss_damage)
            Batt_msg =(f"{boss.name} attacks {player.name}\n")
            for char in Batt_msg:
                print(char, end='', flush=True)
                time.sleep(0.03)
            player.take_damage(Bdamage)
        else:
            boss.heal_damage(25 + (random.randint(0, 25)))
            Bheal_msg = (f"{boss.name} desperately heals some of its wounds.\n")
            for char in Bheal_msg:
                print(char, end='', flush=True)
                time.sleep(0.03)
    

def round_results():
    Phealth_msg = (f"{player.name} has {player.health} health remaining.\n")
    for char in Phealth_msg:
        print(char, end='', flush=True)
        time.sleep(0.03)
    Bhealth_msg = (f"{boss.name} has {boss.health} health remaining.\n")
    for char in Bhealth_msg:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print("")

if __name__ == "__main__":
    main()