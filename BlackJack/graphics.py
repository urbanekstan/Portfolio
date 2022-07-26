from random import randint
from os import system
from time import sleep

 
from Deck import Deck
from Player import Player
from CardCounter import CardCounter


def graphics(message, Player1, Dealer, action):
    # Organizes display for readability
    system('clear')
    print(message)
    Player1.print()
    Dealer.print()
    print(action)
    sleep(1)

    return 0
