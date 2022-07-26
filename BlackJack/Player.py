from random import randint
from os import system
from time import sleep

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
        
    def dealMeACard(self, Deck): # Deck Object
        # Removes one card from the deck and assigns to hand
        card = Deck.dealACard()
        self.currentHandFV.append(card[0])
        self.currentHandS.append( card[1])
        self.currentHandIV.append(card[2]) 
        if card[0]=='A':
            self.numAces += 1

        return 0

    def doWeHaveBlackJack(self):
        # Do we have bj?
        # Determines final score if relevant
        self.finalHandValue = sum(self.currentHandIV)
        if (self.numAces == 1) and ( self.currentHandFV[0] in ['10','J','Q','K'] or self.currentHandFV[1] in ['10','J','Q','K'] ) and (len(self.currentHandFV)==2):
            self.hit   = 0
            self.stand = 1
            self.finalHandValue = 21

        return 0

    def countHand(self):
        # Count the current value of hand
         self.finalHandValue = sum(self.currentHandIV)
         # Did we bust?
         if self.finalHandValue > 21:
             self.bust = 1
             self.hit  = 0
         # Or do we have 21 w aces = 1?
         elif self.finalHandValue == 21:
             self.hit = 0
         # Or do we have 21 w aces = 11?
         # SIMPLIFIED LOGIC bc no splitting hand, etc
         elif (self.numAces > 0) and (self.finalHandValue == 11):
             self.finalHandValue = 21
             self.hit = 0
        # Or do we have an ace w low cards? Use ace = 11
         elif (self.numAces > 0) and (self.finalHandValue < 11):
             self.finalHandValue += 10
             self.hit = 0

         return 0

    def resetHandForNextRound(self):
        # Reset variables for next round
        self.hit            = 0 # Booleans
        self.bust           = 0 
        self.stand          = 0
        self.numAces        = 0 # Integers
        self.finalHandValue = 0 
        self.currentHandFV  = [] # Vector of Face Values    e.g. ['2','10','K','A']
        self.currentHandS   = [] # Vector of Suits          e.g. ['♠', '♥','♣','♦']
        self.currentHandIV  = [] # Vector of Integer Values e.g. [ 2 , 10, 10 , 1 ]
        return 0

    def print(self):
        # Prints player's current hand
        # https://stackoverflow.com/questions/31011395/python-print-unicode-character

        #self.currentHandFV  = [] # Vector of Face Values    e.g. ['2','10','K','A']
        #self.currentHandS   = [] # Vector of Suits          e.g. ['♠', '♥','♣','♦']
        num     = len(self.currentHandFV)
        t1,t3= '         ','         '
        if self.isDealer: t2 = 'Dealer:  '
        else            : t2 = 'Player 1:'
        print('         '+'┌───────┐'*num)
        for i in range(num):
            t1 =  t1 + '|' + str(self.currentHandFV[i]) + str('     |') if len(self.currentHandFV[i])==2 else t1 + '|' + str(self.currentHandFV[i]) + str('      |')
        print(t1)
        print('         ' + '|       |'*num)
        for i in range(num):
            t2 =  t2 + '|   ' + str(self.currentHandS[i]) + str('   |')
        print(t2)
        print('         '+'|       |'*num)
        for i in range(num):
            t3 =  t3 + '|     ' + str(self.currentHandFV[i]) + str('|') if len(self.currentHandFV[i])==2 else t3 + '|      ' + str(self.currentHandFV[i]) + str('|')
        print(t3)
        print('         '+'└───────┘'*num)
        
