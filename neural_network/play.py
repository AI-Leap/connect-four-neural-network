import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
import copy
import random
from tensorflow import keras
from tensorflow.python.framework.tensor_util import GetNumpyAppendFn
model = keras.models.load_model('./checkpoints')
from connect4 import Connect4

def generateTrainingBoard(playboard):
    board = [ [0.0]* 7 for i in range(6)]
    for i in range(6):
        for j in range(7):
            if playboard[i][j] == ' X':
                board[i][j] = 1.0
            if playboard[i][j] == ' O':
                board[i][j] = -1.0 
    return board

def bestMove(game, model, player, rnd=0):
    scores = []
    moves = game.getMoves()
    
    # Make predictions for each possible move
    for i in range(len(moves)):
        gameCopy = copy.deepcopy(game)
        gameCopy.play(i, player)
        board = np.array(generateTrainingBoard(gameCopy.board)).reshape(-1, 42)
        prediction = model.predict(board)[0]
        # gameCopy.displayBoard()
        print('prediction', prediction)
        if player == ' O':
            winPrediction = prediction[1]
            lossPrediction = prediction[2]
            scores.append(winPrediction)
        else:
            winPrediction = prediction[2]
            lossPrediction = prediction[1]
        drawPrediction = prediction[0]
        # if winPrediction - lossPrediction > 0:
        #     scores.append(winPrediction - lossPrediction)
        # else:
        #     scores.append(drawPrediction - lossPrediction)

    # Choose the best move with a random factor
    bestMoves = np.flip(np.argsort(scores))
    print(bestMoves)
    for i in range(len(bestMoves)):
        if random.random() * rnd < 0.5:
            return moves[bestMoves[i]]

    # Choose a move completely at random
    return moves[random.randint(0, len(moves) - 1)]

def manualPlay():
  c = Connect4()

  # First while lopp init
  game = True
  while game:
      # Choose your marker
      # Display the board
      c.displayBoard()
      # Second while loop init
      win = False
      i = 0
      while not win:
          # Start Playing
          print('move...')
          if i % 2 == 0:
              currentPlayer = "Player1"
              marker = 'X'
          else:
              currentPlayer = "Player2"
              marker = 'O'
          # Player to choose where to put the mark
          # if currentPlayer == 'Player2':
          #     position = bestMove(c, model, 'O', 0)
          #     print('best move', position)
          # else:
          position = c.player_choice()

          # board = np.array(generateTrainingBoard(c.board)).reshape(-1, 42)
          # print(board)
          # prediction = model.predict(board)[0]
          # print('prediction', prediction)
          # gameCopy.displayBoard()

          if not c.play(position, marker):
              print(f"Column {position} full")
          board = np.array(generateTrainingBoard(c.board)).reshape(-1, 42)
          print(board)
          prediction = model.predict(board)[0]
          print('prediction', prediction)

          # Generate the reversed board
          reversedBoard = c.generateReversedBoard()
          # Check if won
          # if c.checkLines(marker) or c.checkLines(marker, reversedBoard) or c.checkDiags(marker):
          if c.getWinner():
              # update the win to exit the second while loop
              win = True
              c.displayBoard()
              print(f"Game won by {currentPlayer}", c.getWinner())
              # Ask for replay.
              # If no, change the first loop game = True to False
              # If yes, reset our class with fresh new datas
              replay = input("Do you want to play again (Y/N) ? ")
              if replay.lower() == 'n':
                  game = False
                  print("Game ended !")
              else:
                  c = Connect4()
              break
          c.displayBoard()
          i += 1

manualPlay()
