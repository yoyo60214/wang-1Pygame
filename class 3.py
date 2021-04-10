# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:12:17 2021

@author: EDISON
"""
import pygame
BLACK=(0,0,0)
WHITE=(255,0,0)
pygame.init()#初始化
import random
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done=False
clock=pygame.time.Clock()
while not done:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    clock.tick(10)
    
    color=(r,g,b)
    screen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    # -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:12:17 2021

@author: EDISON
"""
import pygame
import random
BLACK=(0,0,0)
WHITE=(255,0,0)
T=(225,189,0)
pygame.init()#初始化
import random
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")
count=100
circle_x=350
circle_y=0
rect_x=300
rect_y=200
circle_list=[]

color=WHITE



for i in range(0,count):
    point=[]
    circle_x=random.randint(20,680)
    circle_y=random.randint(-500,0)
    circle_list.append(point)
    point.append(circle_x)
    point.append(circle_y)





done=False
clock=pygame.time.Clock()
while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("K_SPACE Press")
            if event.key==pygame.K_UP:
                print("K_UP Press")
                rect_y=rect_y-10
            if event.key==pygame.K_DOWN:
                print("K_DOWN Press")
                rect_y=rect_y+10
            if event.key==pygame.K_LEFT:
                print("K_LEFT Press")
                rect_x=rect_x-10
            if event.key==pygame.K_RIGHT:
                print("K_RIGHT Press")
                rect_x=rect_x+10
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            print(pos[0])
            print(pos[1])
            rect_x=pos[0]
            rect_y=pos[1]
            
            color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
       ############C######################################################################
               
    circle_y=circle_y+10
    if circle_y>700:
        circle_y=0
        
    for i in range(0,count):
        x=circle_list[i][0]
        y=circle_list[i][1]
        y=y+1
        circle_list[i][1]=circle_list[i][1]+1
        pygame.draw.circle(screen,color,(x,y),10)
    pygame.draw.rect(screen,T,[rect_x,rect_y,100,100])





#########################################################################################            
    clock.tick(100)
    pygame.display.flip()#更新畫面
pygame.quit()










