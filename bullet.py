import pygame
import random



class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.max_bullet_spawn_length=1300
        self.velocity_y = 5
        self.player = player
        self.image = pygame.image.load("Bullet.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect=self.image.get_rect()

        self.rect.x = random.randint(0,self.max_bullet_spawn_length)
        self.rect.y = 0
        self.bullet_spawning_speed = 1
        self.bool_angle_bullets=True

        

    def move(self):
        self.rect.y=self.rect.y+self.velocity_y

        if self.rect.y>600:
            self.remove()
    def remove(self):
        self.player.all_bullets.remove(self)
    def draw_debug(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


