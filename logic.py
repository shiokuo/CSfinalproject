count = 0
def hit(factor):
	'''Define how the player attacks the monster.'''
	factor['life_ob'][0] -= factor['atk']*factor['atk_up']
	print('Beat the monster: "ahah ahhhh..." The monster loses %f points of life.'% (factor['atk'] * factor['atk_up']))
	factor['atk_up']=1	
	return factor

def charge(factor):
	'''You can attack 0.2 more powerfully the next round.'''
	factor['atk_up']*=1.2 #to be modified
	print("Next round, you'll attack the monster 0.2 more powerfully than you will originally.")
	return factor

def react(factor,status): 
	'''Define how the monster attacks the player.'''
	if status == 1:
		factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
		print('The monster is attacking you... Be careful...\n"Ahhh"')
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
	return factor

def strong_charge(factor):
	factor['atk_up'] *= 2
	factor['life'] *= 2
	print('')
	return factor

def (factor):
	print('')
	return factor

def (factor):
	print('')
	return factor

def (factor):
	print('')
	return factor

def (factor):
	print('')
	return factor