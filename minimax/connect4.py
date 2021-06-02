import numpy as np
import os
import sys
import math
import random
import time
from board import Board

game_over = False
turn = random.randint(Board.PLAYER1_PIECE, Board.PLAYER2_PIECE)

def next_turn():
	global turn
	print("\nPlayer " + str(turn) + "'s Turn\n")
	board.print_board()
	if turn == board.PLAYER1_PIECE:
		turn = board.PLAYER2_PIECE
	else:
		turn = board.PLAYER1_PIECE

def check_win(piece):
	if board.winning_move(piece):
		print("\nPLAYER " + str(piece) + " WINS!")
		return True
	
	if board.check_draw():
		print("\n IT'S A TIE!")
		return True
	return False

def connect4(p1, p2):
	global game_over, board


	board = Board(turn)
	board.print_board()

	time_p1 = time_p2 = 0
	moves_count_p1 = moves_count_p2 = 0

	while not game_over:
		# Player1's Input
		start = time.perf_counter()
		if turn == board.PLAYER1_PIECE and not game_over:
			col = p1.get_move(board)

			if board.is_valid_location(col):
				board.drop_piece(col, board.PLAYER1_PIECE)
				moves_count_p1 += 1
				next_turn()
				game_over = check_win(board.PLAYER1_PIECE)
		end = time.perf_counter()

		time_p1 += (end - start)

		# Player2's Input
		start = time.perf_counter()
		if turn == board.PLAYER2_PIECE and not game_over:
			col = p2.get_move(board)

			if board.is_valid_location(col):
				board.drop_piece(col, board.PLAYER2_PIECE)
				moves_count_p2 += 1
				next_turn()
				game_over = check_win(board.PLAYER2_PIECE)
		end = time.perf_counter()

		time_p2 += (end - start)

		if game_over:

			print("\nPlayer 1")
			print("TIME: " + "{:.2f}".format(round(time_p1, 2)) + " seconds")
			print("MOVES: "+ str(moves_count_p1))
			print("\nPlayer 2")
			print("TIME: " + "{:.2f}".format(round(time_p2, 2)) + " seconds")
			print("MOVES: "+ str(moves_count_p2))
