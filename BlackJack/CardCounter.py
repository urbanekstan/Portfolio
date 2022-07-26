from random import randint
from os import system
from time import sleep


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
