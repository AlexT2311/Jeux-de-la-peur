import pygame
import random

#Managing bullet shooting class

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("Bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1400)
        self.rect.y = 0
        self.image = pygame.transform.scale(self.image, (50, 50))

