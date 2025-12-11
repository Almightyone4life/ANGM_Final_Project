# ANGM_Final_Project
This repository is meant to be a final project for a programming class, with the hopes I can submit a working turn-based combat game in python.

In this game the player is the "Hero" who must fight the boss "Dragon". The player has 4 moves during their turn:
Attack - A key, Special - S key, Heal - H key, Surrender - P key.
Attack is a standard Garuenteed attack, Special is similar but dealing more damage at the cost of having a chance to miss (high risk, high reward), Heal simplys heals the player, and Surrender functions more like the quit but thematically it makes more sense that the player surrenders the fight.

The dragon has their own moves as well. While above 50 hp, they will simply attack the player, dealing more damage but having a base chance of missing their attack, giving the player some more breathing room. Once below 50 hp, the dragon has a low chance to heal back some hp as a last ditch effort of survival.

3 win conditions:
The hero wins - player's hp > 0 & dragon's hp =< 0
The hero wins - player's hp =< 0 & dragon's hp > 0
The hero wins - player's hp =< 0 & dragon's hp =< 0 