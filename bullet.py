import pygame
import random

#Managing bullet shooting class

class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("Bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1400)
        self.rect.y = 0
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.bullet_spawning_speed = 1
        self.bool_angle_bullets=True
        

    def move(self):
        if self.bool_angle_bullets==True:
            self.angle_bullets=random.randint(-5,5)
            self.bool_angle_bullets=False
        self.rect.y=self.rect.y+self.velocity
        self.rect.x=self.rect.x+self.angle_bullets
        if self.rect.y>600:
            self.player.all_bullets.remove(self)
            print("AHHHHHHHHHHHHHHHHHH")
    def remove(self):
        self.player.all_bullets.remove(self)


