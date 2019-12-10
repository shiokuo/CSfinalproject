import pygame
screen = pygame.display.set_mode((640,480),0,32)
background=pygame.image.load('background.gif').convert()
#import main
def word(string,color=(255,0,0),coef=1,size=50):
    my_font = pygame.font.SysFont("arial", size)
    plot = my_font.render(string,999,color)
    x=((640-plot.get_width()))/2
    y=((480-plot.get_height()))
    screen.blit(plot,(x,y*coef))

def change_plot (status):
    if status==0:      #breakfaststealer
        my_font = pygame.font.SysFont("arial", 50)
        plot_1=my_font.render('you found your breakfast is stolen',999,(255,0,0))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(background,(0,0))
        screen.blit(plot_1,(x,y))
        f=my_font.render('press f to continue',999,(255,0,0))
        screen.blit(f,(x,400))
        pygame.display.update()
        return 1
    else:
        return 0
    if status==4:      #OXO
        my_font = pygame.font.SysFont("arial", 50)
        plot_1=my_font.render('a man who taught Earth Science block your way',999,(255,0,0))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(background,(0,0))
        screen.blit(plot_1,(x,y))
        f=my_font.render('press f to continue',999,(255,0,0))
        screen.blit(f,(x,400))
        pygame.display.update()
        return 1
    else:
        return 0
    if status==8:      #tanya
        my_font = pygame.font.SysFont("arial", 50)
        plot_1=my_font.render('a chemistry teacher stand in front of you',999,(255,0,0))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(background,(0,0))
        screen.blit(plot_1,(x,y))
        f=my_font.render('press f to continue',999,(255,0,0))
        screen.blit(f,(x,400))
        pygame.display.update()
        return 1
    else:
        return 0
def fight(status):
    #width, height = 640, 480                      
    #screen = pygame.display.set_mode((width, height)) 
    #fight=pygame.image.load('FIGHT.PNG').convert()
    #act=pygame.image.load('ACT.PNG').convert()
    #tool=pygame.image.load('TOOL.PNG').convert()
    if status==1:
        #screen = pygame.Surface(screen.get_size())
        #screen = screen.convert()
        #screen.fill((255,255,255))
        my_font = pygame.font.SysFont("arial", 50)
        enemy_1=pygame.image.load('stealerv2.png').convert()
        screen.blit(background,(0,0))
        screen.blit(enemy_1,(0,0))
        #screen.blit(fight,(0,0))
        #screen.blit(act,(0,160))
        #screen.blit(tool,(0,320))
        f=my_font.render('1:event 2:skill 3:item',999,(255,0,0))
        screen.blit(f,(0,420))
        pygame.display.update()
        return 1
    if status==5:
        enemy_2=pygame.image.load('OXO.png').convert()
        screen.blit(background,(0,0))
        screen.blit(enemy_2,(0,0))
        my_font = pygame.font.SysFont("arial", 50)
        #screen.blit(fight,(0,0))
        #screen.blit(act,(0,160))
        #screen.blit(tool,(0,320))
        f=my_font.render('1:event 2:skill 3:item',999,(255,0,0))
        screen.blit(f,(0,420))
        pygame.display.update()
        return 1
    if status==9:
        enemy_3=pygame.image.load('chemistry.png').convert()
        screen.blit(background,(0,0))
        screen.blit(enemy_3,(0,0))
        my_font = pygame.font.SysFont("arial", 50)
        #screen.blit(fight,(0,0))
        #screen.blit(act,(0,160))
        #screen.blit(tool,(0,320))
        f=my_font.render('1:event 2:skill 3:item',999,(255,0,0))
        screen.blit(f,(0,420))
        pygame.display.update()
        return 1
    else :
        return 0
def choice_event(status):
    if status == 1:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('(q)feed more food(w)capture it',999,(255,0,0))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,370))
        pygame.display.update()
        return 1
    if status == 5:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('(q)clean the floor(w)ask him to dance',999,(255,0,0))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,370))
        pygame.display.update()
        return 1
    if status == 9:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('(q)draw a mind map(w)hide in the trashcan',999,(255,0,0))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,370))
        pygame.display.update()
        return 1
    else:
        return 0
def choice_battle(status):
    if status[0]!=1 and status[1]!=1:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('(q)attack\n(w)charging',999,(255,255,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
    if status[0]==1:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('(q)attack\n(w)charging\n(e)weaken',999,(255,255,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
    if status[1]==1:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('(q)attack\n(w)charging\n(e)weaken\n(r)strong charge',999,(255,255,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
def choice_item(status):
    if status[0]!=2 and status[1]!=2:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('nothing',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
    if status[0]==2:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('breakfast(q)',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
    if status[1]==2:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('doll(w)',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(x,y))
        pygame.display.update()
def feed():
    '''fail'''    
    my_font = pygame.font.SysFont("arial", 50)
    plot_1=my_font.render('the thief bite you and ran away',999,(255,255,0))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(background,(0,0))
    screen.blit(plot_1,(x,y))
    pygame.display.update()    
def capture():
    '''fail'''    
    my_font = pygame.font.SysFont("arial", 50)
    plot_1=my_font.render('it ran away lol',999,(255,255,0))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(background,(0,0))
    screen.blit(plot_1,(x,y))
    pygame.display.update()
def clean(): 
    '''blood up up =)(use heal)'''   
    my_font = pygame.font.SysFont("arial", 50)
    plot_1=my_font.render('you are a good student',999,(255,255,0))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    pygame.display.update()
def dance():
    '''his attack become more cruel'''    
    my_font = pygame.font.SysFont("arial", 50)
    plot_1=my_font.render('now he is mad at you',999,(255,255,0))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    pygame.display.update()
def mind_map():
    '''blood up(use heal) '''    
    my_font = pygame.font.SysFont("arial", 50)
    plot_1=my_font.render('well done',999,(255,255,0))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    pygame.display.update()
def hide():
    '''nothing happen'''    
    my_font = pygame.font.SysFont("arial", 50)
    plot_1=my_font.render('at least you know how to hide from\nthe pressure',999,(255,255,0))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    pygame.display.update()    
def reward(status):
    if status==2:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('choose your reward\n(z)weaken\n(a)a new breakfast\n(c)a sword',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(background,(0,0))
        screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1
    if status==6:
        my_font = pygame.font.SysFont("arial", 45)
        plot_1=my_font.render('choose your reward\n(z)heal\n(x)doll\n(c)shield',999,(255,0,0))
        x=2*((640-plot_1.get_width()))/3
        y=((480-plot_1.get_height()))/3
        screen.blit(background,(0,0))
        screen.blit(plot_1,(x,y))
        pygame.display.update()
        return 1

