class Board:
    board = ["0","1","2","3","4","5","6","7","8"]

    def printBoard(self):
        print(f"\r{self.board[0]} || {self.board[1]} || {self.board[2]} \n"+
              "______________\n"
               + f"\r{self.board[3]} || {self.board[4]} || {self.board[5]} \n"+
               "_____________\n"+
                f"\r{self.board[6]} || {self.board[7]} || {self.board[8]}"
              )
    def playInAposition(self, player, position):
            if self.board[position] != "X" or self.board[position] != "O":
                self.board[position] = player
    def getNumberOfSpacesInBoard(self) -> int:
        spaces:int = 0;
        for space in self.board:
            if space != "X" and spaces != "O":
                spaces += 1;
        return spaces;
    def getBoard(self) -> list:
        return self.board

# player x or o 
class Player:
    def __init__(self, player):
        self.player = player
    def selectHumanPlayer(self):
        if self.player == "X":
            return "X"
        else:
            return "O"
    def selectAiPlayer(self):
        if self.player == "X":
            return "O"
        else:
            return "X"



class Game:
    def __init__(self, board, player, ai):
        self.board_object = board
        self.board = self.board_object.board
        self.player = player
        self.ai = ai
        
    def evaluate(self):
        # example board 
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8

        wins = [
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,4,8],
            [2,4,6],
        ]
        for win in wins:
            [a,b,c] = win
            if (self.board[a] == "X" or self.board[a] == "O") and (self.board[a] == self.board[b] and self.board[a] == self.board[c]):
                return self.board[b];
            else:
                if self.board_object.getNumberOfSpacesInBoard() == 0:
                    return 0
                

    def Minimax(self, isMax, depth) -> int:
        evaluation = self.evaluate()

        if evaluation == self.ai:
            return 1 * (self.board_object.getNumberOfSpacesInBoard()+1)
        if evaluation == self.player:
            return -1 * (self.board_object.getNumberOfSpacesInBoard()+1)
        if evaluation == 0:
            return 0
        
        
        if isMax == True:
            bestScore = -10000
            previousMove = ""
            for moves in range(9):
                if (self.board[moves] != self.player and self.board[moves] != self.ai):
                    previousMove = self.board[moves]
                    self.board_object.playInAposition(self.ai,moves) 
                    score = self.Minimax(isMax=False, depth=depth-1)
                    self.board[moves] = previousMove
                    bestScore = max(score , bestScore)
            return bestScore

        else:
            bestScore = 10000
            previousMove = ""
            for moves in range(9):
                if (self.board[moves] != self.player and self.board[moves] != self.ai):
                    previousMove = self.board[moves]
                    self.board_object.playInAposition(self.player,moves) 
                    score = self.Minimax(isMax=True, depth=depth-1)
                    self.board[moves ] = previousMove
                    bestScore = min(score , bestScore)
            return bestScore
        

    def bestPossibleMove(self):
        if self.evaluate() == "X":
            return
        if self.evaluate() == "O":
            return
        if self.evaluate() == 0:
            return
        bestScore:int = -1000000
        move = 0
        previousMove = ""
        for moves in range(9):
            if (self.board[moves] != self.player and self.board[moves] != self.ai):
                previousMove = self.board[moves]
                self.board_object.playInAposition(self.ai,moves) 
                score = self.Minimax(False, 5)
                self.board[moves] = previousMove
                if score > bestScore:
                    bestScore = max(score, bestScore)
                    move = moves
        self.board[move] = self.ai
        print("----------- ai move ---------------")
        self.board_object.printBoard()
        self.humanPlay()

    def humanPlay(self):
        spaces = self.board_object.getNumberOfSpacesInBoard()
        if spaces == 0:
            print("tie")
            return
        elif self.evaluate() == self.player:
            print(self.player, "wins")
            return
        elif self.evaluate() == self.ai:
            print(self.ai, "wins")
            return
        else:
            human_choice = int(input("Player "+ self.player+" please pick a spot: "))
            self.board_object.playInAposition(self.player, human_choice)
            print("-------------------- human player ---------- ---")
            self.board_object.printBoard()
            self.bestPossibleMove()

    def play(self):
        print("Game is Starting")
        self.bestPossibleMove()

    

board_object = Board()
x = str(input("pick a player X or O: "))
# proper use the upper case 
player_human = Player(player=x).selectHumanPlayer()
player_ai = Player(player=x).selectAiPlayer()
Game(board=board_object, player= player_human,ai=player_ai).play()