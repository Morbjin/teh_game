'''
Created on 18.12.2014

@author: Morba
'''
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('E:\Dropbox\Pokemon_tildes\dragoran.png')
        self.rect = pygame.rect.Rect((500, 500), self.image.get_size())
        self.health = 100
        
        
    def update(self, dt):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if key[pygame.K_UP]:
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]:
            self.rect.y += 300 * dt

            