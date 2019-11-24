def hit(fac,status):
    if status == 1:
        life_ob[0]-=atk*atk_up
        print('Beat the monster: "ahah ahhhh..." The monster loses %f points of life.'%(atk*atk_up))
        atk_up=1	
        return fac,1
def charge(fac,status):
	atk_up*=1.2
	print("Next hit, you'll attack the monster 0.2 stronger than you will originally.")
	return fac,2
def react(factor,skill_use,status):
	if status == 1:
		atk_ob[0] -= atk_ob*atk_ob_up
		print('The monster is attacking you... Be careful...\n"Ahhh"')
	return factor