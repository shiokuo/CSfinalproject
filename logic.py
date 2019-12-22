import random
count = 0
def hit(factor):
	'''Define how the player attacks the opponent.'''
	factor['life_ob'][0] -= factor['atk']*factor['atk_up']
	print('\nBeat the opponent: "ah ah AARRRR..."\nThe opponent\'s life points:%f' %(factor['life_ob'][0]))
	factor['atk_up']=1	
	return factor

def charge(factor):
	'''You can attack 0.8 more powerfully the next round.'''
	factor['atk_up'] *= 1.8
	print("\nNext round, you'll attack the opponent more powerfully.")
	return factor

def react(factor,status): 
	'''Define how the opponent attacks the player.'''
	if status == 1:
		factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
		print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nYour life points:%f' %(factor['life']))
		factor['atk_ob_up'] = 1
	
	if status == 5:
		if factor['atk_ob_up'] < .8 or factor['atk_ob_up'] > 1.2:
			factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
			print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nYour life points:%f' %(factor['life']))
			factor['atk_ob_up'] = 1
		
		elif factor['life_ob'][0] < 100:
			random_index = random.randint(1,10)
			if random_index >= 7:
				factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
				print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nYour life points:%f' %(factor['life']))
				factor['atk_ob_up'] = 1
			elif 4 <= random_index <= 6:
				factor['atk_up'] *= 0.7
				print('\nOh. You\'ll attack less powerfully next round.')
			else:
				factor['life_ob'][0] += 15
				print('\nThe opponent is healing!\nThe opponent\'s life points:%f' %(factor['life_ob'][0]))
		
		else:
			random_index = random.randint(1,10)
			if random_index >= 9:
				factor['atk_up'] *= 0.8
				print('\nOh. You\'ll attack the opponent less powerfully next round.')
			elif 4 <= random_index <= 8:
				factor['atk_ob_up'] *= 1.2
				print("\nNext round, you'll be attacked more fiercely.")
			else:
				factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
				print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nYour life points:%f' %(factor['life']))
				factor['atk_ob_up'] = 1
	
	if status == 9:
		global count
		if (count % 4 == 0 or count % 4 == 1):
			if factor['atk_ob_up']>1:
				factor['atk_ob_up'] = 1
				print('\nThe opponent\'s will attack you normally next time.')
			else:
				print('\nThe opponents is too lazy to hit you.')	 
			
		if count % 4 == 2:
			factor['life_ob'][0] *= .8
			print('\n??? Something seems to be wrong since the opponent loses some points.\nThe opponent\'s life points:%f' %(factor['life_ob'][0]))
		if count % 4 == 3: 
			if factor['atk_ob_up'] != 0:
				factor['life'] -= factor['atk_ob'][0] * factor['atk_ob_up']
				print('\nThe opponent is attacking you... Be careful...\n"Ahhh"\nYour life points:%f' %(factor['life']))
				factor['atk_ob_up'] = 1
			else:
				print('The opponent can\'t hit you.')
		count += 1
	return factor

def irritate(factor):
	'''The opponent can attack 0.3 more powerfully.'''
	factor['atk_ob_up'] *= 1.3
	print('\nThe opponent is flying into a rage... Beware of the upcoming attack.')
	return factor

def weak(factor):
	'''The opponent can attack 0.2 less powerfully.'''
	factor['atk_ob_up'] *= 0.8
	print('\nYou will be attacked more mildly. Good news.')
	return factor

def heal(factor):
	factor['life'] += 15
	print('\nYou\'re healing... ... ...\nYour life points:%f' %(factor['life']) )
	return factor

def strong_charge(factor):
	factor['atk_up'] *= 3
	factor['life'] *= 0.8
	print("\nNext round, you will attack the opponent more powerfully significantly.\nHowever, you also lose some life points for compensation.\nSo What's your points now?\nYour life points:%f" %(factor['life']))
	return factor

def breakfast(factor):
	factor['atk_up'] *= 4
	print('\nTo begin a nice day, have your breakfast!\nSee, you are so energetic now that you can almost defeat the opponent!')
	return factor

def doll(factor):
	factor['atk_ob_up'] = 0
	print('\nThe opponent can\'t hit you next time.')
	return factor