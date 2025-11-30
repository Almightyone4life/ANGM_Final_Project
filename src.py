import random
import math
import pygame

class Boss:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

    def deal_damage(self, player):
        pass
    
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

    def is_alive(self):
        print(f"Current health: {self.health}")
        return True if self.health > 0 else False