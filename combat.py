from player import *
from gameparser import *

#PhD student roughly do 20 damage
#You'll need at least 150 health to fight Kirill
playerAttack = {"punch": [True, range(3, 7)], "kick": [True, range(10, 15)], "headbutt": [True, range(20, 30)]}
enemyAttack = {"punch": [True, range(3, 7)], "kick": [True, range(10, 15)], "headbutt": [True, range(20, 30)]}
def begin_combat(player_health, enemy_health):
	print("Your foe has " + str(enemy_health) + " and you have " + str(player_health) + " health.")
	print()
	print("Do you want to...")
	print("PUNCH")
	if playerAttack["kick"] == True:
		print("KICK")
	if playerAttack["headbutt"] == True:
		print("HEADBUTT")

	player_input = (input("> "))

	if is_valid_attack(player_input) == True:
		pass

def is_valid_attack(attack):
	for key in playerAttack:
		if attack == key:
			if playerAttack[key] == True:
				return True
			else:
				return False