import keras
import numpy as np
import copy
import operator
from collections import Counter
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

from keras import models

model = keras.models.load_model('./ai-model')

def getMoves(board):
    moves = []
    for i in range(7):
        if board[i] == 0:
            moves.append(i)
    return moves

def playMove(board, move, player):
    boardCopy = copy.deepcopy(board)

    for i in range(35 + move, 0, -7):
        if board[i] == 0:
            boardCopy[i] = player
            return boardCopy
    return -1

def getPrediction(board):
    try:
        prediction = model.predict(np.array(board).reshape(-1, 42))[0]
        return prediction
    except ValueError:
        print('getPrediction Error', board)


def getOpponentNextMove(board, player):
    moves = getMoves(board)
    scores = []

    for move in moves:
        newBoard = playMove(board, move, player)
        prediction = getPrediction(newBoard)

        if player == -1:
            winPrediction = prediction[2]
            lossPrediction = prediction[1]
        else:
            winPrediction = prediction[1]
            lossPrediction = prediction[2]
        drawPrediction = prediction[0]
        if winPrediction - lossPrediction > 0:
            scores.append(winPrediction - lossPrediction)
        else:
            scores.append(drawPrediction - lossPrediction)
            
    (a, b) = max(enumerate(scores), key=operator.itemgetter(1))
    return (a, b)

def calculateFrequencyConfidence(nextMoves):
    moves = []
    for [move, confidence] in nextMoves:
        moves.append(move)

    confidenceDict = {}
    moveDict = Counter(moves)
    for key in moveDict:
        if moveDict[key] >= 3:
            totalConfidence = 0
            for [move, confidence] in nextMoves:
                if move == key:
                  totalConfidence += confidence
            averageConfidence = totalConfidence / moveDict[key]
            confidenceDict[key] = averageConfidence

    # print('moveDict', moveDict, 'confDict', confidenceDict)
    # mostF = max(confidenceDict.iteritems(), key=operator.itemgetter(1))[0]
    if bool(confidenceDict):
        mostF = max(confidenceDict, key=confidenceDict.get)
        # print('mostF', mostF, confidenceDict[mostF])
        if mostF == 0: return -1, -1 # dirty but works
        return mostF, confidenceDict[mostF]
    return -1, -1

def getMove(board, player):
    moves = getMoves(board)
    opponentNextMoves = []
    scores = []

    for move in moves:
        newBoard = playMove(board, move, player)
        prediction = getPrediction(newBoard)

        (opponentMove, opponentConfidence) = getOpponentNextMove(newBoard, 1 if player == -1 else -1)
        opponentNextMoves.append([opponentMove, opponentConfidence])

        if player == -1:
            winPrediction = prediction[2]
            lossPrediction = prediction[1]
        else:
            winPrediction = prediction[1]
            lossPrediction = prediction[2]
        drawPrediction = prediction[0]

        if winPrediction - lossPrediction > 0:
            scores.append(winPrediction - lossPrediction)
        else:
            scores.append(drawPrediction - lossPrediction)

    bestMoves = np.flip(np.argsort(scores))
    print('bestMoves', bestMoves)

    opponentBestMove, opponentBestConfidence = calculateFrequencyConfidence(opponentNextMoves)
    print('opponentBestMove', opponentBestMove)

    if opponentBestConfidence > scores[bestMoves[0]] or opponentBestConfidence > 0.95:
        return opponentBestMove

    for move in bestMoves:
        if move in moves:
            return move

def getBestMove(board, player):
    move = getMove(board, int(player))
    return move