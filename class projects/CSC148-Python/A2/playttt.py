from tic_tac_toe import *

try:
    INF = float('inf')
except ValueError:
    INF = 1e300000

def _int_input(Message):
    out = False
    while not (out and out.isdigit()):
        out = raw_input(Message)
    return int(out)

board_size = _int_input("Size of board (int): ")
starting_ply = ""
while starting_ply not in ("p1", "p2"):
    starting_ply = raw_input("Who starts, p1 or p2: ")
computer_foresight = _int_input("Computer foresight (0 for infinity): ")
if computer_foresight == 0:
    computer_foresight = INF

# Generate board
board = []
for r in xrange(board_size):
    board.append([])
    for c in xrange(board_size):
        board[-1].append(None)

g = None

print "Each row and column are 0 based, so enter the row/column you wish to play in minus 1"
while (not g or (raw_input("Play again (y/n)? ") == "y")):
    g = TicTacToe((board, starting_ply))
    print g
    while not (g.winner('p1') or g.winner('p2')) and g.next_move():
        if g.player() == 'p1':
            legal_moves = g.next_move()
            row = -1
            column = -1
            while (row, column) not in legal_moves:
                row = _int_input("Row to move in: ")
                column = _int_input("Column to move in: ")
            g = g.make_move((row, column))
            print g
        else:
            m = g.minimax(computer_foresight)[0] # best move
            print "Computer's Move: ", m
            g = g.make_move(m)
            print g
    
    if g.winner('p1'):
        print "Congratulations, you won!"
    elif g.winner('p2'):
        print "You lose!"
    else:
        print "Cats game!"

print "Goodbye!"