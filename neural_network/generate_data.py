from connect4 import Connect4
import random

def bestMove(game, model, player, rnd=0):
    scores = []
    moves = game.getMoves(board)
    
    # Make predictions for each possible move

    # Choose a move completely at random
    return moves[random.randint(0, len(moves) - 1)]

def simulateGame(p1=None, p2=None, rnd=0):
    history = []
    game = Connect4()
    game.displayBoard()
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
        
        game.displayBoard()
        # Add the move to the history
        history.append((playerToMove, move))
        
        # Switch the active player
        playerToMove = 'X' if playerToMove == 'O' else 'O' 
    
    print('The Winner is ', game.getWinner())
        
    return history

simulateGame()
