from random import randint
from os import system
from time import sleep

from Game import Game
from Deck import Deck
from Player import Player
from CardCounter import CardCounter
from graphics import graphics

def main():

    system('clear')
    game = Game(3)
    game.playGame()

main()
