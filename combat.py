from player import *
from gameparser import *
from game import *

import random

#PhD student roughly do 20 damage
#You'll need at least 150 health to fight Kirill
playerAttack = {"punch": [True, 3, 7, 0], "kick": [True, 10, 15, 0], "headbutt": [True, 20, 30, 0]}
enemyAttack = {"punch": [True, 3, 7, 0], "kick": [True, 10, 15, 0], "headbutt": [True, 20, 30, 0]}


def begin_combat(player_health, enemy_health, enemy_name):
	playerAttack = {"punch": [True, 3, 7, 0], "kick": [True, 10, 15, 0], "headbutt": [True, 20, 30, 0]}
	enemyAttack = {"punch": [True, 3, 7, 0], "kick": [True, 10, 15, 0], "headbutt": [True, 20, 30, 0]}
	while (player_health > 0) and (enemy_health > 0):
		print()
		print("An angry " + enemy_name + " is about to attack you!")
		print(enemy_name + " has " + str(enemy_health) + " and you have " + str(player_health) + " health.")
		print()
		print("Do you want to...")
		print("PUNCH")
		if playerAttack["kick"][0] == True:
			print("KICK")
		if playerAttack["headbutt"][0] == True:
			print("HEADBUTT")

		player_input = str(normalise_input(input("> ")))[2:-2] #normailse_input returns a list of normailsed words, this is converted into a string and the list structure is removed
		
		if is_valid_attack(player_input) == True:
			print()
			playerAttackDamage = random.randrange(playerAttack[player_input][1], playerAttack[player_input][2])
			print("You " + player_input + "ed " + enemy_name + " and did " + str(playerAttackDamage) + " damage to them!")
			enemy_health = enemy_health - playerAttackDamage

			if player_input == "headbutt":
				player_health = player_health - int(playerAttackDamage / 2)

			if enemy_health > 0:
				enemy_input = enemy_attack(enemy_health) # Enemy health needed so the enemy doesn't kill itself by headbutting the player!
				enemyAttackDamage = random.randrange(enemyAttack[enemy_input][1], enemyAttack[enemy_input][2])
				print(enemy_name + " " + enemy_input + "ed you and did " + str(enemyAttackDamage) + " damage to you!")
				player_health = player_health - enemyAttackDamage

				if enemy_input == "headbutt":
					enemy_health = enemy_health - int(enemyAttackDamage / 2)

			playerAttack[player_input][0] = False
			playerAttack[player_input][3] = 0

			playerAttack["punch"][3] += 1
			playerAttack["kick"][3] += 1
			playerAttack["headbutt"][3] += 1

			if playerAttack["punch"][3] == 1:
				playerAttack["punch"][0] = True
			if playerAttack["kick"][3] == 2:
				playerAttack["kick"][0] = True
			if playerAttack["headbutt"][3] == 3:
				playerAttack["headbutt"][0] = True

		else:
			print("That is not a valid attack.")

	if player_health <= 0:
		print("Oh no, " + enemy_name + " " + enemy_input + "ed you so hard you died")
	else:
		print("Congratulations, you defeated " + enemy_name + "!")
		if enemy_name == theLecturer:
			input()
			running = False
	health = player_health

def enemy_attack(enemy_health):
	if enemyAttack["headbutt"][0] == True and enemy_health > 15:
		return("headbutt")
	if enemyAttack["kick"][0] == True:
		return("kick")
	return("punch")


def is_valid_attack(attack):
	for key in playerAttack:
		if attack == key:
			if playerAttack[key][0] == True:
				return True
			else:
				return False