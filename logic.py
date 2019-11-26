import main
def hit(status):
	if status == 1:
		main.factor[life_ob[0]]-=main.factor[atk]*main.factor[atk_up]
		print('Beat the monster: "ahah ahhhh..." The monster loses %f points of life.'% (atk*atk_up))
		main.factor[atk_up]=1	
	return 1
def charge(status):
	main.factor[atk_up]*=1.2
	return 2
	print("Next round, you'll attack the monster 0.2 stronger than you will originally.")
def react(skill_use,status):
	if status == 1:
		main.factor[atk_ob[0]] -= main.factor[atk_ob]*main.factor[atk_ob_up]
		print('The monster is attacking you... Be careful...\n"Ahhh"')