dict{'atk':}
def hit(fac,status):
    if status == 1:
        life_ob[0]-=atk*atk_up
		#let monster shake a while(this part can be done next week)#
		print(‘you use hit and make monster lost %f life’,atk*atk_up)
		atk_up=1
	#~	
	return fac,1
def charge(fac,status):
	Atk_up*=1.2
	return fac,2
    #print
def react(factor,skill_use,status):
	if status == 1:
		#do as monster using hit to us
		#don’t forget printing
	#~
    return fac

