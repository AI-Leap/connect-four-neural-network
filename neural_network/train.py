import os
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from keras.utils.np_utils import to_categorical
import generate_data
import model

def gamesToWinLossData(games):
    X = []
    y = []
    for (history, game) in games:
        winner = game.getWinner()
        r = 0
        if winner == 'X':
          r = 1
        if winner == 'O':
          r = 2

        for move in range(len(history)):
            X.append(generate_data.generateTrainingBoard(history[:(move + 1)]))
            y.append(r)

    X = np.array(X).reshape((-1, 48))
    y = to_categorical(y)
    
    # Return an appropriate train/test split
    trainNum = int(len(X) * 0.8)
    return (X[:trainNum], X[trainNum:], y[:trainNum], y[trainNum:])


games = generate_data.getTrainingGames(3)
# for (history, game) in games:
#   game.displayBoard()
#   print(generate_data.generateTrainingBoard(history))

X_train, X_test, y_train, y_test = gamesToWinLossData(games)

model = model.getModel()
nEpochs = 100
batchSize = 100
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=nEpochs, batch_size=batchSize)