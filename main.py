import ui 
import logic
import pygame as pg 
from pygame.locals import *
#from sys import exit

factor={'atk':30,'life':100,'atk_ob':[10],'life_ob':[100],'atk_up':1,'atk_ob_up':1} # game factors(atk_ob & life_ob to be finished)
status={'main':0,'change':0,'fight':0,'subchoice':0,'reward':[0,0],'skill':0}

#identify status
#whether keyin for change plot work
#in fight:1 ; reward:2 ; else:0
#choicing:0 ; event:1 ; fight:2 ; item:3 
#nothing:0 ; skill:1 ; item:2 ; item been used or factor change:3


pg.init()
screen = pg.display.set_mode((640,480),0,32)        #set window
pg.display.set_caption('RPG(project no.15)')        #set window title

background=pg.image.load('background.gif').convert()
screen.blit(background,(0,0))

ui.word('Welcome to CK',(150,255,0),0.5)
ui.word('press Enter to continue')
pg.display.update()

#ui.change_plot(1)   #?

def stop():
    status['fight']=0
    status['main']=-1
def ploting(f): 
    status['change']=f(status['main'])
    #screen.blit(background,(0,0))
    #pg.display.update()            need to be solve
    if status['change']:
        status['main']+=1
        status['change']=0
def fight():
    status['fight']=ui.fight(status['main'])
    status['subchoice']=0
def using(f):
    global factor
    factor,status['skill']=f(factor)
    factor=logic.react(factor,status['skill'],status['main'])
    fight()
def lose():
    lose=pg.image.load('lose.gif').convert()
    screen.blit(lose,(0,0))
    ui.word('you lose. please quit and try again',(255,0,0),0.5)
    stop()
    pg.display.update()
def win():
    win=pg.image.load('win.gif').convert()
    screen.blit(win,(0,0))
    ui.word('you win the battle and get something',(150,150,0),0.5)
    ui.word('press v to choose item')
    #screen.blit(plot.plot,(plot.x,plot.y/2))
    #screen.blit(express.plot,(express.x,express.y))
    factor['life_ob'].pop(0)
    factor['atk_ob'].pop(0)
    status['fight']=0
    status['main']+=1
    pg.display.update()
def reward(state):
    i=0
    while i<len(status['reward']):
        if status['reward'][i] == 0:
            status[i] = state
            break
        i+=1
    status['main']+=1
    status['fight']=0
    print(status['main'])
    return i                        
                  
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            exit()
        
        if factor['life']<=0:
            lose()
        
        if factor['life_ob']:
            if factor['life_ob'][0]<=0:
                win()
        else:
            pass #final win
        
        if event.type == KEYDOWN: 
            if event.key == K_RETURN:
                ploting(ui.change_plot)                   #to plot
            
            if event.key == K_v:
                ploting(ui.reward)
                status['fight'] = 2
            #do reward
    
            if event.key == K_f:           
                fight()       #to fight
            
            if status['fight']==1: 
                #if event.key == K_b:
                #   ui.fight(status['main'])
                #   status['subchoice']=0
                                
                if event.key == K_1 and status['subchoice']==0:
                    ui.choice_event(status['main'])
                    status['subchoice']=1
                if event.key == K_2 and status['subchoice']==0:
                    ui.choice_battle(status['reward'])
                    status['subchoice']=2
                if event.key == K_3 and status['subchoice']==0:
                    ui.choice_item(status['reward'])
                    status['subchoice']=3
            
                if status['subchoice'] == 1:      #act(need discusion)
                    if event.key == K_q:
                        if status['main'] == 1:
                            ui.feed()
                            stop()

                    if event.key == K_w:
                        if status['main'] == 1:
                            ui.capture()
                            stop()
                                                       
                if status['subchoice'] == 2:      #attack(function not complete)
                    if event.key == K_q:
                        using(logic.hit)
                    if event.key == K_w:
                        using(logic.charge)
                    #if event.key == K_e and status['reward'][0]==1:
                    #if event.key == K_r and status['reward'][1]==1:    
                #if status['subchoice']==3:
                #    if event.key == K_q and status['reward'][0]==2:
                #    if event.key == K_w and status['reward'][1]==2:

            if status['fight'] == 2:
                if event.key == K_z:
                    reward(1)
                if event.key == K_x:
                    reward(2)
                if event.key == K_c:
                    r_num=reward(3)
                    if r_num ==1:
                        factor['atk']*=1.2
                    #if r_num ==2:

            

             

