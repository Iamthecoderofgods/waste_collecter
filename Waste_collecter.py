import pygame
import random
import os
from pygame.locals import *
import time

pygame.init()
WIDTH = 800
HEIGHT = 700
clock = pygame.time.Clock()

Start_time = time.time()
screen =  pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont("Times New Romain",30)
score = 0
time_left = 40
Game_over = False
def load_image(__path__):
    Bag = pygame.image.load(__path__).convert_alpha()
    Bag = pygame.transform.scale(Bag,(40,40))
    return Bag

class Sprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()

        self.image = load_image(image)
        self.rect = self.image.get_rect(topleft = (x,y))
        
        
class Bin(Sprite):
    def __init__(self):
        super().__init__("images/bin.png",0,0)
    

bin = Bin()
All_items = pygame.sprite.Group(bin)
recycable_items = pygame.sprite.Group()
nonrecycable_items = pygame.sprite.Group()


#create items#
for i in range(10):
    plastic = Sprite("images/Plastic_bag.png",random.randint(0,WIDTH),random.randint(0,HEIGHT))
    nonrecycable_items.add(plastic)
    All_items.add(plastic)
    
for i in range(15):
    Item = random.choice(["images/pen.png","images/Plastic_bag.png","images/item1.png"])
    Items= Sprite(Item,random.randint(0,WIDTH),random.randint(0,HEIGHT))
    recycable_items.add(Items)
    All_items.add(Items)

        

keys = [False,False,False,False]      


Running = True

while Running:
    clock.tick(30)
    bg = pygame.image.load("images/greenblock.png")
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))
    Score_text = font.render("Score:"+str(score),True,(10,10,10))
    screen.blit(Score_text,(10,10))
    elapsed_time = time.time()-Start_time
    if elapsed_time > 60:
        Game_over = True
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
                bin.rect.y -= 5
            elif event.key == K_s:
                keys[0] = True
                bin.rect.y += 5
            elif event.key == K_a:
                keys[0] = True
                bin.rect.x -= 5 
            elif event.key == K_d:
                keys[0] = True
                bin.rect.x += 5
    
    score += len(pygame.sprite.spritecollide(bin,recycable_items,True))
    score -= len(pygame.sprite.spritecollide(bin,nonrecycable_items,True))
    print(score)
   

            
            

            
            
        
    All_items.draw(screen)
    pygame.display.update()
    

     
    
    