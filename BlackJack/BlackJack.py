from random import randint
from os import system
from time import sleep
 
from Deck import Deck
from Player import Player
from CardCounter import CardCounter
from Game import Game

def main():

    #system('clear')
    game = Game(3)
    game.playGame()

'''
def graphics(message, Player1, Dealer, action):
    # Organizes display for readability
    system('clear')
    print(message)
    Player1.print()
    Dealer.print()
    print(action)
    sleep(1)

    return 0
'''
'''
# BlackJack Game w Card Counting Trainer
# By Stan Urbanek
#!python3.6

# 4 Classes:
#  -> Game   - Handles game play. Game contains all other objects
#  -> Deck   - Tracks the deck, chooses cards 
#  -> Player - Handles player's hand and interaction w deck
#  -> CardCounter - Counts cards, logs and displays hands

# Card trainer implements a hi-lo count
# Dealer hits on hard 16, soft 17

# Possible Future Functionality:
#  -> Betting
#     -  The pot would be added to Betting class, contained w/in Game
#     -  Player's bank and additional functions (eg. Double Down, Surrender, Insurance) would be added to Player class

# ---------------------------------------------------------
'''

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


    def playGame(self):
        # Play the decided number of rounds
        # Uses depleted deck from last round
        system('clear')
        openingText = 'The BlackJack Card Counting Trainer\n ~ Uses Hi-Lo Counting Strategy\n ~ By Stan Urbanek\n\n'
        blackJackRules = 'Quick BlackJack Rules:\n ~ The object of the game is to get as close to 21 without going over\n ~ Go over 21 and you bust (lose)\n ~ Each player is dealt 2 cards (Aces count as either 1 or 11\n ~ Players then choose between \n   ~ Hitting (drawing) a card from the deck\n   ~ Standing (staying) w current hand \n\n'
        cardCounter = 'Hi-Lo Counting Strategy:\n ~ For every card displayed\n     Hi Cards    10 J Q K A => RunningCount - 1 \n     Lo Cards     2 3 4 5 6 => RunningCount + 1\n     Zero Cards   7 8 9     => RunningCount + 0\n    (The logic is that as the favorable Hi cards are used up, there are fewer Hi cards for you to get later in the game)\n ~ Your bet size would be proportional to this running count \n\nWe will try a ' + str(self.maxRounds-1) + ' round game. \nYou are given the option at the end of each round to look at the running count. \n\n[Press ENTER to start]'
        howToCount = 'Recommended way to count: \n ~ Wait '
        
        print(openingText + blackJackRules + cardCounter)
        input('')
        
        while (self.currentRound != self.maxRounds):
            self.Me.resetHandForNextRound()
            self.Dealer.resetHandForNextRound()
            self.playRoundNumber(self.currentRound)

            self.CardCounter.calculateRunningCount(self.Dealer.currentHandFV, self.Me.currentHandFV,self.currentRound)
            self.CardCounter.showRunningCount()
            
            self.currentRound += 1
            
        self.CardCounter.endGameDisplay()
        
        return 0
    
    def playRoundNumber(self, round):
        # Play one round of BlackJack
        # First deal everybody 1st
        banner = 'Round ' + str(round)
        self.Me.dealMeACard(self.Deck)
        graphics(banner, self.Me, self.Dealer, 'Dealing Players...')
        self.Dealer.dealMeACard(self.Deck)
        graphics(banner, self.Me, self.Dealer, 'Dealing Players...')
        # Next deal everybody 2nd
        self.Me.dealMeACard(self.Deck)
        graphics(banner, self.Me, self.Dealer, 'Dealing Players...')
        # TEMP DEALER OBFUSCATION
        self.Dealer.dealMeACard(self.Deck)
        self.Dealer.tempDealer.append(self.Dealer.currentHandFV[1])
        self.Dealer.tempDealer.append(self.Dealer.currentHandS[1])
        self.Dealer.currentHandFV[1] = '?'
        self.Dealer.currentHandS[1]  = '?'
        graphics(banner, self.Me, self.Dealer, 'Dealing Players...')
        # Ask player 1 input
        self.Me.doWeHaveBlackJack()
        if self.Me.stand: # We have blackjack
            graphics(banner, self.Me, self.Dealer, 'Player 1 has Black Jack!')
            # Now dealers turn
        else: # Otherwise, hit or stand?
            graphics(banner, self.Me, self.Dealer, 'Player 1, do you Hit or Stand? (1) Hit (0) Stand: ')
            user = int(input(':'))
            if user: self.Me.stand, self.Me.hit = 0, 1
            else   :
                self.Me.stand, self.Me.hit = 1, 0
                self.Me.countHand()
            while self.Me.hit:
                # Deal me a card and examine hand
                self.Me.dealMeACard(self.Deck)
                self.Me.countHand()
                # If bust
                if self.Me.bust:
                    self.Me.hit = 0
                    graphics(banner, self.Me, self.Dealer,'Player 1 busts')
                # If 21
                elif self.Me.finalHandValue == 21:
                    self.Me.hit = 0
                    graphics(banner, self.Me, self.Dealer, 'Player 1 has 21')
                # Otherwise, hit again?
                else:
                    graphics(banner, self.Me, self.Dealer, 'Player 1, do you Hit Or Stand? (1) Hit (0) Stand: ')
                    self.Me.hit = int(input(''))
                
        # Dealer Turn
        # REVERSE DEALER OBFUSC ~
        self.Dealer.currentHandFV[1] = self.Dealer.tempDealer[0]
        self.Dealer.currentHandS[1]  = self.Dealer.tempDealer[1]
        graphics(banner, self.Me, self.Dealer, 'Dealer reveals ' + str(self.Dealer.currentHandFV[1]) + ' ' + str(self.Dealer.currentHandS[1]))

        # 
        self.Dealer.doWeHaveBlackJack()
        if self.Dealer.stand: # We have blackjack
            print('Dealer has Black Jack')
            sleep(1)
            #graphics(banner, self.Me, self.Dealer, 'Dealer has Black Jack!')
            # End and compare values
        else: # Otherwise, hit or stand?
            self.Dealer.countHand()
            if (self.Dealer.finalHandValue < 17):
                self.Dealer.hit = 1
                print('Dealer hits')
                sleep(1)
            else:
                self.Dealer.hit = 0
                print('Dealer stands')
                sleep(1)
            while self.Dealer.hit:
                self.Dealer.dealMeACard(self.Deck)
                self.Dealer.countHand()
                # If bust
                if self.Dealer.bust:
                    self.Dealer.hit = 0
                    graphics(banner, self.Me, self.Dealer,'Dealer busts')
                # If 21
                elif self.Dealer.finalHandValue == 21:
                    self.Dealer.hit = 0
                    graphics(banner, self.Me, self.Dealer, 'Dealer has 21')
                # Otherwise, hit again?
                else:
                    if self.Dealer.finalHandValue < 17:
                        self.Dealer.hit = 1
                        graphics(banner, self.Me, self.Dealer, 'Dealer hits again')
                    else: self.Dealer.hit = 0
                    
        self.determineWhoWon()
        
        return 0


    def determineWhoWon(self):
        # Determines who won and prints results
        # Did I bust?
        if (self.Me.finalHandValue > 21): print('Player 1 loses')
        # No bust ~ did dealer bust? -> I win
        elif (self.Dealer.finalHandValue > 21): print('Player 1 wins')
        # Both valid scores ~ who is higher?
        elif (self.Me.finalHandValue > self.Dealer.finalHandValue): print('Player 1 wins')
        elif (self.Me.finalHandValue < self.Dealer.finalHandValue): print('Dealer wins')
        elif (self.Me.finalHandValue == self.Dealer.finalHandValue): print('Tie')
        else: print('determineWhoWon broke')
        
        return 0
'''
'''
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
'''
'''        
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
'''
'''
class CardCounter():
# Counts cards based on Hi-Lo strategy

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

    def calculateRunningCount(self, dealerFV, playerFV, currentRound):
        # Calculates the running Count after each round
        self.rounds.append(currentRound)
        self.dealerHand = 0
        self.playerHand = 0
        # Dealer hands
        dealerSave = ''
        for i in range(len(dealerFV)):
            dealerSave = dealerSave + ' ' + str(dealerFV[i])
            if dealerFV[i] in self.hi:
                #print('dealerFV[i] in self.hi' + str(dealerFV[i]) + ' ' + str(self.hi))
                self.dealerHand -= 1
            elif dealerFV[i] in self.lo:
                #print('dealerFV[i] in self.lo' + str(dealerFV[i]) + ' ' + str(self.lo))
                self.dealerHand += 1
        self.dealerCounts.append(self.dealerHand)
        # Player hands
        playerSave = ''
        for j in range(len(playerFV)):
            playerSave = playerSave + ' ' + str(playerFV[j]) 
            if playerFV[j] in self.hi:
                self.playerHand -= 1
            elif playerFV[j] in self.lo:
                self.playerHand += 1
        self.playerCounts.append(self.playerHand)
        self.dealerFaces.append(dealerSave)
        self.playerFaces.append(playerSave)
        self.runningCount.append(self.dealerHand + self.playerHand)
        
        return 0
    
    def showRunningCount(self):
        # Prompts if to display running count
        display = int(input('What is running count? '))
        if display:
            print('\n> Player 1      : ' + str(self.playerHand))
            print('> Dealer        : ' + str(self.dealerHand))
            print('> Running Count : ' + str(sum(self.runningCount))+'\n')   
            print('[Notes  : Player 1 and Dealer are local hand sums ]')
            print('[       : Treat each player\'s hand as one +/- count] ')
            print('[       : Running Count is net cumulative total   ] \n')
            x = input('[Press ENTER to Proceed]')

        return 0

    def endGameDisplay(self):
        # Displays closing information
        system('clear')
        text = 'Game is done. Now for your post game analysis: \n'
        print(text)
        print(  ' Rounds: ' + str(max(self.rounds)))
        print('\n Dealer Cardlog ' + str(self.dealerFaces))
        print(' Player Cardlog ' + str(self.playerFaces))
        print('\n Dealer counts    ' + str(self.dealerCounts))
        print(' Player counts    ' + str(self.playerCounts))
        print('\n Running Count  ' + str(self.runningCount))
        print(' True Count*    ' + str(self.runningCount))
        print(' Bet^           ' + 'Will add later')

        print(' \n\n*True Count is used to determine how to bet. \n True Count = [Running Count] / [Decks left ~ rounded to nearest 1/2 deck] \n Decks left ~ 1 and 0.5 in our case')
        print('\n^Bet is the recommended bet\n Bet = TrueCount - 1 ( Betting Unit)\n Assume 1 Betting Unit = $100')
        print('Subtract 1 from the True Count to determine how many units to bet. Multiply the number of units to bet by your betting unit. \n\nFor Example, your betting unit is 100, running count is +10, true count is +5, then the optimal bet would be 4X100 which gives us 400.')


'''        


main()
