count = 0
def hit(factor):
	factor['life_ob'][0] -= factor['atk']*factor['atk_up']
	print('Beat the monster: "ahah ahhhh..." The monster loses %f points of life.'% (factor['atk'] * factor['atk_up']))
	factor['atk_up']=1	
	return factor
def charge(factor):
	factor['atk_up']*=1.2 #to be modified
	print("Next round, you'll attack the monster 0.2 stronger than you will originally.")
	return factor
def react(factor,status):
	if status == 1:
		factor['life'] -= factor['atk_ob'][0]*factor['atk_ob_up']
		print('The monster is attacking you... Be careful...\n"Ahhh"')
	return factor
def irritate(factor):
	

