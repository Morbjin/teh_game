__author__ = 'Morba'
'''
Created on 17.12.2014

@author: Morba
'''
import sys

import pygame

# import pytmx
# import Tkinter
# import Player

# root = Tkinter.Tk()
screen_width = 800  # root.winfo_screenwidth()
screen_height = 1200  # root.winfo_screenheight()


class Player(pygame.sprite.Sprite):
    def __init__(self, startpos=(500, 500),*groups):
        super(Player, self).__init__(*groups)
        #self.pos = [0.0, 0.0]
        #self.pos[0] = startpos[0]
        #self.pos[1] = startpos[1]
        self.image = pygame.image.load('E:\Dropbox\Pokemon_tildes\dragoran.png')
        self.rect = pygame.rect.Rect((500, 500), self.image.get_size())
        self.name = 'Held'
        self.health = 100
        self.radius = 50
        self.death = False

    def set_death(self):
        self.death = True
        print("Sie haben "+self.get_name()+" getoetet")
        self.kill()
        return self.death

    def get_name(self):
        return self.name

    def update(self, dt):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x = 300 * dt
        if key[pygame.K_UP]:
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]:
            self.rect.y = 300 * dt


    def attack(self, target, schaden=10):
        target.set_health(schaden)
        print( "Hier sollte etwas mit DMG passieren")
        return

    def set_health(self, schaden):
        if (self.health - schaden) <= 0:
            self.set_death()
        else:
            self.health -= schaden
            print( self.get_name()+" erleidet" +str(schaden)+ " Schaden!")
        print (self.get_name()+" hat noch "+str(self.get_health())+"Leben")
        return self.health

    def get_health(self):
        return self.health

    def get_death(self):
        return self.death

    def move(self, dx, dy):





class Enemie(Player, pygame.sprite.Sprite):
    image = []
    # image.append(pygame.image.load('E:\Dropbox\Pokemon_tildes\pokeball_map.png'))
    all_enemies = {}
    number = 0
    # def __init__(self):
    #    pygame.sprite.Sprite.__init__(self, self.groups)
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('E:\Dropbox\Pokemon_tildes\pokeball_map.png')
        self.rect = pygame.rect.Rect((100, 100), self.image.get_size())
        self.name = 'Monster'
        self.health = 100
        self.radius = 50
        self.death = False
        # self.mask = pygame.mask.from_surface(Surface, 127)
        Enemie.number += 1
        Enemie.all_enemies[self.number] = self

    def update(self, dt):
        #last = self.rect.copy()

        key = pygame.key.get_pressed()
        board = pygame.mouse.get_pos()
        if key[pygame.K_KP8]:
            self.rect.x = board[0]
            self.rect.y = board[1]
        if pygame.mouse.get_pressed()[0]:
            self.rect.x = 100 * dt
            # self.rect.x -= 50
            self.rect.y = 100 * dt
            # self.rect.x = board.


class Game(object):
    def main(self, screen):
        # Attribute von einer Game Instanze
        clock = pygame.time.Clock()
        backround = pygame.image.load('E:\Dropbox\Pokemon_tildes\Stadt_1.png')
        # Sprites
        enemiegroup = pygame.sprite.LayeredUpdates()
        # bargroup = pygame.sprite.Group()
        # stuffgroup = pygame.sprite.Group()
        blockergroup = pygame.sprite.Group()
        playergroup = pygame.sprite.Group()
        # LayeredUpdates instead of group to draw in correct order
        allgroup = pygame.sprite.LayeredUpdates()



        Player.groups = playergroup, allgroup
        Enemie.groups = enemiegroup, allgroup

        player = Player(playergroup, allgroup)
        enemie1 = Enemie(enemiegroup, allgroup)


# Niedriger ist Hintergrund
        Enemie._layer = 1
        Player._layer = 2

        wallgrafik = pygame.image.load("E:\Dropbox\Pokemon_tildes\pokeball_map.png")
        for x in range(0, screen_height, 16):
            for y in range(0, screen_width, 16):
                if x in (0, screen_height - 16) or y in (0, screen_width - 16):
                    wall = pygame.sprite.Sprite(blockergroup)
                    wall.image = wallgrafik
                    wall.rect = pygame.rect.Rect((x, y), wallgrafik.get_size())
        allgroup.add(blockergroup)

        mainloop = True

        while mainloop:

            dt = clock.tick(30)

            for event in pygame.event.get():
                # Abfangen des UserInputs
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                    print ('Inventar in Progress')
                    # if event.type == pygame.MOUSEMOTION:

            hitrange = pygame.sprite.spritecollide(player, enemiegroup, False)

            for inrange_enemie in hitrange:
                # enemie1.set_health(10)
                print ("Gegner in Hitrange")
                if pygame.mouse.get_pressed()[0]:
                    player.attack(inrange_enemie)
                    print (player.get_name()+" greift "+enemie1.get_name()+" an!")

            last_rec_player = player.rect.copy()
            last_rec_enemie1= enemie1.rect.copy()

            for noob in pygame.sprite.spritecollide(player, blockergroup, False):
                player.rect = last_rec_player
            for noob in pygame.sprite.spritecollide(enemie1, blockergroup, False):
                enemie1.rect = last_rec_enemie1


            # pygame.sprite.spritecollideany(self.player.groups(), self.gegner1.groups(), False)
            allgroup.clear(screen, backround)
            allgroup.update(dt / 1000.)
            # stuffgroup.update(dt /1000.)
            screen.blit(backround, (0, 0))
            allgroup.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption('Dragonborn')
    Game().main(screen)
