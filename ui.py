import pygame
screen = pygame.display.set_mode((640,480),0,32)
#import main
def change_plot (status):
    if status==0:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('you found your breakfast is stolen',999,(255,0,0))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1
    else:
        return 0
def fight(status):
    #width, height = 640, 480                      
    #screen = pygame.display.set_mode((width, height)) 
    fight=pygame.image.load('FIGHT.PNG').convert()
    act=pygame.image.load('ACT.PNG').convert()
    tool=pygame.image.load('TOOL.PNG').convert()
    if status==1:
        #screen = pygame.Surface(screen.get_size())
        #screen = screen.convert()
        #screen.fill((255,255,255))
        enemy_1=pygame.image.load('stealer.png').convert()
        screen.blit(enemy_1,(250,240))
        screen.blit(fight,(600,0))
        screen.blit(act,(600,160))
        screen.blit(tool,(600,320))
        pygame.display.update()
        return 1
    else :
        return 0
def choice_event(status):
    if status ==1:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('(a)feed more food\n(b)capture it',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1
    else:
        return 0
def choice_battle(status):
    if status[0]!=1 and status[1]!=1:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('(q)attack\n(w)charging',999,(255,255,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
def choice_item(status):
    if status[0]!=2 and status[1]!=2:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('nothing',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
def feed(status):
    if status==1:
        my_font = pygame.font.SysFont("arial", 30)
        plot_1=my_font.render('the thief bite you and ran away',999,(255,255,0))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1
    else:
        return 0
def capture(status):
    if status==1:
        my_font = pygame.font.SysFont("arial", 30)
        plot_1=my_font.render('it ran away lol',999,(255,255,0))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1
    else:
        return 0
def reward(status):
    if status==2:
        my_font = pygame.font.SysFont("arial", 16)
        plot_1=my_font.render('choose your reward\n(z)weaken\n(a)a new breakfast\n(c)a stick',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()

