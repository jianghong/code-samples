# tic-tac-toe game
import minimax as mm
import copy

def _column_common_value(l, value, i):
    '''Return True if the lists inside l all have value at a valid
    index i.'''
    
    for lists in l:
        if lists[i] != value:
            return False
    return True

def _diagonal_common_value(l, value, i):
    '''Return True if lists inside l all have value at index i of first list, 
    i+1(i-1 if i starts at -1) of second list,..., i+(n-1) of nth list. Valid
    inputs for i are 0 or -1.'''
    
    for lists in l:
        if lists[i] != value:
            return False
        if i >= 0:  # for diagonal
            i += 1
        else:
            i -= 1 # for anti-diagonal
    return True
            
class TicTacToe(mm.GameState):

    """Tic-tac-toe GameState.
    """

    def __init__(self, start_state): 
        """Create a tic-tac-toe game in start_state.

           Arguments:
           start_state: A tuple consisting of two elements:
                          --a list of k lists, where each list has k entries,
                            consisting of either None (empty), 'p1' (occupied
                            by player 1), or 'p2' (occupied by player 2), where
                            k is, implicitly, the size of the list
                          --current (to play) player, 'p1' or 'p2'.

            Assumption:
            start_state represents a valid tic-tac-toe game.

           Returns:
           A tic-tac-toe game in start_state.
        """
        
        mm.GameState.__init__(self, start_state)
        self._size = len(self._state[0])

    def _check_open_column(self, player, i):
        '''Return True if opponent of player does not have a square 
        occupied in column i.'''
        
        for row in self._state[0]:
            if player == self.player():
                if row[i] == self.opponent():
                    return False
            elif player == self.opponent():
                if row[i] == self.player():
                    return False
        return True
    
    def winner(self, player):
        """Return whether player has won.

           Arguments:
           Player may be either the current player or the opponent.

           Assumptions:
           Only one of p1 or p2 may be the winner.

           Returns
           Exactly one of True or False
        """
        
        # Check if player won by rows
        if [player] * self._size in self._state[0]:
            return True
        elif player in self._state[0][0]:
            i = self._state[0][0].index(player)
            for j in range(self._size - i):
                # Check columns
                if _column_common_value(self._state[0], player, i):
                    return True
                i += 1  
            # Check diagonals
            status = _diagonal_common_value(self._state[0], player, 0)
            if not status:
                return _diagonal_common_value(self._state[0], player, -1)
            return True
        return False
    
    def __str__(self):
        '''String representation of board.
           
           Returns
           A string where the first line reads 'To play: p?\n'
           where p? is the current player,
           followed by a \n-terminated line for each row, where each
           instance of p1 is replaced by X, each p2 is replaced by O,
           and each None is replaced by -
        '''
        
        s = 'To play: ' + self._state[1] + '\n'
        for row in self._state[0]:
            for p in row:
                if p == 'p1':
                    s += 'X'
                elif p == 'p2':
                    s += 'O'
                else:
                    s += '-'
            s += '\n'
        return s
    
    def next_move(self):
        """Return a (possibly empty) list of legal moves for current player.

            Assumptions:
            The list will be empty if either player has already won, and
            the order of moves in the list is not significant

            Returns:
            A list of pairs of legal moves of the form (r, c) such that
            self._state[0][r][c] is currently unoccupied and the current player
            may move by occupying it.
        """
        
        move_list = []
        if self.winner(self.opponent()):
            return move_list
        for r in range(self._size):
            for c in range(self._size):
                if self._state[0][r][c] == None:
                    move_list.append((r, c))
        return move_list

    def make_move(self, move):
        """Apply move to current game.

           Arguments:
           move:  A pair (r, c) representing square self._state[0][r][c]

           Assumptions:
           (r, c) are valid coordinates for self._state[0].  If they represent
           a valid move for current player, then the current player occupies
           that position and the opponent becomes the current player.
           Otherwise self._state is left unchanged.

           Returns:
           New TicTacToe gamestate with move recorded on
           self._state[0] and current player replaced by opponent, if
           this is legal.  Otherwise return None.
        """
        
        state = list(copy.deepcopy(self._state[0]))
        r = move[0]
        c = move[1]
        if state[r][c] == None:
            state[r][c] = self._state[1]
            return TicTacToe((state, self.opponent()))
        return None

    def heuristic_eval(self):
        """Return number of opportunities open to this player, minus those
           open to opponent.  A row, column, or diagonal is an open
           opportunity if it has no squares occupied by this player's
           opponent.

           Assumptions:
           The evaluation is not exact, and is, in general, inferior to an
           exact evaluation.

           Returns:
           Number of rows, columns, diagonals open to this player, minus
           those open to opponent, divided by total possible winning lines.
        """

        # Initialize needed variables
        p1 = 0
        p2 = 0
        total = 2 * (self._size + 1)
        diag_list = []
        anti_diag_list = []
        k = -1
        for row in self._state[0]:  # Check rows
            if self.opponent() not in row:
                p1 += 1
            if self._state[1] not in row:
                p2 += 1
        for i in range(self._size):  # Check columns while adding to diag_list
            diag_list.append(self._state[0][i][i])
            if self._check_open_column(self._state[1], i):
                p1 += 1
            if self._check_open_column(self.opponent(), i):
                p2 += 1
        for j in range(self._size): # Add anti diagonals
            anti_diag_list.append(self._state[0][j][k])
            k -= 1
        # Check both diagonals for open opportunities
        if self.opponent() not in diag_list:
            p1 += 1
        if self._state[1] not in diag_list:
            p2 += 1
        if self.opponent() not in anti_diag_list:
            p1 += 1
        if self._state[1] not in anti_diag_list:
            p2 += 1
        return (p1 - p2) / float(total)
