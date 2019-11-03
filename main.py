# -*- coding: utf-8 -*-

import pygame
import time
import random
 
pygame.init()

#%% set params

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
bright_green = (0,255,0)

health_color_bright = (255,0,0)
energy_color_bright = (255,255,0)
mood_color_bright = (0,0,255)

health_color_reg = (200,0,0)
energy_color_reg = (200,200,0)
mood_color_reg = (0,0,200)

health_color = health_color_reg
energy_color = energy_color_reg
mood_color = mood_color_reg

health_color_dark = (125,0,0)
energy_color_dark = (125,125,0)
mood_color_dark = (0,0,125)

frame_color = black

bar_width = 90
bar_height = 40
bar_border = 3

radius = 40
icon_border = 3

hicfx,hicfy,hicx,hicy = int(display_width*1/7),int(display_height*5/6),int(display_width*1/7+icon_border),int(display_height*5/6)
eicfx,eicfy,eicx,eicy = int(display_width*3/7),int(display_height*5/6),int(display_width*3/7+icon_border),int(display_height*5/6)
micfx,micfy,micx,micy = int(display_width*5/7),int(display_height*5/6),int(display_width*5/7+icon_border),int(display_height*5/6)

hbfx,hbfy,hbfw,hbfh=display_width*1/7,display_height/6,bar_width,bar_height # health bar frame positions
ebfx,ebfy,ebfw,ebfh=display_width*3/7,display_height/6,bar_width,bar_height # energy bar frame positions
mbfx,mbfy,mbfw,mbfh=display_width*5/7,display_height/6,bar_width,bar_height # mood bar frame positions

health_flash_count = 3
energy_flash_count = 3
mood_flash_count = 3

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Art Game!')
clock = pygame.time.Clock()
 
#carImg = pygame.image.load('racecar.png')

starting_death_count = 100

#%% Bars    
def health_bar(b1x,b1y,b1w,b1h, color):
    pygame.draw.rect(gameDisplay,frame_color, [hbfx,hbfy,hbfw,hbfh])
    pygame.draw.rect(gameDisplay,color, [b1x,b1y,b1w,b1h])

def energy_bar(b2x,b2y,b2w,b2h, color):
    pygame.draw.rect(gameDisplay,frame_color, [ebfx,ebfy,ebfw,ebfh])
    pygame.draw.rect(gameDisplay,color, [b2x,b2y,b2w,b2h])
    
def mood_bar(b3x,b3y,b3w,b3h, color):
    pygame.draw.rect(gameDisplay,frame_color, [mbfx,mbfy,mbfw,mbfh])
    pygame.draw.rect(gameDisplay,color, [b3x,b3y,b3w,b3h])


#%% Icons
def health_icon(health_color): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[hicfx,hicfy],radius,0)
    pygame.draw.circle(gameDisplay,health_color,[hicx,hicy],radius-icon_border*4,0)

def energy_icon(energy_color): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[eicfx,eicfy],radius,0)
    pygame.draw.circle(gameDisplay,energy_color,[eicx,eicy],radius-icon_border*4,0)

def mood_icon(mood_color): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[micfx,micfy],radius,0)
    pygame.draw.circle(gameDisplay,mood_color,[micx,micy],radius-icon_border*4,0)

#%%
#def health_button(health_width): 
#    health_color = health_color_bright
#    color_change_count = 20
#    health_width = health_width + 20
#    return health_color, color_change_count,health_width
#    
#def energy_button(energy_width): 
#    energy_color = energy_color_bright
#    color_change_count = 20
#    energy_width += 20
#    return energy_color, color_change_count,energy_width
#
#def mood_button(mood_width):
#    mood_color = mood_color_bright
#    color_change_count = 20
#    mood_width += 20   
#    return mood_color, color_change_count,mood_width
    
#%% Generic Support Functions
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def crash():
    message_display('You Crashed')

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Art Game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)

        mouse = pygame.mouse.get_pos()

        #print(mouse)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ( (150+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
            
        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, health_color_bright,(550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, health_color_reg,(550,450,100,50))
            
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("QUIT!", smallText)
        textRect.center = ( (550+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
#        pygame.draw.rect(gameDisplay, red,(550,450,100,50))
        pygame.display.update()
        clock.tick(15)
        
def game_loop():

    player = "alive"
    frame_count = 0
    
    health_loss = random.randint(1,3)
    energy_loss = random.randint(1,3)
    mood_loss = random.randint(1,3)
    
    health_startx = display_width*1/7+bar_border
    health_starty = display_height/6+bar_border
    health_width = bar_width - bar_border*2
    health_height = bar_height - bar_border*2
    
    energy_startx = display_width*3/7+bar_border
    energy_starty = display_height/6+bar_border
    energy_width = bar_width - bar_border*2
    energy_height = bar_height - bar_border*2
    
    mood_startx = display_width*5/7+bar_border
    mood_starty = display_height/6+bar_border
    mood_width = bar_width - bar_border*2
    mood_height = bar_height - bar_border*2

    health_color = health_color_reg
    energy_color = energy_color_reg
    mood_color = mood_color_reg

    color_change_count = 0 
    
    life_count = 0
    death_rate_mod = 0.01
    death_num = 0
    
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    health_color = health_color_bright
                    color_change_count = 20
                    health_width = health_width + 20#                    
                if event.key == pygame.K_DOWN:
                    energy_color = energy_color_bright
                    color_change_count = 20
                    energy_width += 20
                if event.key == pygame.K_RIGHT:
                    mood_color = mood_color_bright
                    color_change_count = 20
                    mood_width += 20  
                    #                if event.key == pygame.K_UP:
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pass

        if player == "alive":
            gameDisplay.fill(white)
                        
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects("Death Count:" + str(death_num),smallText)
            textRect.center = (100,50)
            gameDisplay.blit(textSurf, textRect)
            
            if color_change_count > 0:
                color_change_count -= 1
            else:
                health_color, energy_color, mood_color = health_color_reg, energy_color_reg, mood_color_reg
            
            if health_width < 25:
                health_color = health_color_dark
            if energy_width < 25:
                energy_color = energy_color_dark
            if mood_width < 25:
                mood_color = mood_color_dark
            
            health_icon(health_color)
            energy_icon(energy_color)
            mood_icon(mood_color)
            
            health_bar(health_startx, health_starty, health_width, health_height, health_color)
            energy_bar(energy_startx, energy_starty, energy_width, energy_height, energy_color)
            mood_bar(mood_startx, mood_starty, mood_width, mood_height, mood_color)                        
            
            if 0 < health_width < bar_width - bar_border*2 + 30 and 0 < energy_width < bar_width - bar_border*2 + 30 and 0 < mood_width < bar_width - bar_border*2 + 30:
                if frame_count % 10 == 0:
                    health_width -= health_loss + death_rate_mod*life_count
                    energy_width -= energy_loss + death_rate_mod*life_count
                    mood_width -= mood_loss + death_rate_mod*life_count
                    life_count += 1
                    

            else:
                if health_width <= 0:
                    death_cause = "starvation!"
                elif energy_width <= 0:
                    death_cause = "acute withdrawl!"
                elif mood_width <= 0:
                    death_cause = "depressive symptomology!"
                elif health_width >= bar_width - bar_border*2 + 30:                
                    death_cause = "refeeding syndrome"
                elif energy_width >= bar_width - bar_border*2 + 30:                
                    death_cause = "heart attack"                    
                else:             
                    death_cause = "couch-potato-itis"                
                player = "dead"
                dead_count = starting_death_count
                death_num += 1
                life_count = 0
           
        else:
            if dead_count <= 0:
                player = "alive"
                health_width = bar_width - bar_border*2
                energy_width = bar_width - bar_border*2
                mood_width = bar_width - bar_border*2
                health_loss = random.randint(1,3)
                energy_loss = random.randint(1,3)
                mood_loss = random.randint(1,3)
            else:
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects("You died of " + death_cause,smallText)
                textRect.center = (display_height/2,display_width/2)
                gameDisplay.blit(textSurf, textRect) 
                dead_count -= 1
            
        frame_count += 1
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()