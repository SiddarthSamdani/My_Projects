import random
import sys # sys.exit to exit the program
import pygame
from pygame.locals import * #Basic pygame imports
 
 #Global Variables for the game
 FPS = 32
 SCREENWIDTH = 289
 SCREENHEIGHT = 511
 SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
 GROUNDY = SCREENHEIGHT * 0.8
 GAME_SPRITES = {}
 GAME_SOUNDS = {}
 PLAYER = ''
 BACKGROUND = 
 PIPE = 

 if __name__ == "__main__":
     # Main point to start game
     pygame.init
     FPSCLOCK = pygame.time.Clock()
     pygame.display.set_caption('Flappy Bird')