# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:04:08 2021

@author: EDISON
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:12:17 2021

@author: EDISON
"""
import random
import pygame
from math import pi
BLACK=(0,0,0)
WHITE=(155,243,0)
BLUE=(0,153,255)
YELLOW=(255,255,0)
COOL=(190,153,255)
pygame.init()#初始化

size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")
rect_x=0
rect_y=250
done=False
r=1
shift=1
clock=pygame.time.Clock()
while not done:
    screen.fill(WHITE)
    rect_x=rect_x+1
    #pygame.draw.polygon(screen,BLUE,[(200,200),(150,250),(250,250)]) 
    #pygame.draw.rect(screen,YELLOW,(rect_x,rect_y,100,100))
    r=r+shift
    #pygame.draw.circle(screen,YELLOW,(200,150),r)
    if r >200:
        shift=shift*-1
    if r<1:
        shift=shift*-1
   
    
    pygame.draw.rect(screen,BLUE,(0,0,100,100))
    pygame.draw.polygon(screen,YELLOW,[(200,200),(175,250),(225,250)])
    pygame.draw.arc(screen,BLUE,(150,300,100,100),pi,2*pi)
    pygame.draw.rect(screen,BLUE,(300,0,100,100))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
            
            
            
    clock.tick(100)
    pygame.display.flip()#更新畫面
pygame.quit()




