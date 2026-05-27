import pygame
from Player import Player
from bullet import bullet
import random
import time
import pygame
from moviepy.editor import VideoFileClip
import numpy as np

from PIL import Image, ImageSequence
import pygame




pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("Menu_music.mp3")
Resolutionx=1400
Resolutiony=750
Spawing_bullets_delay=1
debug_mode=False


#Frame creator
pygame.display.set_caption("Les Jeux de la peur")
screen=pygame.display.set_mode((Resolutionx,Resolutiony))

class Game:
    def __init__(self):
        self.player=Player()
        self.pressed={}


game=Game()

background_original = pygame.image.load("BG.png").convert()
background = pygame.transform.scale(background_original, (Resolutionx, Resolutiony))
gif = Image.open("Menu_GIF.gif")


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

    #screen.fill((0, 0, 0))  # optionnel
    screen.blit(frames[frame_index], (0, 0))

    pygame.display.flip()
    time.sleep(0.025)


    if game.pressed.get(pygame.K_SPACE):
        on=False
        running=False
        pygame.mixer.music.stop()






running=True
pygame.mixer.music.load("Running_1.mp3")
pygame.mixer.music.play(-1)

while running :
    
    if time.time()-counter>Spawing_bullets_delay:
        counter=time.time()
        game.player.launch_bullet()





    if (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d)) and game.player.rect.x<Resolutionx-100:
        game.player.move_right()
    if (game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q)) and game.player.rect.x>0:
        game.player.move_left()
    
    
    #Sprite Display
    screen.blit(background, (0,0))
    screen.blit(game.player.image, game.player.rect)
    game.player.all_bullets.draw(screen)

    if debug_mode:
        for bullet in game.player.all_bullets:
            bullet.draw_debug(screen)

        game.player.draw_debug(screen)

    pygame.display.flip() #screen refreshing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running=False
            pygame.quit()
            print("Succesfully closed")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    for bullet in game.player.all_bullets:
        bullet.move()
        if game.player.rect.y<bullet.rect.y+10 and game.player.rect.colliderect(bullet.rect):
            pygame.mixer.music.stop()
            running=False
            pygame.quit()
            print("Succesfully closed")
            #À changer pour mettre un écran de fin

pygame.quit()