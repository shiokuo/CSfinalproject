import main.factor as fac
def hit(status):
	if status == 1:
		fac[life_ob[0]]-=fac[atk]*fac[atk_up]
		print('Beat the monster: "ahah ahhhh..." The monster loses %f points of life.'% (atk*atk_up))
		fac[atk_up]=1	
	return fac,1
def charge(status):
	fac[atk_up]*=1.2
	return fac,2
	print("Next round, you'll attack the monster 0.2 stronger than you will originally.")
def react(skill_use,status):
	if status == 1:
		fac[atk_ob[0]] -= fac[atk_ob]*fac[atk_ob_up]
		print('The monster is attacking you... Be careful...\n"Ahhh"')
	return fac