# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:46:19 2021

@author: EDISON
"""
import random
import pygame
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
class block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
pygame.init()
screen=pygame.display.set_mode([800,500]) 
block_sprites_list=pygame.sprite.Group()       
all_sprites_list=pygame.sprite.Group()
for i in range(50):
    black=block(BLACK,20,15)
    black.rect.x=random.randrange(700)
    black.rect.y=random.randrange(400)
    block_sprites_list.add(black)
    all_sprites_list.add(black)
for i in range(1):
    player=block(RED,50,35)
    player.rect.x=random.randrange(700)
    player.rect.y=random.randrange(400)
    all_sprites_list.add(player)


clock=pygame.time.Clock()
timeTick=pygame.time.get_ticks()
font=pygame.font.Font(None,50)
gametime=0
end=False


score=0
play=True
startTime=pygame.time.get_ticks()
while play:
    if gametime < 10:
        gametime = (pygame.time.get_ticks()-startTime)/1000
    else:
        end=True
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
            
            
    (m_x,m_y)=pygame.mouse.get_pos()
    player.rect.x=m_x
    player.rect.y=m_y  
    #######################################################
    if end==False:
        hit_list=pygame.sprite.spritecollide(player,block_sprites_list,True)

        for block in hit_list:
            score=score+1
            print(score)



      


    ########################################################
  
    
 
    screen.fill(WHITE)
    text=font.render("SCORE:"+str(score),True,RED)
    screen.blit(text,(10,10))
    text=font.render("time:"+str(gametime),True,RED)
    screen.blit(text,(10,50))  
    
    
    
    
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()    



















    