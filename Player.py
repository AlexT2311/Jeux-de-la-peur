import pygame
from bullet import bullet
import random

#class player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        self.health = 1
        self.max_health = 1
        self.attack = 10
        self.velocity = 5
        self.all_bullets = pygame.sprite.Group()
        original_image_1 = pygame.image.load("WAZOWSKI ULTIME.png").convert_alpha() #transparent background
        original_image_2 = pygame.image.load("WAZOWSKI ULTIME 2.png").convert_alpha() #transparent background
        original_image_3 = pygame.image.load("WAZOWSKI ULTIME 3.png").convert_alpha() #transparent background
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, 65, 75)
        self.rect.x = 11
        self.rect.y = 500
        self.image1 = pygame.transform.scale(original_image_1, (62, 82))
        self.image2 =  pygame.transform.scale(original_image_2, (62, 82))
        self.image3 =  pygame.transform.scale(original_image_3, (62, 82))

    def move_right(self):
        self.rect.x = self.rect.x+self.velocity


    def move_left(self):
        self.rect.x = self.rect.x-self.velocity

    def launch_bullet(self):
        new_bullet = bullet(self)
        self.all_bullets.add(new_bullet)

    def draw_debug(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)