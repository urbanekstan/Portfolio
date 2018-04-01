# An abridged outline of BlackJack.py

# Possible Future Functionality:
#  -> Betting
#     -  The pot could be added to Game class
#     -  Player's bank and additional functions (eg. Double Down, Surrender, Insurance) could be added to Player class
#  -> Card Counting trainer
#     - This could be added to Deck class

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

    def playOneRound(self):

    def determineWhoWon(self):

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

    def dealMeIn(self, Deck): 

    def hitOrStand(self, Deck):

    def dealerHitOrStand(self):

    def resetHandForNextRound(self):


class Deck:
# Tracks the deck, chooses cards
    
    def __init__(self):
        # Tracks specific cards/suits, multiple decks
        self.numDecks = 2
        self.deck     = [ [1,2,..,52],[1,2,..,52] ]

    def dealACard(self):

    def getCardFromCardNum(self, cardNum):
