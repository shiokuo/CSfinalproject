import random
count = 0
def hit(factor,status):
	'''Define how the player attacks the monster.'''
	if status == 1:
		i = 0
	if status == 5:
		i = 1 
	if status == 9:
		i = 2
	factor['life_ob'][i] -= factor['atk']*factor['atk_up']
	print('Beat the opponent: "ah ah AARRRR..."\nLife points of opponent:%f' %(factor['life_ob'][i]))
	factor['atk_up']=1	
	return factor

def charge(factor):
	'''You can attack 0.2 more powerfully the next round.'''
	factor['atk_up']*=1.2
	print("Next round, you'll attack the opponent more powerfully.")
	return factor

def react(factor,status): 
	'''Define how the monster attacks the player.'''
	if status == 1:
		factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
		print('The opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
	
	if status == 5:
		if factor['atk_ob_up'] < .8 or factor['atk_ob_up'] > 1.2:
			factor['life'] -= factor['atk_ob'][1]*factor['atk_ob_up']
			print('The opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
		
		elif factor['life_ob'][1] < 100:
			random_index = random.randint(1,10)
			if random_index >= 9:
				factor['life'] -= factor['atk_ob'][1]*factor['atk_ob_up']
				print('The opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
			elif 4 <= random_index <= 8:
				factor['atk_up'] *= 0.8
				print('Oh. You\'ll attack less powerfully next round.')
			else:
				factor['life_ob'][1] += 20
				print('The opponent is healing!\nLife points of opponent:%f' %(factor['life_ob'][1]))
		
		else:
			random_index = random.randint(1,10)
			if random_index >= 9:
				factor['atk_up'] *= 0.8
				print('Oh. You\'ll attack less powerfully next round.')
			elif 4 <= random_index <= 8:
				factor['atk_ob_up'] *= 1.2
				print("Next round, you'll be attacked more fiercely.")
			else:
				factor['life'] -= factor['atk_ob'][1]*factor['atk_ob_up']
				print('The opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
	
	if status == 9:
		if count % 4 == (0 or 1):
			factor['atk_ob_up'] = 1
			print('Reset the opponent\'s attacking factor.')
		if count % 4 == 2:
			factor['life_ob'][2] = .8
			print('Whhhaaat? Something seems to be wrong.\nLife points of opponent:%f' %(factor['life_ob'][2]))
		if count % 4 == 3:
			factor['life'] -= factor['atk_ob'][2] * factor['atk_ob_up']
			print('The opponent is attacking you... Be careful...\n"Ahhh"\nLife points of you:%f' %(factor['life']))
		count += 1
	return factor

def irritate(factor):
	'''The monster can attack 0.5 more powerfully.'''
	factor['atk_ob_up'] *= 1.5
	print('The monster is flying into a rage... Beware of the upcoming attack.')
	return factor

def weak(factor):
	'''The monster can attack 0.2 less powerfully.'''
	factor['atk_ob_up'] *= 0.8
	print('You will be attacked more mildly. Good news.')
	return factor

def heal(factor):
	factor['life'] += 20
	print('You\'re healing... ... ...\nLife points of you:%f' %(factor['life']) )
	return factor

def strong_charge(factor):
	factor['atk_up'] *= 2
	factor['life'] *= 0.5
	print("Next round, you will attack the monster more powerfully significantly.\nHowever, you are going to die if you don't have enough life point.\nSo What's your points now?\nLife points of you:%f" %(factor['life']))
	return factor

def breakfast(factor):
	factor['atk_up'] *= 3.6
	print('To begin a nice day, have your breakfast!\nSee, you are so energetic now that you can almost defeat the opponent!')
	return factor

def doll(factor):
	factor['atk_ob_up'] = 0
	print('The opponent can\'t hit you next time.')
	return factor