import ui 
import logic
import pygame as pg 
from pygame.locals import *
#from sys import exit

factor={'atk':30,'life':100,'atk_ob':[10],'life_ob':[100],'atk_up':1,'atk_ob_up':1} # game factors(atk_ob & life_ob to be finished)
status={'main':0,'change':0,'fight':0,'subchoice':0,'reward':[0,0],'skill':0}            
#identify status
#whether keyin for change plot work
#whether we are in fight
#what subcoice we're in 
#what we choose for reward


pg.init()
screen = pg.display.set_mode((640,480),0,32)        #set window
pg.display.set_caption('RPG(project no.15)')        #set window title

background=pg.image.load('background.gif').convert()
screen.blit(background,(0,0))

my_font = pg.font.SysFont("arial", 50)
plot_1=my_font.render('Welcome to CK',999,(150,255,0))
x_1=((640-plot_1.get_width()))/2
y_1=((480-plot_1.get_height()))/2
plot_2 = my_font.render('press Enter to continue',1,(255,0,0))
x_2=((640-plot_2.get_width()))/2
screen.blit(plot_1,(x_1,y_1))
screen.blit(plot_2,(x_2,410))
pg.display.update()

ui.change_plot(1)
def ploting(f):
    status['change']=f(status['main'])
    screen.blit(background,(0,0))
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
    status['fight']=0
    status['main']=-1
    pg.display.update()
def win():
    win=pg.image.load('win.gif').convert()
    screen.blit(win,(0,0))
    factor['life_ob'].pop(0)
    factor['atk_ob'].pop(0)
    status['fight']=0
    status['main']+=1
    pg.display.update()
def reward(state):
    i=0
    while i<len(status['reward']):
        if status[i] == 0:
            status[i] == state
            break
        i+=1
    status['main']+=1
    return i                        
                  
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            exit()
        
        if event.type == KEYDOWN: 
            if event.key == K_RETURN:
                ploting(ui.change_plot)                   #to plot
            
            if event.key == K_v:
                ploting(ui.reward)
                factor['fight'] == 2
            #do reward
    
            if event.key == K_f:           
                fight()       #to fight
            
            if status['fight']==1: 
                #if event.key == K_b:
                #   ui.fight(status['main'])
                #   status['subchoice']=0
                if factor['life']<=0:
                    lose()
                if factor['life_ob'][0]<=0:
                    win()
                
                if event.key == K_1 and status['subchoice']==0:
                    ui.choice_event(status['reward'])
                    status['subchoice']=1
                if event.key == K_2 and status['subchoice']==0:
                    ui.choice_battle(status['reward'])
                    status['subchoice']=2
                if event.key == K_3 and status['subchoice']==0:
                    ui.choice_item(status['reward'])
                    status['subchoice']=3
            
                if status['subchoice'] == 1:      #act(need discusion)
                    #if
                    print(1)
                                    
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

            

             

