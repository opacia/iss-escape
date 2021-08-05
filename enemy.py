import pygame
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, texture: pygame.Surface, speed: float):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.texture = texture
        self.speed = speed
        self.rect = texture.get_rect()

    def move(self):
        self.pos_y += self.speed
