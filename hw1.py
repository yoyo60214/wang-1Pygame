# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:25:53 2021

@author: EDISON
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:07:26 2021

@author: EDISON
"""

import pygame
BLACK=(0,0,0)
WHITE=(155,243,0)
pygame.init()#初始化
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

backgroundPic=pygame.image.load("10.jpg")
backgroundPic=pygame.transform.scale(backgroundPic,size)
backgroundPic.convert()
shipPic=pygame.image.load("9.png")
shipPic=pygame.transform.scale(shipPic,(250,250))
shipPic.convert
shootSound=pygame.mixer.Sound("11.ogg")
ship_x=300
ship_y=250






done=False
clock=pygame.time.Clock()
while not done:
    screen.fill(WHITE)
    screen.blit(backgroundPic,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:    
            if event.key==pygame.K_SPACE:
               shootSound.play()
            if event.key==pygame.K_LEFT:
                ship_x=ship_x-5
            if event.key==pygame.K_RIGHT:
                ship_x=ship_x+5
   #############################
   #do something
    screen.blit(shipPic,(ship_x,ship_y)) 
   
    
   
            
            
    clock.tick(60)
    pygame.display.flip()#更新畫面
pygame.quit()