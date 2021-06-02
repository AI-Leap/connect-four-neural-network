from minimax import MiniMaxBot
from board import Board

bot = MiniMaxBot(1)

numberOfColumns = 7
numberOfLines = 6
board = Board(1)

a = bot.get_move(board)
print(a)
board.print_board()
board.drop_piece(a, 1)
board.print_board()
print(bot)
