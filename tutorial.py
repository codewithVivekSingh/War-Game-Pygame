import pygame
from pygame.locals import *
import sys
import random
import math

#initializing pygame modules
pygame.init()

#setting the game window size
gameSurface=pygame.display.set_mode((500,500))

#Giving the title to our game
pygame.display.set_caption("WAR Game")


#setting colors
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)

#tank 
tank=pygame.image.load(r'H:\python fun\Pygame\PygameTutorial\tank.png')
xt=220
yt=420

#bomb
bomb=pygame.image.load(r'H:\python fun\Pygame\PygameTutorial\bomb.png')
xb=random.randint(50,450)
yb=50

#missile
missile=pygame.image.load(r'H:\python fun\Pygame\PygameTutorial\missile.png')
xm=220
ym=400
   
#explosion
explosion=pygame.image.load(r'H:\python fun\Pygame\PygameTutorial\explosion.png')
xe=250
ye=250

#background
background=pygame.image.load(r'H:\python fun\Pygame\PygameTutorial\bg.png')
xbg=0
ybg=0
#---------------------------function definition--------------------

def move_left():
    global launch
    global xt
    global xm
    if xt<20:
        xt=20

    if launch==0:
        xt-=4
        xm=xt
    if launch==1:
        xt-=4
        

def move_right():
    global launch
    global xt
    global xm
    if xt>450:
        xt=450
    if launch==0:
        xt+=4
        xm=xt        
    if launch==1:
        xt+=4
        

#flags to determine state of our game
launch=0
blast=0

#--------------------------Game loop----------------------------------
    

while True: 
    
    
    #checking every event
    for event in pygame.event.get():
        pygame.key.set_repeat(10)
        #if quit event is detected quit the game
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                move_left()
            if event.key==K_RIGHT:
                move_right()
            if event.key == pygame.K_SPACE :
                launch=1
                blast=0

    #if bomb crossed tank, reposition bomb
    yb=yb+0.2
    if yb>420:
        yb=50
    
    #calculating distance between missile and bomb
    D=math.sqrt(math.pow(xm-xb, 2)+math.pow(ym-yb,2))
    #calculating distance between bomb and tank
    Dt=math.sqrt(math.pow(xb-xt, 2)+math.pow(yb-yt,2))
    
    #if launch happened and distance is large enough, keep the missle and bomb moving
    if launch==1 and D>25:
        #make missile and bomb move
        ym=ym-0.5
        yb=yb+0.5

    #if launch happened and distance is small enough, reset the bomb and missile position
    if launch==1 and D<25:
        ym=yt
        xm=xt
        yb=50
        xb=random.randint(50,450)
        launch=0
        blast=1
        
    #if blast is there, show explosion image
    if blast==1:
        gameSurface.blit(explosion, (xe, ye))
        ye-=2
    
    #if bomb crossed tank, reposition bomb
    if yb>420:
        yb=50



    #Drawing our game components
    gameSurface.blit(background,(xbg,ybg))
    gameSurface.blit(tank, (xt,yt))
    gameSurface.blit(bomb,(xb,yb))
    gameSurface.blit(missile,(xm,ym))
    gameSurface.blit(explosion, (xe, ye))

    #updating the display
    pygame.display.update()
   