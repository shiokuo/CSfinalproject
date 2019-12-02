import main
def hit(status):
	if status == 1:
		factor[life_ob[0]] -= factor[atk]*factor[atk_up]
		print('Beat the monster: "ahah ahhhh..." The monster loses %f points of life.'% (atk*atk_up))
		factor[atk_up]=1	
	return factor,1
def charge(status):
	factor[atk_up]*=1.2 #to be adjusted
	return factor,2
	print("Next round, you'll attack the monster 0.2 stronger than you will originally.")
def react(skill_use,status):
	if status == 1:
		factor[life_atk_ob[0]] -= factor[atk_ob]*factor[atk_ob_up]
		print('The monster is attacking you... Be careful...\n"Ahhh"')
	return factor