from random import randint
from os import system
from time import sleep

from Game import Game
from Deck import Deck
from Player import Player
from CardCounter import CardCounter


def main():

    system('clear')
    game = Game(3)
    game.playGame()

main()
