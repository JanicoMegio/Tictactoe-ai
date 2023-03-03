import random
import time
# **************************************************************
# Simple TicTacToe Game with some fun AI look Siri versus Alexa
# It automatically play and see if whos gonna win!
# *** It has many bugs feel free to modify it! Enjoy :) ***
# Created by ** Janico Megio ** 
# **************************************************************
class tictactoe:
    
    def __init__(self, board, player, gamerunning, winner, statso, statsx, tie):
        self.board = board
        self.player = player
        self.gamerunning = gamerunning
        self.winner = winner
        self.statso = statso
        self.statsx = statsx
        self.tie = tie
        
    # Start Here -- ** Display the board ** 
    def displayboard(self):
        print("-------")
        print(f"|{self.board[0]}|{self.board[1]}|{self.board[2]}|")
        print("-------")
        print(f"|{self.board[3]}|{self.board[4]}|{self.board[5]}|")
        print("-------")
        print(f"|{self.board[6]}|{self.board[7]}|{self.board[8]}|")
        print("-------")
        
    # Start Here -- ** random place of "X" to board **
    
    def siri(self):
        if self.player == 'X':
            com = random.randint(0, 8) # generate random number from 0 - 8
            if self.board[com] == '-': # checking the board if it can place "X"
                self.board[com] = "X" # replace '-' to "X"
                self.player = "O" # player value replace to 'O' 
                self.displayboard() 
                print(f"Siri(X) place: {com+1}")
            
                    
    def Alexa(self):
        if self.player == "O":
            com = random.randint(0, 8)
            if self.board[com] == '-':
                self.board[com] = "O" 
                self.player = "X"
                self.displayboard()
                print(f"Alexa(O) place: {com+1}")
           
    #  Here --- ** Check all pattern **\
        # Check the Row of board if are equal
    def  checkrow(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        if self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True

        # Check the column of board if are equal
    def checkcolumn(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0] # Set the value of winner
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True

        # Check the diagonal of board if are equal
    def checkdiag(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
    # End Here -- 

    # Here -- Check the board if it's not contains '-'
    def checktie(self):
        if '-' not in self.board:
            print("=======")
            print('\033[96m')
            self.displayboard()
            print("It's a Tie!")
            print('\033[0m')
            self.tie += 1
            for i, n in enumerate(self.board):
                # replace the board value to '-'
                self.board[i] = "-"
            return self.tie
        
    # Start Here -- ** Check the winner ** 
    def checkwon(self):
        # Check the boolean value of pattern  
        if self.checkrow() or self.checkcolumn() or self.checkdiag(): 
            self.gamerunning += 1
            self.player = "X"
            print("=======")
            print('\033[92m')
            self.displayboard()
            print('\033[0m')
            if self.winner == 'X':
                print(f'\033[92m'+'SIRI Win!..'+'\033[0m')
                self.statsx += 1
            else:
                print(f'\033[92m'+'Alexa Win!..'+'\033[0m')
                self.statso += 1
            for i, n in enumerate(self.board): # replace the board value to '-'
                self.board[i] = "-"
            print("", end=" ")
            
    # Start Here -- ** Front design and to the end of program            
    def display(self):
        print("==============")
        print("SIRI VS. Alexa")
        print("TICTACTOE GAME")
        print("SIRI: X Alexa: O")
        print("==============")
        
    def stats(self):
        print()
        print()
        print("##############")
        self.display()
        print(f"X: {self.statsx} O: {self.statso} TIE: {self.tie}")
        print("===============")
        if self.statsx > self.statso:
            print('\033[1m'+"SIRI"+'\033[0m'+" IS THE "+'\033[92m'+"WINNER!!"+'\033[0m'+"..")
        else:
            print('\033[1m'+"Alexa"+'\033[0m'+" IS THE "+'\033[92m'+"WINNER!!"+'\033[0m'+"..")
        print("==============")
        print("##############")
    # End Here -- **
        
    # Here -- ** Run all the function **
    def game(self):
        while self.gamerunning != 5:
            self.siri()
            time.sleep(0.4)
            self.Alexa()
            self.checkwon()
            self.checktie()
        else:
            self.stats()
        time.sleep(10)


if __name__ == "__main__":
    
    play = tictactoe(['-','-','-',
                      '-','-','-',
                      '-','-','-'],
                     "X", 0, None, 0, 0, 0)
    play.display()
    time.sleep(3)
    play.game()
        
        