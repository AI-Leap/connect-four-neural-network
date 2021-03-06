import numpy as np
from tensorflow import keras
model = keras.models.load_model('./checkpoints')

counter = 0

class Evaluation:
	def __init__(self, piece):
		self.bot_piece = piece
		if self.bot_piece == 1:
			self.opp_piece = 2
		else:
			self.opp_piece = 1

	def evaluate_window(self, board):
		# print('eval', board)
		global counter
		board = np.array(board).reshape(-1, 42)
		prediction = model.predict(board)[0]
		# print('prediction', prediction)
		counter += 1
		if counter % 1000 == 0: print('prediction', prediction, counter)
		return prediction[self.bot_piece]

	def score_position(self, board):
		score = 0
		score += self.evaluate_window(board.get_board())
		return score

	def is_terminal_node(self, board):
		return board.winning_move(self.bot_piece) or board.winning_move(self.opp_piece) or len(board.get_valid_locations()) == 0
