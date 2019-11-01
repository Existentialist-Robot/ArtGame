# -*- coding: utf-8 -*-

import pygame
import time
import random
 
pygame.init()
player = "alive"

#%% set params

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
yellow = (255,255,0) 
blue = (0,0,255)

health_color_bright = red
energy_color_bright = yellow
mood_color_bright = blue

health_color_reg = red
energy_color_reg = yellow
mood_color_reg = blue

health_color_dark = red
energy_color_dark = yellow
mood_color_dark = blue


block_color = blue
frame_color = black


car_width = 73

bar_width = 90
bar_height = 40
bar_border = 3

hi = 0 
ei = 0
mi = 0

hbfx,hbfy,hbfw,hbfh=display_width*1/7,display_height/6,bar_width,bar_height # health bar frame positions
mbfx,mbfy,mbfw,mbfh=display_width*3/7,display_height/6,bar_width,bar_height # energy bar frame positions
ebfx,ebfy,ebfw,ebfh=display_width*5/7,display_height/6,bar_width,bar_height # mood bar frame positions

health_flash_count = 3
energy_flash_count = 3
mood_flash_count = 3



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Art Game!')
clock = pygame.time.Clock()
 
#carImg = pygame.image.load('racecar.png')

starting_death_count = 100

#%% old stuff -delete
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Existential Crisis Averted:"+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
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
def health_icon(): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)

def energy_icon(): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)

def mood_icon(): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)

#%%
def health_button(): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)
    health_color = health_color_bright
    colour_change_count = 20
    health_width += 20   
    
def energy_button(): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)
    energy_color = energy_color_bright
    colour_change_count = 20
    energy_width += 20

def mood_button(): # circle(surface, color, center, radius, width=0)
    pygame.draw.circle(gameDisplay,frame_color,[100,100],20,width=0)
    mood_color = mood_color_bright
    colour_change_count = 20
    mood_width += 20    
    
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
            
        if 550+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red,(550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, red,(550,450,100,50))
            
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
    x_change = 0
 
    
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
    print(health_width)

    health_color = health_color_reg
    energy_color = energy_color_reg
    mood_color = mood_color_reg

    colour_change_count = 0 
    
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 1
                if event.key == pygame.K_RIGHT:
                    x_change = 2
                if event.key == pygame.K_UP:
                    x_change = 3
                    
                    # add in the buttons to here
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0

        if player == "alive":
            
            if frame_count % 5 == 0 :
                update_bars = 1
            
            if colour_change_count > 0:
                colour_change_count -= 1
            else:
                health_color, energy_color, mood_color = health_color_reg, energy_color_reg, mood_color_reg
#            x += x_change
            gameDisplay.fill(white)
     
            print(health_width)
            print(energy_width)
            print(mood_width)      
            
            health_bar(health_startx, health_starty, health_width, health_height, health_color)
            energy_bar(energy_startx, energy_starty, energy_width, energy_height, energy_color)
            mood_bar(mood_startx, mood_starty, mood_width, mood_height, mood_color)
        
            # draw all the icons here with both the frame and the icon with the update bar colors!
            
            
#            print(health_width)
#            print(type(health_width))
#            print(energy_width)
#            print(type(energy_width))
#            print(mood_width)
#            print(type(mood_width))
#            print(health_width > 0 & energy_width > 0 & mood_width > 0)

            if health_width > 0 and energy_width > 0 and mood_width > 0:
                if frame_count % 5 == 0:
                    print("DEBUG")
                    health_width -= health_loss
                    energy_width -= energy_loss
                    mood_width -= mood_loss

            else:
                if health_width <= 0:
                    death_cause = "starvation!"
                elif energy_width <= 0:
                    death_cause = "acute withdrawl!"
                else:
                    death_cause = "depressive symptomology!"
                player = "dead"
                dead_count = starting_death_count
           
                #%%  old - delete
#            thing_starty += thing_speed
#            car(x,y)
#            things_dodged(dodged)
#     
#            if x > display_width - car_width or x < 0:
#                crash()
#    
#            if thing_starty > display_height:
#                thing_starty = 0 - thing_height
#                thing_startx = random.randrange(0,display_width)
#                dodged += 1
#                thing_speed += 1
#                thing_width += (dodged * 1.2)
#     
#            if y < thing_starty+thing_height:
#                print('y crossover')
#     
#                if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
#                    print('x crossover')
#                    crash()
            
            #%%
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
        update_bars = 0
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()