from random import randint
from os import system
from time import sleep

def main():

    system('clear')
    game = Game(3)
    game.playGame()

def graphics(message, Player1, Dealer, action): # Organizes display for readability

'''
4 Classes
'''

class Game:
# Handles game play
    
    def __init__(self, maxRounds = 5):
        # Initialize the deck and players
        # Assuming only 2 players ~ dealer and me, but could scale up
        self.Deck         = Deck()
        self.Dealer       = Player(1)
        self.Me           = Player(0)
        self.CardCounter  = CardCounter()
        self.maxRounds    = maxRounds
        self.currentRound = 1

    def playGame(self): # Play the decided number of rounds
 
    def playRoundNumber(self, round): # Play one round of BlackJack

    def determineWhoWon(self): # Determines who won and prints results

class Player:
# Handles a player's hand and interaction w deck
    
    def __init__(self, isDealer = 0):
        # Tracks player's hand and game play values/booleans
        self.hit            = 0 # Booleans
        self.bust           = 0 
        self.stand          = 0
        self.isDealer       = isDealer
        self.numAces        = 0 # Integers
        self.finalHandValue = 0 
        self.currentHandFV  = [] # Vector of Face Values    e.g. ['2','10','K','A']
        self.currentHandS   = [] # Vector of Suits          e.g. ['♠', '♥','♣','♦']
        self.currentHandIV  = [] # Vector of Integer Values e.g. [ 2 , 10, 10 , 1 ]
        self.tempDealer     = [] # Vector for temp dealer handling
        
    def dealMeACard(self, Deck): # Removes one card from the deck and assigns to hand

    def doWeHaveBlackJack(self): # Do we?

    def countHand(self): # Count the current value of hand

    def resetHandForNextRound(self): # Reset variables for next round

    def print(self): # Prints player's current hand

class Deck:
# Tracks the deck, chooses cards
    
    def __init__(self, numDecks = 1): # Not ready for 2 yet
        # Tracks specific cards/suits, multiple decks
        self.suits    = ['♦','♥','♠','♣']
        self.numDecks = numDecks
        self.deck     = []        
        basisDeck     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
        for i in range(0, self.numDecks):
            self.deck.append(basisDeck)


    def dealACard(self): # Randomly picks which deck and card num
        return self.getCardFromCardNum(cardNum) # [faceVal, suit, intVal]

    def getCardFromCardNum(self, cardNum): # Determine Card face and value
        return [faceValue, suit, intValue] # [faceValue - '2','10','A', suit - ♥♦♣♠, intValue - 1]


class CardCounter():
# Invoked within Game class ~ Hi-Lo counting

    def __init__(self):
        # Tracks running count
        self.dealerHand = 0 # One round, dealer's side running count
        self.playerHand = 0
        self.runningCount = [] # Running count for each round
        self.rounds       = []
        self.hi = ['10','J','Q','K','A']
        self.lo = ['2','3','4','5','6']
        self.dealerFaces = []
        self.playerFaces = []
        self.dealerCounts= []
        self.playerCounts= []

    def calculateRunningCount(self, dealerFV, playerFV, currentRound): # Calculates the running Count after each round
    
    def showRunningCount(self): # Prompts if to display running count

    def endGameDisplay(self): # Displays closing information
