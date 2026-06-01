import pygame

#class player
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.zoom=1000
        original_image = pygame.image.load("Background.png").convert_alpha() #transparent background
        self.image = pygame.transform.scale(original_image, (self.zoom*(3000/768),self.zoom))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0



    def move_right(self):
        self.rect.x = self.rect.x+self.velocity
    def move_left(self):
        self.rect.x = self.rect.x-self.velocity
