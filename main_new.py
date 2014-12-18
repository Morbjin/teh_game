'''
Created on 17.12.2014

@author: Morba
'''
import sys
import pygame
import pytmx
import Tkinter

root = Tkinter.Tk()
screen_width = 400#root.winfo_screenwidth()
screen_height = 680#root.winfo_screenheight() 

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('E:\Dropbox\Pokemon_tildes\dragoran.png')
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

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
            
class Game(object):
 
    def main(self, screen):
        
        clock = pygame.time.Clock()
        
        backround = pygame.image.load('C:\Users\Morba\Desktop\hintergrund.png')
        sprites = pygame.sprite.Group()
        spiru
        self.player = Player(sprites)
        
        while True:
        
            dt = clock.tick(30)
            
            for event in pygame.event.get():
                #Abfangen des UserInputs
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            sprites.update(dt /1000.)
            screen.blit(backround, (0, 0))
            sprites.draw(screen)
            pygame.display.flip()
        


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_height, screen_width))
    Game().main(screen)