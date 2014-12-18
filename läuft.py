'''
Created on 17.12.2014

@author: Morba
'''
import sys
import pygame
import pytmx
import Tkinter
import Player

root = Tkinter.Tk()
screen_width = 800#root.winfo_screenwidth()
screen_height = 1200#root.winfo_screenheight() 


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
            
class Enemie(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Enemie, self).__init__(*groups)
        self.image = pygame.image.load('E:\Dropbox\Pokemon_tildes\pokeball_map.png')
        self.rect = pygame.rect.Rect((100, 100), self.image.get_size())
        self.radius = 50
        #self.health = health #100.0
        #self.mask = pygame.mask.from_surface(Surface, 127)
        
    def update(self, dt):
        key = pygame.key.get_pressed()
        board = pygame.mouse.get_pos()
        if key[pygame.K_KP8]:
            self.rect.x += board
        print ('tescht')
        if pygame.mouse.get_pressed()[0]:
            
            self.rect.x += 100 * dt
        #self.rect.x -= 50
            self.rect.y += 100 * dt
        #self.rect.x = board.
    
class Game(object):
 
    def main(self, screen):
        #Attribute von einer Game Instanze
        clock = pygame.time.Clock()
        backround = pygame.image.load('E:\Dropbox\Pokemon_tildes\Stadt_1.png')
        #SPRITES
        enemiegroup = pygame.sprite.LayeredUpdates()   
        #bargroup = pygame.sprite.Group()
        stuffgroup = pygame.sprite.Group()
        self.blockergroup = pygame.sprite.Group()
        playergroup = pygame.sprite.Group()
# LayeredUpdates instead of group to draw in correct order
        allgroup = pygame.sprite.LayeredUpdates()
        
        #sprites = pygame.sprite.Group()
        self.player = Player(playergroup, allgroup)
        self.enemie1 = Enemie(enemiegroup, allgroup)
        
        #Player.groups(self) = playergroup, allgroup
        #Enemie.groups = enemiegroup, allgroup
        
        Enemie._layer = 2
        Player._layer = 1
        
        #self.gegner1 = Enemie(sprites)
        
        #self.blockergroup = pygame.sprite.Group()
        wallgrafik = pygame.image.load('E:\Dropbox\Pokemon_tildes\pokeball_map.png')
        for x in range(0, screen_height, 16):
            for y in range(0, screen_width, 16):
                if x in (0, screen_height-16) or y in (0, screen_width-16):
                    wall = pygame.sprite.Sprite(self.blockergroup) 
                    wall.image = wallgrafik
                    wall.rect = pygame.rect.Rect((x, y), wallgrafik.get_size())
        allgroup.add(self.blockergroup)
        
        self.image = pygame.image.load('E:\Dropbox\Pokemon_tildes\dragoran.png')
        self.rect = pygame.rect.Rect((500, 500), self.image.get_size())        
        
        
        mainloop=True
        
        while mainloop:
        
            dt = clock.tick(30)
            
            for event in pygame.event.get():
                #Abfangen des UserInputs
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    mainloop = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    mainloop = False
                if event.type == pygame.KEYDOWN and pygame.K_i:
                    print ('Inventar in Progress')
                #if event.type == pygame.MOUSEMOTION:
                    
                    
            #pygame.sprite.spritecollideany(self.player.groups(), self.gegner1.groups(), False)
            allgroup.clear(screen, backround)
            allgroup.update(dt /1000.)
            #stuffgroup.update(dt /1000.)
            screen.blit(backround, (0, 0))
            allgroup.draw(screen)
            pygame.display.flip()
        


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption('Hallo Welt')
    Game().main(screen)