import random
import math
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

    def heal_damage(self, amount):
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
boss_damage = 20

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
        print("The Hero and the Dragon have both slain each other.")
    else:
        print(f"The winner is the {winner}.")

def play_game():
    round = int (1)
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
    player_pick = input("Player's turn: A = Attack, H = heal\n")
    if player_pick.lower() == 'a':
        damage = player.deal_damage(boss, player_damage + (random.randint(-2, 5)))
        #boss.take_damage(damage)
        print(f"{player.name} attacks the {boss.name}")
    elif player_pick.lower() == 'h':
        player.heal_damage(20 + (random.randint(1, 5)))
    
    print(f"{boss.name}'s turn:")
    Bdamage = boss.deal_damage(boss_damage)
    print(f"{boss.name} attacks {player.name}")
    player.take_damage(Bdamage)
    

def round_results():
    print(f"{player.name} has {player.health} health remaining.")
    print(f"{boss.name} has {boss.health} health remaining.")

if __name__ == "__main__":
    main()