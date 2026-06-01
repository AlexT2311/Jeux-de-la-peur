import pygame
import random

# Image chargée UNE seule fois au niveau du module
_bullet_image = None

def _get_bullet_image():
    global _bullet_image
    if _bullet_image is None:
        img = pygame.image.load("Bullet.png").convert_alpha()
        _bullet_image = pygame.transform.scale(img, (50, 50))
    return _bullet_image

class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.max_bullet_spawn_length = 2400
        self.velocity_y = 5
        self.velocity_x = random.randint(-5,5)
        self.player = player
        self.image = _get_bullet_image()  # référence partagée, pas de reload
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.max_bullet_spawn_length)
        self.rect.y = 0

    def move(self):
        self.rect.y += self.velocity_y
        self.rect.x = self.rect.x+self.velocity_x
        if self.rect.y > 600:
            self.kill()  # retire de tous les groupes + libère la mémoire

    def draw_debug(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


