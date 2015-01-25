'''
Created on 17.12.2014

@author: Morba
'''

import Tkinter

import pygame

from Game import *

root = Tkinter.Tk()
screen_width = 800#root.winfo_screenwidth()
screen_height = 1200#root.winfo_screenheight() 


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption('Dragonborn')
    Game().main(screen, screen_height, screen_width)
    print(pygame.ver)