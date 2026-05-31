import pygame
from Player import Player
from bullet import bullet
import random
import time
import pygame
from moviepy.editor import VideoFileClip
import numpy as np
from background import Background

from PIL import Image, ImageSequence
import pygame




pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()


pygame.mixer.music.load("Menu_music.mp3")
Resolutionx=1400
Resolutiony=768
Spawing_bullets_delay=4
debug_mode=False
dt=0
IWV=0
Jump_step=0

#Frame creator
pygame.display.set_caption("Les Jeux de la peur")
screen=pygame.display.set_mode((Resolutionx,Resolutiony))

class Game:
    def __init__(self):
        self.player=Player()
        self.pressed={}
        self.background=Background()


game=Game()

background_original = pygame.image.load("BG.png").convert()
background = pygame.transform.scale(background_original, (Resolutionx, Resolutiony))
gif = Image.open("Menu_GIF_2.gif")


running=True

frames = []


for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")  # important pour pygame

    pygame_image = pygame.image.fromstring(
        frame.tobytes(),
        frame.size,
        "RGBA"
    )
    pygame_image = pygame.transform.scale(pygame_image, (Resolutionx, Resolutiony))
    frames.append(pygame_image)



counter = time.time()

frame_index = 0

running = True
on=True
pygame.mixer.music.play(-1)

while on==True and running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False




    frame_index = (frame_index + 1) % len(frames)

    screen.blit(frames[frame_index], (0, 0))

    pygame.display.flip()


    if game.pressed.get(pygame.K_SPACE):
        on=False
        running=False
        pygame.mixer.music.stop()
    clock.tick(30)









def Check_Wazowski_length_for_BG(L_R):
    #print(game.player.rect.x)
    #print(game.background.rect.x)
    if game.player.rect.x<=10 and L_R== True:
        #print("Impossible4")
        return None
    if game.player.rect.x>=Resolutionx-10 and L_R== False:
        #print("Impossible2")
        return None

    
    if game.background.rect.x>=0 and L_R == True and game.player.rect.x<=156:
        #print("Impossible1")
        return None
    if game.background.rect.x<-2490 and game.player.rect.x>Resolutionx-156 and L_R==False:
        #print("Impossible3")
        return None


    
    if game.player.rect.x >Resolutionx-150 and L_R== False:
        game.background.rect.x=game.background.rect.x-game.player.velocity
        for bullet in game.player.all_bullets:
            bullet.rect.x=bullet.rect.x-game.player.velocity


        #print("right back")
        return None
    
    if game.player.rect.x < 150 and L_R== True:
        game.background.rect.x=game.background.rect.x+game.player.velocity
        for bullet in game.player.all_bullets:
            bullet.rect.x=bullet.rect.x+game.player.velocity
        #print("left back")
        return None
    
    if L_R == True:
        game.player.move_left()
        #print("simple move L")
        return None
    
    if L_R == False:
        game.player.move_right()
        #print("simple move R")
        return None


running=True
pygame.mixer.music.load("Running_1.mp3")
pygame.mixer.music.play(-1)

On_move=False
ticks=0
fps=time.time()
OJ=False
while running :
    ticks=ticks+1
    if time.time()-fps>1:
        #print(ticks+1)
        ticks=0
        fps=time.time()

    IWV=IWV+1
    if time.time()-counter>Spawing_bullets_delay:
        counter=time.time()
        game.player.launch_bullet()




    if (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d)):
        Check_Wazowski_length_for_BG(False)

        On_move=True
        

    if (game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q)):
        Check_Wazowski_length_for_BG(True)
        On_move=True
    
    if game.pressed.get(pygame.K_l):
        if debug_mode==True:
            debug_mode=False
        else:
            debug_mode=True 
    print(Jump_step)
    if game.pressed.get(pygame.K_SPACE) and OJ==False:
        Jump_step=1
        OJ=True
    
    if Jump_step==13:
            game.player.jump7()
            Jump_step=0
            OJ=False
    if Jump_step==11:
            game.player.jump6()
            Jump_step=Jump_step+1
    if Jump_step==9:
            game.player.jump5()
            Jump_step=Jump_step+1
    if Jump_step==7:
            game.player.jump4()
            Jump_step=Jump_step+1
    if Jump_step==5:
            game.player.jump3()
            Jump_step=Jump_step+1
    if Jump_step==3:
            game.player.jump2()
            Jump_step=Jump_step+1
    if Jump_step==1:
            game.player.jump1()
            Jump_step=Jump_step+1
    if Jump_step==2 or  Jump_step==4 or Jump_step==6 or Jump_step==8 or Jump_step==10 or Jump_step==12:
         Jump_step=Jump_step+1

            





    if On_move==True:
        
        dt=dt+1

        if dt <=0 or dt>150:
            screen.blit(game.player.image1, game.player.rect)


        if dt > 50:
            screen.blit(game.player.image2, game.player.rect)

        if dt > 100:
            screen.blit(game.player.image3, game.player.rect)

        if dt>150:
            screen.blit(game.player.image4, game.player.rect)
            dt=0
        else:
             screen.blit(game.player.image1, game.player.rect)

    else:
        screen.blit(game.player.image1, game.player.rect)
    

    



    On_move=False
    pygame.display.flip()



    #Sprite Display
    screen.blit(background,(0,0))
    screen.blit(game.background.image, game.background.rect)
    game.player.all_bullets.draw(screen)


    if debug_mode:
        for bullet in game.player.all_bullets:
            bullet.draw_debug(screen)

        game.player.draw_debug(screen)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running=False
            print("Succesfully closed")


        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



    for bullet in game.player.all_bullets:
        bullet.move()
        if game.player.rect.y<bullet.rect.y+10 and game.player.rect.colliderect(bullet.rect):
            #pygame.mixer.music.stop()
            running=False
            print("Succesfully closed")
            #À changer pour mettre un écran de fin
    clock.tick(60)

pygame.quit()
