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

gif = Image.open("pixel.gif")


pygame.init()

Resolutionx=1400
Resolutiony=750
Spawing_bullets_delay=1
debug_mode=False
statement=0

#Frame creator
pygame.display.set_caption("Les Jeux de la peur")
screen=pygame.display.set_mode((Resolutionx,Resolutiony))

class Game:
    def __init__(self):
        self.player=Player()
        self.pressed={}


game=Game()

background_original = pygame.image.load("BG.png")
background = pygame.transform.scale(background_original, (Resolutionx, Resolutiony))


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

while on==True and running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
            running=False
            print("here")
            on=False


    frame_index = (frame_index + 1) % len(frames)

    #screen.fill((0, 0, 0))  # optionnel
    screen.blit(frames[frame_index], (0, 0))

    pygame.display.flip()
    time.sleep(0.025)

    statement += 1






running=True
while running :
    
    if time.time()-counter>Spawing_bullets_delay:
        counter=time.time()
        game.player.launch_bullet()
    print(game.pressed)
    print(game.player.rect.x)





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
            print("collision")
            running=False
            pygame.quit()
            print("Succesfully closed")
            #À changer pour mettre un écran de fin

pygame.quit()










""" if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down/S")
            elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                print("Left/Q")
                game.player.move_left()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right/d")
                game.player.move_right()
            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                print("Up/Space")
"""
