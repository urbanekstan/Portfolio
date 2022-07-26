from random import randint
from os import system
from time import sleep

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


    def dealACard(self):
        # Randomly picks which deck and card num
        deckNum = randint(0, len(self.deck)-1)
        cardIdx = randint(0, len(self.deck[deckNum])-1)
        cardNum = self.deck[deckNum][cardIdx]
        self.deck[deckNum].pop(cardIdx)

        return self.getCardFromCardNum(cardNum) # [faceVal, suit, intVal]

    def getCardFromCardNum(self, cardNum):
        # Determine Card face and value
        cardNum=cardNum-1
        suitIdx = cardNum%4
        suit = self.suits[cardNum % 4]
        face = cardNum // 4
        if   face == 0: faceValue, intValue = 'A', 1
        elif face == 1: faceValue, intValue = '2', 2
        elif face == 2: faceValue, intValue = '3', 3
        elif face == 3: faceValue, intValue = '4', 4
        elif face == 4: faceValue, intValue = '5', 5
        elif face == 5: faceValue, intValue = '6', 6
        elif face == 6: faceValue, intValue = '7', 7
        elif face == 7: faceValue, intValue = '8', 8
        elif face == 8: faceValue, intValue = '9', 9
        elif face == 9: faceValue, intValue = '10', 10
        elif face == 10: faceValue, intValue = 'J', 10
        elif face == 11: faceValue, intValue = 'Q', 10
        elif face == 12: faceValue, intValue = 'K', 10
        else:print('GET CARD FROM CARD NUM IS BROKEN!!! face ' + str(face))
        
        return [faceValue, suit, intValue] # [faceValue - '2','10','A', suit - ♥♦♣♠, intValue - 1]

