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
        original_image_1 = pygame.image.load("bob mouvement 1.png").convert_alpha() #transparent background
        original_image_2 = pygame.image.load("bob mouvement 1.png").convert_alpha() #transparent background
        original_image_3 = pygame.image.load("bob mouvement 2.png").convert_alpha() #transparent background
        original_image_4 = pygame.image.load("bob mouvement 3.png").convert_alpha() #transparent background
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, 65, 75)
        self.rect.x = 156
        self.rect.y = 500
        self.image1 = pygame.transform.scale(original_image_1, (62, 82))
        self.image2 =  pygame.transform.scale(original_image_2, (62, 82))
        self.image3 =  pygame.transform.scale(original_image_3, (62, 82))
        self.image4 =  pygame.transform.scale(original_image_4, (62, 82))

    def move_right(self):
        self.rect.x = self.rect.x+self.velocity


    def move_left(self):
        self.rect.x = self.rect.x-self.velocity
    
    def jump1(self):
        #print("Jump 1:", self.rect.y)
        self.rect.y = self.rect.y-30
        #print(self.rect.y,"Jump 1")
    def jump2(self):
        #print("Jump 2:", self.rect.y)
        self.rect.y = self.rect.y-20
        #print("Jump 2:", self.rect.y)
    def jump3(self):
        #print("Jump 3:", self.rect.y)
        self.rect.y = self.rect.y-10
       # print(self.rect.y,"Jump 3")
    def jump4(self):
        #print("Jump 4:", self.rect.y)
        self.rect.y = self.rect.y
        #print(self.rect.y,"Jump 4")
    def jump5(self):
        #print("Jump 5:", self.rect.y)
        self.rect.y = self.rect.y+10
        #print(self.rect.y,"Jump 5")
    def jump6(self):
        #print("Jump 6:", self.rect.y)
        self.rect.y = self.rect.y+20
        #print(self.rect.y,"Jump 6")
    def jump7(self):
        #print("Jump 7:", self.rect.y)
        self.rect.y = self.rect.y+30
        #print(self.rect.y,"Jump 7")


    

    def launch_bullet(self):
        new_bullet = bullet(self)
        self.all_bullets.add(new_bullet)

    def draw_debug(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)