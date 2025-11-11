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
button_img = pygame.image.load("images/restart.png")
score = 0
time_left = 5
game_over = False
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
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.Rect = self.image.get_rect()
        self.Rect.topleft = (x,y)
    def Draw(self):
        screen.blit(self.image,(self.Rect.x,self.Rect.y))
        action = False
        if self.Rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                action = True
        return action

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
    Items = Sprite(Item,random.randint(0,WIDTH),random.randint(0,HEIGHT))
    recycable_items.add(Items)
    All_items.add(Items)


def reset_game():
    global score,game_over,Start_time
    score = 0
    game_over = False
    Start_time = time.time()
    return score

        

keys = [False,False,False,False]      
button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)

Running = True

while Running:
    clock.tick(30)
    bg = pygame.image.load("images/greenblock.png")
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))
    Score_text = font.render("Score:"+str(score),True,(10,10,10))
    screen.blit(Score_text,(10,10))
    elapsed_time = time.time()-Start_time
    if elapsed_time >= time_left:
        game_over = True
        elapsed_time = time_left
    
    Time = font.render("Elapsed time:"+str(elapsed_time),True,(10,10,10))
    screen.blit(Time,(100,10))
    Left = font.render("total time:"+str(time_left),True,(10,10,10))
    screen.blit(Left,(450,10))

    
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
    
    if not game_over:

        score += len(pygame.sprite.spritecollide(bin,recycable_items,True))
        score -= len(pygame.sprite.spritecollide(bin,nonrecycable_items,True))
    else:
        if button.Draw():
            reset_game()
            elapsed_time -= 1
        


            
            

            
            
        
    All_items.draw(screen)
    pygame.display.update()
    

     
    
    