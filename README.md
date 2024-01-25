# python-3-tic-tac-toe-using-minimax-algorithm
The Minimax Algorithm is a recursive decision making algorithm. In the code I used the Minimax algorithm to help my Artificail Intelligent player to decide where to play next.

## How it works 
![a2xk9nor](https://github.com/S-Immanuel01/python-3-tic-tac-toe-minimax-/assets/142397823/91543631-bd18-4454-adcb-084f65840a4b)

The minimax algorithm uses recursion to test every possibility of the game (giving each possibility a utility value/ score) and picks the optimal path for a definite win. Ofcourse all this is done with the Assumption that the human player is also playing optimally to Maximize his score and minimize the AI player score.

The function responsible for choices is the `bestMove` function
```python
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
```

### Pictures of One of my random games against the AI player
![Screenshot (22)](https://github.com/S-Immanuel01/python-3-tic-tac-toe-minimax-/assets/142397823/8f1c07e5-4607-4e0a-a9c3-ca59829ed105)
![47r71oxk](https://github.com/S-Immanuel01/python-3-tic-tac-toe-minimax-/assets/142397823/13914b6d-eca2-49b5-98af-9716314d5943)



