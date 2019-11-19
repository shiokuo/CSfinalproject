import pygame as pg 
from pygame.locals import *
#from sys import exit

pg.init()
screen = pg.display.set_mode((640,480),0,32)        #set window
pg.display.set_caption('RPG(project no.15)')        #set window title

background=pg.image.load(' ').convert()
screen.blit(background,(0,0))
pg.display.update()
status=0
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            exit()
        
        if status==0 and  event.type == KEYDOWN and event.key == K_RETURN:
            

