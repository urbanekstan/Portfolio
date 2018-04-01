def main():
    print('yo')
    deck = Deck(1)
    a = deck.dealACard()
  
'''
# By Stan Urbanek

#!python3.6
#coding: utf8
#https://stackoverflow.com/questions/31011395/python-print-unicode-character


# Primary Objectives: Clearly lay out structure for BlackJack game
#                   : Show which variables are handled within each function
#                   : Design w future functionality in mind

# Acknowledgements  : Function logic not complete 
#                   : Syntax not necessarily correct

# Game Play         : Dealer and Player 1 are dealt hands from Deck. After seeing Dealer's 1 card and own hand, Player 1 decides to hit or stand until finished. Game continues for set number of rounds.

# 3 Classes:
#  -> Deck   - Tracks the deck, chooses cards 
#  -> Player - Handles player's hand and interaction w deck
#  -> Game   - Handles game play

# Possible Future Functionality:
#  -> Betting
#     -  The pot would be added to Game class
#     -  Player's bank and additional functions (eg. Double Down, Surrender, Insurance) would be added to Player class
#  -> Card Counting trainer
#     - This would be added to Deck class

# Card train implements a hi-lo count
# ---------------------------------------------------------
'''
from random import randint

class Game:
# Handles game play
    
    def __init__(self, maxRounds = 5):
        # Initialize the deck and players
        # Assuming only 2 players ~ dealer and me, but could scale up
        self.Deck         = Deck()
        self.Dealer       = Player()
        self.Me           = Player()
        self.maxRounds    = maxRounds
        self.currentRound = 1

    def playGame(self):
        # Play the decided number of rounds
        # Uses depleted deck from last round
        while (self.currentRound != self.maxRounds):
            self.Me.resetHandForNextRound()
            self.Dealer.resetHandForNextRound()
            self.playOneRound()
            self.currentRound += 1

        return 0
    
    def playOneRound(self):
        # Play one round of BlackJack
        # First deal everybody
        self.Me.dealMeIn(self.Deck)
        self.Dealer.dealMeIn(self.Deck)
        # Print 1 dealer card
        print('Dealer Face up card: ' + str(self.Dealer.currentHand[0]))
        # Hit or Stand for everybody
        self.Me.hitOrStand(self.Deck)
        self.Dealer.dealerHitOrStand(self.Deck)  
        # Determine who won
        self.determineWhoWon()
        
        return 0

    def determineWhoWon(self):
        # Determines who won and prints results
        if self.Me.bust:
            print('BUST - You lost')
        elif self.Me.has21:
            print('21 - You win')
        elif (self.Me.finalHandValue < self.Dealer.finalHandValue):
            print('DEALER won')
        elif (self.Me.finalHandValue == self.Dealer.finalHandValue):
            print('TIE')
        elif (self.Me.finalHandValue > self.Dealer.finalHandValue):
            print('YOU won')

        return 0


class Player:
# Handles a player's hand and interaction w deck
    
    def __init__(self):
        # Tracks player's hand and game play values/booleans 
        self.bust           = 0 # Booleans
        self.stand          = 0
        self.has21          = 0
        self.isDealer       = 0
        self.numAces        = 0 # Integers
        self.finalHandValue = 0 
        self.currentHandFV  = [] # Vector of Face Values    e.g. ['2','10','K','A']
        self.currentHandS   = [] # Vector of Suits          e.g. ['♠', '♥','♣','♦']
        self.currentHandIV  = [] # Vector of Integer Values e.g. [ 2 , 10, 10 , 1 ]

    def dealMeACard(self, Deck): # Deck Object
        # Removes one card from the deck and assigns to hand
        card = deck.dealACard()
        self.currentHand.append(card[0])
        self.currentHandValues.append(card[1])
        if card[1] == 1:
            self.numAces += 1

        return 0

    def dealMeIn(self, Deck): # Deck Object
        # Deals player 2 cards
        self.dealMeACard(Deck)
        self.dealMeACard(Deck)

        return 0

    def hitOrStand(self, Deck):
        # Interacts w player to determine hit or stand, bust
        # Fcn determines final player score
        print(self.currentHand)
        # If A and T/J/Q/K, you win
        if (['A','T','J','Q','K'] in self.currentHand[0][0]) and (['A','T','J','Q','K'] in self.currentHand[1][0]):
            self.win = 1
            self.stand = 1
            self.finalHandValue = 21
            return 0
        # Otherwise, stand/hit loop
        self.stand = input('Press (1) for stand, (0) for hit')
        '''
        while !self.stand:
           # [Incomplete ~ Prompts user to hit, prompts Ace usage, checks card totals
            self.finalHandValue = 18
        '''
        return 0

    def dealerHitOrStand(self):
        # Does hit or stand for dealer
        # Determines final dealer score
        # [Incomplete ~ Uses similar but automated logic as self.hitOrStand()]
        self.finalHandValue = 15 # HC'd
        
        return 0

    def resetHandForNextRound(self):
        # Reset variables for next round
        self.bust = 0
        self.stand = 0
        self.numAces = 0
        self.currentHand = []
        self.currentHandValues = []

        return 0

    def print(self):
        # Prints player's current hand
        # https://stackoverflow.com/questions/31011395/python-print-unicode-character

        #self.currentHandFV  = [] # Vector of Face Values    e.g. ['2','10','K','A']
        #self.currentHandS   = [] # Vector of Suits          e.g. ['♠', '♥','♣','♦']
        num     = len(self.currentHandFV)
        t1,t2,t3= '','',''
        print('┌───────┐'*num)
        for i in range(num):
            #t1 =  t1 + '|' + str(faceVal[i]) + str('     |') if len(faceVal[i])==2 else t1 + '|' + str(faceVal[i]) + str('      |')
            t1 =  t1 + '|' + str(self.currentHandFV[i]) + str('     |') if len(self.currentHandFV[i])==2 else t1 + '|' + str(self.currentHandFV[i]) + str('      |')
        print(t1)
        print('|       |'*num)
        for i in range(num):
            #t2 =  t2 + '|   ' + str(suit[i]) + str('   |')
            t2 =  t2 + '|   ' + str(self.currentHandS[i]) + str('   |')
        print(t2)
        print('|       |'*num)
        for i in range(num):
            #t3 =  t3 + '|     ' + str(faceVal[i]) + str('|') if len(faceVal[i])==2 else t3 + '|      ' + str(faceVal[i]) + str('|')
            t3 =  t3 + '|     ' + str(self.currentHandFV[i]) + str('|') if len(self.currentHandFV[i])==2 else t3 + '|      ' + str(self.currentHandFV[i]) + str('|')
        print(t3)
        print('└───────┘'*num)

        
class Deck:
# Tracks the deck, chooses cards
    
    def __init__(self, numDecks = 1):
        # Tracks specific cards/suits, multiple decks
        self.faceVals = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.suits    = ['♠','♥','♣','♦']
        self.numDecks = numDecks
        self.deck     = []
        
        basisDeck     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
        for i in range(0, self.numDecks):
            self.deck.append(basisDeck)
        print(self.deck)


    def dealACard(self):
        # Randomly picks which deck and card num
        deckNum = randint(0, len(self.deck))
        cardIdx = randint(0, len(self.deck[deckNum]))
        cardNum = self.deck[deckNum][cardIdx]
        self.deck[deckNum].pop(cardIdx)

        return self.getCardFromCardNum(cardNum) # [faceVal, suit, intVal]

    def getCardFromCardNum(self, cardNum):
        # Determine Card face and value
        # [Incomplete ~ Uses integer division and modulus functions]

        return [faceValue, suit, intValue] # [faceValue - '2','10','A', suit - 1,2,3,4 ~ ♥♦♣♠, intValue - 1]




main()