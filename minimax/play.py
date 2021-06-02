from minimax import MiniMaxBot
from neuralbot import NeuralBot
from board import Board
from connect4 import connect4

# bot = MiniMaxBot(1)
# bot2 = NeuralBot(2)

bot = NeuralBot(1)
bot2 = MiniMaxBot(2)

connect4(bot, bot2)
