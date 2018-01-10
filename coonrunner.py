#!/usr/bin/env python

# Coon Runner 
# This is the main app, sort of a controller of all the sound, graphics, userinputs, gamelogic, time and space...

# Imports
import drawer                       # This controls the window and all the graphics drawn on it
import soundblaster                 # This plays bacground music and sound effects
import spriter                      # This controls the movement and animation of game objects
import mapper                       # This controls the map
import pygame                       # The marvelous Pygame library our bred and butter
from pygame.locals import *         # We also need Pygame's locals
import os.path                      # This is needed to determine absolute path to the Graphics, Music, Sound and Level folder
from sys import exit as AbandonShip # For instant quit
from random import randint          # For generating nice round random numbers

# This God-class will controll everything
class TheGame():
    def __init__(self):
        pass
    
    def go(self):
        pass

game = TheGame()

if __name__ == '__main__': 
    game.go()