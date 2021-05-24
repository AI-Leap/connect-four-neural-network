import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout, Conv2D, MaxPool2D
from keras.backend import reshape
from keras.utils.np_utils import to_categorical
from tensorflow.python.keras.layers.pooling import MaxPool2D
optimizer = keras.optimizers.Adam(lr=0.001)

def getModel():
    numCells = 48
    outcomes = 3
    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(48, )))
    # model.add(MaxPool2D(pool_size=(2, 2)))
    # model.add(Dense(500, activation='relu'))
    # model.add(Dropout(0.3))
    model.add(Dense(256, activation='relu'))
    # model.add(Conv2D(125, kernel_size=5, activation='relu'))
    # model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(25, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(outcomes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['acc'])
    return model

# model = getModel()
# print(model.summary())
