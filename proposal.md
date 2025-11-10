# Title - A Totally Simple Fight.

## Description: 
This repository is meant to be a final project for a programming class, with the hopes that I can submit a working turn-based combat game in Python. 

### Features:
At least 2 button prompts for Attacking and Healing for the player.
A dynamic opponent that'll use different attacks/abilities depending on either their own or the player's hp
Attacks and Healing use a random range amount, with some attacks having a chance to miss.
(potentially) An ally to fight alongside the player.
PNGS/JPGs that change depending on the attacks/abilities used.

### Challenges:
Having a variety of attacks and abilities that would make multiple playthroughs feel less stale, that also work properly.
Making the PNGs/JPGs *animate* properly (i.e., switch from default, to action, then back to default)
Making a HUD system that displays and updates the player's and the enemy's HP, and shows the name of the attack/ability used each turn.
(Potentially) The Ally AI is working properly while also being useful.

### Outcomes:
  Ideal Outcome - Ideally, the turn-based combat will work smoothly and feel similar to the combat from the game "Darkest Dungeon 2", which is where I get my inspiration from.
  Miniable Viable Outcome - The player can have a simple 1v1, turn-based combat with 2 different attacks (one guaranteed low damage, one high damage with a chance to miss) 
  and the ability to heal themselves, with the same thing for the enemy. Instead of images, numbers representing the player's and the enemy's HP that change after an action.

### Milestones
Goal 1: Make the player and enemy stat sheet (i.e, HP, Attack amount, heal amount), and making it so they can be changed with an action.
Goal 2: make a functioning round, where the player can make an imput for their turn, and then the enemy makes their turn. This repeats as long as either's HP > 0.
Goal 3: A display system with at least working action icons/buttons (attack and heal), and displaying/updating HP
Goal 4 (if have time): Ally AI, and *animations* for player and enemy.
