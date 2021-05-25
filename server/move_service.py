from tensorflow import keras
import numpy as np
import copy

model = keras.models.load_model('./ai-model')

def getPrediction(board):
    prediction = model.predict(np.array(board).reshape(-1, 42))[0]
    print(prediction)

    return 4