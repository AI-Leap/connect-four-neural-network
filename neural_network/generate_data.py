from connect4 import Connect4
import random

def bestMove(game, model, player, rnd=0):
    scores = []
    moves = game.getMoves(board)
    
    # Make predictions for each possible move

    # Choose a move completely at random
    return moves[random.randint(0, len(moves) - 1)]

def movesToBoard(history):
    game = Connect4()
    for (move, playerToMove) in history:
        game.play(move, playerToMove)
    return game

def generateTrainingBoard(history):
    game = movesToBoard(history)
    board = [ [0]* game.numberOfColumns for i in range(game.numberOfLines)]
    for i in range(game.numberOfLines):
        for j in range(game.numberOfColumns):
            if game.board[i][j] == ' X':
                board[i][j] = 1
            if game.board[i][j] == ' O':
                board[i][j] = 2
    return board

def simulateGame(p1=None, p2=None, rnd=0):
    history = []
    game = Connect4()
    playerToMove = 'X'

    while not game.getWinner():
        # Chose a move (random or use a player model if provided)
        move = None
        if playerToMove == 'X' and p1 != None:
            move = bestMove(game, p1, playerToMove, rnd)
        elif playerToMove == 'O' and p2 != None:
            move = bestMove(game, p2, playerToMove, rnd)
        else:
            moves = game.getMoves()
            move = moves[random.randint(0, len(moves) - 1)]
        
        # Make the move
        game.play(move, playerToMove)
        
        # game.displayBoard()
        # Add the move to the history
        history.append((move, playerToMove))
        
        # Switch the active player
        playerToMove = 'X' if playerToMove == 'O' else 'O' 
    
    return (history, game)

def getTrainingGames(n):
  return [simulateGame() for _ in range(n)]
