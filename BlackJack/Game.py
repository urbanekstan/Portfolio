from random import randint
from os import system
from time import sleep

from Deck import Deck
from Player import Player
from CardCounter import CardCounter
from graphics import graphics

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

