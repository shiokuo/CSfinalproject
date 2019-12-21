import pygame
screen = pygame.display.set_mode((640,480),0,32)
background=pygame.image.load('background.gif').convert()
pic=['stealerv3.png','OXOv2.png','chemistryv2.png']
#import main
def f_to_back():
    f=pygame.image.load('IMG_2920.png').convert()
    screen.blit(f,(0,360))
    bar=pygame.image.load('bar.gif').convert()
    screen.blit(bar,(((640-bar.get_width()))/2,(480-bar.get_height())))
def word(string,color=(255,69,2),coef=1,size=40,c_x=1):
    my_font = pygame.font.SysFont("Impact", size)
    plot = my_font.render(string,999,color)
    x=((640-plot.get_width()))/2
    y=((480-plot.get_height()))
    screen.blit(plot,(x*c_x,y*coef))

def change_plot (status):
    if status==0:      #breakfaststealer
        screen.blit(background,(0,0))
        my_font = pygame.font.SysFont("Impact", 22)
        plot_1=my_font.render('You\'re going to enjoy your breakfast,',999,(0,199,140))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))*0.4
        screen.blit(plot_1,(x,y))
        word('only to find it be stolen!',(0,199,140),0.6,22)
        word('press f to continue',(210,105,30))
        #f=my_font.render('press f to continue',999,(210,105,30))
        #screen.blit(f,(x,400))
        pygame.display.update()
        return 1
    
    if status==4:      #OXO
        screen.blit(background,(0,0))
        my_font = pygame.font.SysFont("Impact", 23)
        plot_1=my_font.render('Now, a man who teaches ',999,(0,199,140))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))*0.4
        word('Earth Science blocks your way.',(0,199,140),0.6,23)
        screen.blit(plot_1,(x,y))
        word('press f to continue',(210,105,30))
        #f=my_font.render('press f to continue',999,(210,105,30))
        #screen.blit(f,(0,400))
        pygame.display.update()
        return 1
    
    if status==8:      #tanya
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('Some chemistry textbooks stand in front of you. LOL',999,(0,199,140))
        x=((640-plot_1.get_width()))/2
        y=((480-plot_1.get_height()))/2
        screen.blit(background,(0,0))
        screen.blit(plot_1,(x,y))
        word('press f to continue',(210,105,30))
        #f=my_font.render('press f to continue',999,(210,105,30))
        #screen.blit(f,(0,400))
        pygame.display.update()
        return 1
    
def fight(status,factor):
    #width, height = 640, 480                      
    #screen = pygame.display.set_mode((width, height)) 
    #fight=pygame.image.load('FIGHT.PNG').convert()
    #act=pygame.image.load('ACT.PNG').convert()
    #tool=pygame.image.load('TOOL.PNG').convert()
    if status==1:
        #screen = pygame.Surface(screen.get_size())
        #screen = screen.convert()
        #screen.fill((255,255,255))
        my_font = pygame.font.SysFont('Impact', 60)
        enemy_1=pygame.image.load(pic[0]).convert()
        screen.blit(enemy_1,(0,0))
        word('your life:%.2f'%factor['life'],size=20,coef=0.25,c_x=0.25)
        word('rival life:%.2f'%factor['life_ob'][0],size=20,coef=0.4,c_x=0.25)
        #screen.blit(fight,(0,0))
        #screen.blit(act,(0,160))
        #screen.blit(tool,(0,320))
        f=my_font.render('1:event 2:skill 3:item',999,(218,112,214))
        screen.blit(f,(0,400))
        pygame.display.update()
        return 1
    if status==5:
        enemy_2=pygame.image.load(pic[1]).convert()
        screen.blit(enemy_2,(0,0))
        word('your life:%.2f'%factor['life'],size=20,coef=0.25,c_x=0.25)
        word('rival life:%.2f'%factor['life_ob'][0],size=20,coef=0.4,c_x=0.25)
        my_font = pygame.font.SysFont('Impact', 60)
        #screen.blit(fight,(0,0))
        #screen.blit(act,(0,160))
        #screen.blit(tool,(0,320))
        f=my_font.render('1:event 2:skill 3:item',999,(218,112,214))
        screen.blit(f,(0,400))
        pygame.display.update()
        return 1
    if status==9:
        enemy_3=pygame.image.load(pic[2]).convert()
        screen.blit(enemy_3,(0,0))
        word('your life:%.2f'%factor['life'],size=20,coef=0.25,c_x=0.25)
        word('rival life:%.2f'%factor['life_ob'][0],size=20,coef=0.4,c_x=0.25)
        my_font = pygame.font.SysFont('Impact', 60)
        #screen.blit(fight,(0,0))
        #screen.blit(act,(0,160))
        #screen.blit(tool,(0,320))
        f=my_font.render('1:event 2:skill 3:item',999,(218,112,214))
        screen.blit(f,(0,400))
        pygame.display.update()
        return 1
    else :
        return 0
def choice_event(status):
    f_to_back()
    if status == 1:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('(q)feed more food(w)capture it',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,((480-plot_1.get_height()))))
        
        pygame.display.update()
        return 1
    if status == 5:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('(q)clean the floor(w)ask him to dance',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,((480-plot_1.get_height()))))
        
        pygame.display.update()
        return 1
    if status == 9:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('(q)draw a mind map(w)hide it in trashcan',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,((480-plot_1.get_height()))))
        
        pygame.display.update()
        return 1
    else:
        return 0
def choice_battle(status):
    f_to_back()
    my_font = pygame.font.SysFont('Impact', 30)
    plot_1=my_font.render('(q)attack',999,(0,199,140))
    x=((640-plot_1.get_width()))/4
    #y=((480-plot_1.get_height()))/3
    screen.blit(plot_1,(0,((480-plot_1.get_height()))))
    plot_2=my_font.render('(w)power',999,(0,199,140))
    #y=((480-plot_1.get_height()))/3
    screen.blit(plot_2,(x,((480-plot_1.get_height()))))
    
    pygame.display.update()
    if status[0]==1:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('(e)scare',999,(0,199,140))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(2*x+5,((480-plot_1.get_height()))))
        pygame.display.update()
    if status[1]==1:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('(r)burnup',999,(0,199,140))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(3*x,((480-plot_1.get_height()))))
        pygame.display.update()
def choice_item(status):
    f_to_back()
    if status[0]!=2 and status[1]!=2:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('nothing',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,((480-plot_1.get_height()))))
        pygame.display.update()
    if status[0]==2:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('breakfast(q)',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(0,((480-plot_1.get_height()))))
        pygame.display.update()
    if status[1]==2:
        my_font = pygame.font.SysFont('Impact', 30)
        plot_1=my_font.render('stone statue(w)',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(plot_1,(200,((480-plot_1.get_height()))))
        pygame.display.update()
def feed():
    '''fail'''    
    my_font = pygame.font.SysFont('Impact', 40)
    plot_1=my_font.render('The thief bites you and runs away.',999,(0,199,140))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    word('quit and try again')
    screen.blit(background,(0,0))
    screen.blit(plot_1,(x,y))
    pygame.display.update()    
def capture():
    '''fail'''    
    my_font = pygame.font.SysFont('Impact', 40)
    plot_1=my_font.render('It ran away. lol',999,(0,199,140))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    word('quit and try again')
    screen.blit(background,(0,0))
    screen.blit(plot_1,(x,y))
    pygame.display.update()
def clean(): 
    '''blood up up =)(use heal)'''
    screen.blit(background,(0,0))   
    my_font = pygame.font.SysFont('Impact', 40)
    plot_1=my_font.render('Bro, you are a good student.',999,(0,199,140))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    word('press g to continue')
    pygame.display.update()
    #print('Bro, you are a good student.')
def dance():
    '''his attack become more cruel'''    
    screen.blit(background,(0,0))
    my_font = pygame.font.SysFont('Impact', 40)
    plot_1=my_font.render('Now he is flying into a rage.',999,(0,199,140))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    word('press g to continue')
    pygame.display.update()
    #print('Now he is flying into a rage.')
def mind_map():
    '''blood up(use heal) '''    
    screen.blit(background,(0,0))
    my_font = pygame.font.SysFont('Impact', 40)
    plot_1=my_font.render('Well done.',999,(0,199,140))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    word('press g to continue')
    pygame.display.update()
    #print('Well done.')
def hide():
    '''nothing happen'''    
    screen.blit(background,(0,0))
    my_font = pygame.font.SysFont('Impact', 40)
    plot_1=my_font.render('At least you know how to hide from the pressure.',999,(0,199,140))
    x=((640-plot_1.get_width()))/2
    y=((480-plot_1.get_height()))/2
    screen.blit(plot_1,(x,y))
    word('press g to continue')
    pygame.display.update()
    #print('At least you know how to hide from the pressure.')    
def reward(status):
    if status==2:
        my_font = pygame.font.SysFont('Impact', 20)
        plot_1=my_font.render('choose your reward(z)weaken(x)a new breakfast[?](c)a sword[attack up]',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(background,(0,0))
        screen.blit(plot_1,(0,420))
        pygame.display.update()
        return 1
    if status==6:
        my_font = pygame.font.SysFont('Impact', 20)
        plot_1=my_font.render('choose your reward(z)strong charge(x)stone statue[?](c)shield[life up]',999,(255,69,2))
        #x=2*((640-plot_1.get_width()))/3
        #y=((480-plot_1.get_height()))/3
        screen.blit(background,(0,0))
        screen.blit(plot_1,(0,420))
        pygame.display.update()
        return 1

