import pygame
import main
def change_plot (status):
    if status==0:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('you found your breakfast is stolen',999,(255,0,0))
        x=((640-plot_1.get_width()))/2
        x=((480-plot_1.get_height()))/2
        main.screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1
    else:
        return 0
def fight(status):
    #width, height = 640, 480                      
    #main.screen = pygame.display.set_mode((width, height)) 
    fight=pygame.image.load('FIGHT.PNG').convert()
    act=pygame.image.load('ACT.PNG').convert()
    tool=pygame.image.load('TOOL.PNG').convert()
    if status==1:
        #main.screen = pygame.Surface(main.screen.get_size())
        #main.screen = main.screen.convert()
        #main.screen.fill((255,255,255))
        enemy_1=pygame.image.load('stealer.png').convert()
        main.screen.blit(enemy_1,(250,240))
        main.screen.blit(fight,(600,0))
        main.screen.blit(act,(600,160))
        main.screen.blit(tool,(600,320))
        pygame.display.update()
        return 1
    else :
        return 0
def choice_event(status):
    if status ==1:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('(a)feed more food\n(b)capture it',(255,0,0))
        pygame.display.update()
        return 1
    else:
        return 0
def choice_battle(status):
    if status[0]!=1 and status[1]!=1:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('(q)attack\n(w)charging',(255,255,0))
        pygame.display.update()
def choice_item(status):
    if status[0]!=2 and status[1]!=2:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('nothing',(255,0,0))
        pygame.display.update()
def feed(status):
    if status==1:
        my_font = pygame.font.SysFont("arial", 30)
        plot_1=my_font.render('the thief bite you and ran away',(255,255,0))
        pygame.display.update()
        return 1
    else:
        return 0
def capture(status):
    if status==1:
        my_font = pygame.font.SysFont("arial", 30)
        plot_1=my_font.render('it ran away lol',(255,255,0))
        pygame.display.update()
        return 1
    else:
        return 0
def reward(status):
    if status==2:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('choose your reward\n(z)weaken\n(a)a new breakfast\n(c)a stick',(255,0,0))
        pygame.display.update()

