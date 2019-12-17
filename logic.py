import random
count = 0
def hit(factor):
	'''Define how the player attacks the monster.'''
	factor['life_ob'][0] -= factor['atk']*factor['atk_up']
	print('\nBeat the opponent: "ah ah AARRRR..."\nLife points of opponent:%f' %(factor['life_ob'][0]))
	factor['atk_up']=1	
	return factor

def charge(factor):
	'''You can attack 0.2 more powerfully the next round.'''
	factor['atk_up']*=1.2
	print("\nNext round, you'll attack the opponent more powerfully.")
	return factor

def react(factor,status): 
	'''Define how the monster attacks the player.'''
	if status == 1:
		factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
		print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
		factor['atk_ob_up'] = 1
	
	if status == 5:
		if factor['atk_ob_up'] < .8 or factor['atk_ob_up'] > 1.2:
			factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
			print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
			factor['atk_ob_up'] = 1
		
		elif factor['life_ob'][0] < 100:
			random_index = random.randint(1,10)
			if random_index >= 9:
				factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
				print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
				factor['atk_ob_up'] = 1
			elif 4 <= random_index <= 8:
				factor['atk_up'] *= 0.8
				print('\nOh. You\'ll attack less powerfully next round.')
			else:
				factor['life_ob'][0] += 20
				print('\nThe opponent is healing!\nLife points of opponent:%f' %(factor['life_ob'][0]))
		
		else:
			random_index = random.randint(1,10)
			if random_index >= 9:
				factor['atk_up'] *= 0.8
				print('\nOh. You\'ll attack less powerfully next round.')
			elif 4 <= random_index <= 8:
				factor['atk_ob_up'] *= 1.2
				print("\nNext round, you'll be attacked more fiercely.")
			else:
				factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
				print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
				factor['atk_ob_up'] = 1
	
	if status == 9:
		global count
		if count % 4 == (0 or 1):
			factor['atk_ob_up'] = 1
			print('\nReset the opponent\'s attacking factor.')
		if count % 4 == 2:
			factor['life_ob'][0] *= .8
			print('\nWhhhaaat? Something seems to be wrong.\nLife points of opponent:%f' %(factor['life_ob'][0]))
		if count % 4 == 3:
			factor['life'] -= factor['atk_ob'][0] * factor['atk_ob_up']
			print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
			factor['atk_ob_up'] = 1
		count += 1
	return factor

def irritate(factor):
	'''The monster can attack 0.5 more powerfully.'''
	factor['atk_ob_up'] *= 1.5
	print('\nThe monster is flying into a rage... Beware of the upcoming attack.')
	return factor

def weak(factor):
	'''The monster can attack 0.2 less powerfully.'''
	factor['atk_ob_up'] *= 0.8
	print('\nYou will be attacked more mildly. Good news.')
	return factor

def heal(factor):
	factor['life'] += 20
	print('\nYou\'re healing... ... ...\nLife points of you:%f' %(factor['life']) )
	return factor

def strong_charge(factor):
	factor['atk_up'] *= 2
	factor['life'] *= 0.5
	print("\nNext round, you will attack the monster more powerfully significantly.\nHowever, you are going to die if you don't have enough life point.\nSo What's your points now?\nLife points of you:%f" %(factor['life']))
	return factor

def breakfast(factor):
	factor['atk_up'] *= 3.6
	print('\nTo begin a nice day, have your breakfast!\nSee, you are so energetic now that you can almost defeat the opponent!')
	return factor

def doll(factor):
	factor['atk_ob_up'] = 0
	print('\nThe opponent can\'t hit you next time.')
	return factor