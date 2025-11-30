import random
import math
import pygame

class Boss:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def take_damage(self, amount):
        self.health -= amount

    def deal_damage(self, player, amount):
        player.take_damage(amount)

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
        print(f"Current health: {self.health}")
        return True if self.health > 0 else False
    
player = Player("Hero", 200, "Sword")
boss = Boss("Dragon", 300, "Claws")

player_damage = 20
boss_damage = 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #player attack input
    player.deal_damage(boss, player_damage + (random.randint(-2, 5)))