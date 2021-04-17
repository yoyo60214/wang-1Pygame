# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:07:26 2021

@author: EDISON
"""

import pygame
import random
BLACK=(0,0,0)
WHITE=(0,255,255)
RED=(255,0,0)
pygame.init()#初始化
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

backgroundPic=pygame.image.load("7.jpg")
backgroundPic=pygame.transform.scale(backgroundPic,size)
backgroundPic.convert()
shipPic=pygame.image.load("4.png")
shipPic=pygame.transform.scale(shipPic,(100,100))
shipPic.convert
shootSound=pygame.mixer.Sound("13.ogg")

font=pygame.font.Font(None,50)



ship_x=300
ship_y=400

ball_x=random.randint(0,700)
ball_y=-100
fires=[]

fireCount=100
for i in range(fireCount):
    position=[]
    x=random.randint(0,700)
    y=random.randint(-500,0)
    position.append(x)
    position.append(y)
    fires.append(position) 



score=0
done=False
clock=pygame.time.Clock()
timeTick=pygame.time.get_ticks()
while not done:
    gameTime=(pygame.time.get_ticks()-timeTick)/1000
    screen.fill(WHITE)
    screen.blit(backgroundPic,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
               shootSound.play()
               ball_x=ship_x+100/2
               ball_y=ship_y
           # if event.key==pygame.K_LEFT:
               # ship_x=ship_x-10
            if event.key==pygame.K_RIGHT:
                ship_x=ship_x+10
                
                
    if pygame.key.get_pressed()[pygame.K_LEFT]!=0:
        ship_x=ship_x-10
    if pygame.key.get_pressed()[pygame.K_RIGHT]!=0: 
        ship_x=ship_x+10
        
    ##########################################################    
    #碰撞的判斷    
    for i in range(fireCount):
        if fires[i][0]<=ball_x and fires[i][0]+10>=ball_x:
            if fires[i][1]<=ball_y and fires[i][1]+10>=ball_y:
                score=score+1
                print(score)
        
    ########################################################
    #do something
    screen.blit(shipPic,(ship_x,ship_y)) 
   
    for i in range(fireCount):
        pygame.draw.circle(screen,RED,(fires[i][0],fires[i][1]),5)
        fires[i][1]=fires[i][1]+5
        if fires[i][1]>500:
            fires[i][1]=random.randint(-500,0)
            
    pygame.draw.circle(screen,WHITE ,(ball_x,ball_y),100)    
    if ball_y>-100:
        ball_y=ball_y-1
        
    text=font.render("SCORE:"+str(score),True,WHITE)
    screen.blit(text,(10,10))  
    text=font.render("time:"+str(gameTime),True,WHITE)
    screen.blit(text,(10,50)) 
    
############################################        
    clock.tick(60)
    pygame.display.flip()#更新畫面
pygame.quit()










