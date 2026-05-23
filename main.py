import pygame
from Player import Player
from bullet import bullet
import random
import time

pygame.init()

#Frame creator
pygame.display.set_caption("Les Jeux de la peur")
screen=pygame.display.set_mode((1400,750))

class Game:
    def __init__(self):
        self.player=Player()
        self.pressed={}


def game_over():
    print("game over")




background_original = pygame.image.load("BG.png")
background = pygame.transform.scale(background_original, (1400, 750))


running=True

#Game instance

game=Game()



#While pour maintenir la fenetre
counter=time.time()
while running:
    
    if time.time()-counter>0.5:
        counter=time.time()
        game.player.launch_bullet()
    print(game.pressed)
    print(game.player.rect.x)



    if (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d)) and game.player.rect.x<1300:
        print("Right/d")
        game.player.move_right()
    if (game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q)) and game.player.rect.x>0:
        print("Left/Q")
        game.player.move_left()
    
    

    #display bg
    screen.blit(background, (0,0))

    #player display
    screen.blit(game.player.image, game.player.rect)

    #bullet group display
    game.player.all_bullets.draw(screen)

    #refresh screen
    pygame.display.flip()



 
    for event in pygame.event.get():     #pygame event return une list de chaque event, la variale event c'est le dernier event
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
        bullet.bool_angle_bullets=True
        if game.player.rect.y<bullet.rect.y+10 and game.player.rect.colliderect(bullet.rect):
            game_over()
            bullet.kill()











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
