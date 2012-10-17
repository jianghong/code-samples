import tic_tac_toe
import game_tree
import time

INF = 1e300000

def test_ttt_winner():
    test_results = []
    # Test 1: Empty grid, no winners.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != False or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 1")
    # Test 2: First row p1 wins and p2 loses.
    r1 = ['p1', 'p1', 'p1']
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != True or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 2")
    # Test 3: Last row p2 wins and p1 loses.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = ['p2', 'p2', 'p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != False or ttt.winner('p2') != True:
        test_results.append("TTT Winner: \tFails Test 3")
    # Test 4: First column p1 wins and p2 loses.
    r1 = ['p1', None, None]
    r2 = ['p1', None, None]
    r3 = ['p1', None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != True or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 4")
    # Test 5: Last column p2 wins and p1 loses.
    r1 = [None, None, 'p2']
    r2 = [None, None, 'p2']
    r3 = [None, None, 'p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != False or ttt.winner('p2') != True:
        test_results.append("TTT Winner: \tFails Test 5")
    # Test 6: Diagonal 1, p1 wins and p2 loses.
    r1 = ['p1', None, None]
    r2 = [None, 'p1', None]
    r3 = [None, None, 'p1']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != True or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 6")
    # Test 7: Diagonal 2, p2 wins and p1 loses.
    r1 = [None, None, 'p2']
    r2 = [None, 'p2', None]
    r3 = ['p2', None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != False or ttt.winner('p2') != True:
        test_results.append("TTT Winner: \tFails Test 7")
    # Test 8: Messier gamestate where p1 wins and p2 loses.
    r1 = ['p2', 'p1', 'p1']
    r2 = [None, 'p1', 'p2']
    r3 = ['p1', 'p2', 'p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != True or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 8")
    # Test 9: Tie game, both players lose.
    r1 = ['p2', 'p1', 'p1']
    r2 = ['p1', 'p2', 'p2']
    r3 = ['p1', 'p2', 'p1']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.winner('p1') != False or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 9")
    # Test 10: Sanity check, also works on larger fields, both players lose.
    r1 = ['p1', 'p1', 'p1', None]
    r2 = ['p1', 'p1', 'p1', None]
    r3 = ['p1', 'p1', 'p1', None]
    r4 = [None, None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3, r4], 'p1'))
    if ttt.winner('p1') != False or ttt.winner('p2') != False:
        test_results.append("TTT Winner: \tFails Test 10")
    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append("TTT Winner: \tPasses All 10 Tests")
    return test_results

def test_ttt_string():
    test_results = []
    # Test 1: Empty 3x3, p1 is up.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.__str__() != "To play: p1\n---\n---\n---\n":
        test_results.append("TTT String: \tFails Test 1")
    # Test 2: Empty 3x3, p2 is up.
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    if ttt.__str__() != "To play: p2\n---\n---\n---\n":
        test_results.append("TTT String: \tFails Test 2")
    # Test 3: All p1, p1 is up.
    r1 = ['p1', 'p1', 'p1']
    r2 = ['p1', 'p1', 'p1']
    r3 = ['p1', 'p1', 'p1']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.__str__() != "To play: p1\nXXX\nXXX\nXXX\n":
        test_results.append("TTT String: \tFails Test 3")
    # Test 4: All p2. p2 is up.
    r1 = ['p2', 'p2', 'p2']
    r2 = ['p2', 'p2', 'p2']
    r3 = ['p2', 'p2', 'p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    if ttt.__str__() != "To play: p2\nOOO\nOOO\nOOO\n":
        test_results.append("TTT String: \tFails Test 4")
    # Test 5: Mixed, p2 is up.
    r1 = ['p2', 'p1', 'p1']
    r2 = [None, 'p2', 'p2']
    r3 = ['p1', 'p2', None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    if ttt.__str__() != "To play: p2\nOXX\n-OO\nXO-\n":
        test_results.append("TTT String: \tFails Test 5")
    # Test 6: Sanity check, also works on larger fields, p1 is up.
    r1 = ['p2', 'p1', 'p1', None]
    r2 = [None, 'p2', 'p2', None]
    r3 = ['p1', 'p2', None, None]
    r4 = [None, None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3, r4], 'p1'))
    if ttt.__str__() != "To play: p1\nOXX-\n-OO-\nXO--\n----\n":
        test_results.append("TTT String: \tFails Test 6")
    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append("TTT String: \tPasses All  6 Tests")
    return test_results

def test_ttt_nextmove():
    test_results = []
    # Test 1: Empty 3x3, all possible moves are legal moves.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    move_list = ttt.next_move()
    move_list.sort()
    if move_list != [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
        test_results.append("TTT Next Move: \tFails Test 1")
    # Test 2: Some positions are taken..
    r1 = ['p1', 'p2', None]
    r2 = [None, None, 'p1']
    r3 = ['p2', 'p2', None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    move_list = ttt.next_move()
    move_list.sort()
    if move_list != [(0,2),(1,0),(1,1),(2,2)]:
        test_results.append("TTT Next Move: \tFails Test 2")
    # Test 3: Tied game, all positions are taken, no legal moves left.
    r1 = ['p2', 'p1', 'p2']
    r2 = ['p1', 'p1', 'p2']
    r3 = ['p2', 'p2', 'p1']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    move_list = ttt.next_move()
    move_list.sort()
    if move_list != []:
        test_results.append("TTT Next Move: \tFails Test 3")
    # Test 4: Won game, all positions are taken, no legal moves left.
    r1 = ['p1', 'p1', 'p1']
    r2 = ['p1', 'p2', 'p2']
    r3 = ['p2', 'p2', 'p1']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    move_list = ttt.next_move()
    move_list.sort()
    if move_list != []:
        test_results.append("TTT Next Move: \tFails Test 4")
    # Test 5: Won game, some positions are open, no legal moves left.
    r1 = ['p1', 'p1', 'p1']
    r2 = [None, None, None]
    r3 = ['p2', 'p2', None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    move_list = ttt.next_move()
    move_list.sort()
    if move_list != []:
        test_results.append("TTT Next Move: \tFails Test 5")
    # Test 6: Sanity check, works on larger fields.
    r1 = ['p2', 'p1', 'p2', None]
    r2 = ['p1', 'p1', 'p2', None]
    r3 = ['p2', 'p2', 'p1', None]
    r4 = [None, None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3, r4], 'p1'))
    move_list = ttt.next_move()
    move_list.sort()
    if move_list != [(0,3),(1,3),(2,3),(3,0),(3,1),(3,2),(3,3)]:
        print move_list
        test_results.append("TTT Next Move: \tFails Test 6")
    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append("TTT Next Move: \tPasses All  6 Tests")
    return test_results

def test_ttt_makemove():
    test_results = []
    # Test 1: Try to make a move on an occupied space, p1 is up.
    r1 = ['p1', 'p2', None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    ttt = ttt.make_move((0,0))
    if ttt != None:
        test_results.append("TTT Make Move: \tFails Test 1")
    # Test 2: Try to make a move on an occupied space, p2 is up.
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    ttt = ttt.make_move((0,0))
    if ttt != None:
        test_results.append("TTT Make Move: \tFails Test 2")
    # Test 3: Try to make a valid move on an empty field.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    field = [r1, r2, r3]
    ttt = tic_tac_toe.TicTacToe((field, 'p1'))
    ttt2 = ttt.make_move((2,2))
    field[2][2] = 'p1'
    if ttt2._state[0] != field or ttt2._state[1] != 'p2':
        test_results.append("TTT Make Move: \tFails Test 3")
    # Test 4: ttt shouldn't have been altered in Test 3
    field[2][2] = None
    if ttt._state[0] != field or ttt._state[1] != 'p1':
        test_resultts.append("TTT Make Move: \tFails Test 4")
    # Test 5: Try to make a valid move on a nearly full field.
    r1 = ['p2', 'p1', 'p2']
    r2 = ['p1', None, 'p2']
    r3 = ['p2', 'p2', 'p1']
    field = [r1, r2, r3]
    ttt = tic_tac_toe.TicTacToe((field, 'p1'))
    ttt = ttt.make_move((1,1))
    field[1][1] = 'p1'
    if ttt._state[0] != field or ttt._state[1] != 'p2':
        test_results.append("TTT Make Move: \tFails Test 5")
    # Test 6: Try to make a move far outside of the field.
    #r1 = ['p2', 'p1', 'p2']
    #r2 = ['p1', None, 'p2']
    #r3 = ['p2', 'p2', 'p1']
    #field = [r1, r2, r3]
    #ttt = tic_tac_toe.TicTacToe((field, 'p1'))
    #ttt = ttt.make_move((10,10))
    #if ttt != None:
        #test_results.append("TTT Make Move: \tFails Test 6")
    # Test 7: Try to make a move far barely outside of the field.
    #ttt = tic_tac_toe.TicTacToe((field, 'p1'))
    #ttt = ttt.make_move((1,3))
    #if ttt != None:
        #test_results.append("TTT Make Move: \tFails Test 7")
    # Test 8: Sanity check, works on larger fields.
    r1 = ['p2', 'p1', 'p2', None]
    r2 = ['p1', None, 'p2', None]
    r3 = ['p2', 'p2', 'p1', None]
    r4 = [None, None, None, None]
    field = [r1, r2, r3, r4]
    ttt = tic_tac_toe.TicTacToe((field, 'p2'))
    ttt = ttt.make_move((1,3))
    field[1][3] = 'p2'
    if ttt._state[0] != field or ttt._state[1] != 'p1':
        print ttt._state[0], field
        test_results.append("TTT Make Move: \tFails Test 8")
    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append("TTT Make move: \tPasses All  8 Tests")
    return test_results

def test_ttt_heuristic():
    test_results = []
    # Test 1: All opportunities are left.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.heuristic_eval() != (8-8)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 1")
    # Test 2: Less opportunities for p1 than p2, p1 is up.
    r1 = [None, None, None]
    r2 = [None, 'p2', None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.heuristic_eval() != (4-8)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 2")
    # Test 3: Same scenario, p2 is up.
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    if ttt.heuristic_eval() != (8-4)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 3")
    # Test 4: Only 1 opportunity for p1, a row, p1 is up.
    r1 = ['p2','p2','p1']
    r2 = ['p1','p1',None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.heuristic_eval() != (1-0)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 4")
    # Test 5: Only 1 opportunity for p2, a diagonal, p2 is up.
    r1 = ['p2','p2','p1']
    r2 = ['p1',None,'p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    if ttt.heuristic_eval() != (1-0)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 5")
    # Test 6: Only 1 opportunity for p1, an antidiagonal, p2 is up.
    r1 = ['p2','p1','p1']
    r2 = ['p1',None,'p2']
    r3 = ['p1','p2','p1']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    if ttt.heuristic_eval() != (0-1)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 6")
    # Test 7: Only 1 opportunity for p2, a column, p1 is up.
    r1 = ['p1','p2','p2']
    r2 = ['p2',None,'p1']
    r3 = ['p1','p2','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.heuristic_eval() != (0-1)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 7")
    # Test 8: It's a tie, no opportunities left.
    r1 = ['p1','p2','p1']
    r2 = ['p2','p2','p1']
    r3 = ['p1','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    if ttt.heuristic_eval() != (0-0)/8.0:
        test_results.append("TTT Heuristic: \tFails Test 8")
    # Test 9: Sanity check, works on larger fields too.
    r1 = ['p2','p1','p1',None]
    r2 = ['p2','p2','p1',None]
    r3 = ['p2','p1','p2',None]
    r4 = [None,None,None,None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3, r4], 'p1'))
    if ttt.heuristic_eval() != (3-4)/10.0:
        test_results.append("TTT Heuristic: \tFails Test 9")
    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append("TTT Heuristic: \tPasses All  9 Tests")
    return test_results

def test_gt_leafcount():
    test_results = []
    # Test 1: No open squares.
    r1 = ['p1','p2','p1']
    r2 = ['p2','p1','p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.leaf_count(node) != 1:
        test_results.append("GT Leaf Count: \tFails Test 1")
    # Test 2: One open square.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,'p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.leaf_count(node) != 1:
        test_results.append("GT Leaf Count: \tFails Test 2")
    # Test 3: Two open squares, choosing either results in a tie.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.leaf_count(node) != 2:
        test_results.append("GT Leaf Count: \tFails Test 3")
    # Test 4: Three open squares, tie is unavoidable.
    r1 = ['p1','p2','p1']
    r2 = [None,None,None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.leaf_count(node) != 6:
        test_results.append("GT Leaf Count: \tFails Test 4")
    # Test 5: Three open squares, victory can be attained.
    r1 = ['p1','p1','p2']
    r2 = [None,None,None]
    r3 = ['p1','p2','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.leaf_count(node) != 5:
        test_results.append("GT Leaf Count: \tFails Test 5")
    if LENGTH == 'l':
        # Test 6: Total leafs possible in Tic Tac Toe. 
        r1 = [None,None,None]
        r2 = [None,None,None]
        r3 = [None,None,None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        node = game_tree.GameStateNode(ttt)
        node.grow()
        if game_tree.leaf_count(node) != 255168:
            test_results.append("GT Leaf Count: \tFails Test 6")
        passmsg = "GT Leaf Count: \tPasses All  6 Tests"
    else:
        passmsg = "GT Leaf Count: \tPasses All  5 Tests (1 omitted)"
    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append(passmsg)
    return test_results

def test_gt_nodecount():
    test_results = []
    # Test 1: No open squares.
    r1 = ['p1','p2','p1']
    r2 = ['p2','p1','p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.distinct_node_count(node) != 1:
        test_results.append("GT Node Count: \tFails Test 1")
    # Test 2: One open square.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,'p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.distinct_node_count(node) != 2:
        test_results.append("GT Node Count: \tFails Test 2")
    # Test 3: Two open squares, choosing either will result in a tie.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.distinct_node_count(node) != 5:
        test_results.append("GT Node Count: \tFails Test 3")
    # Test 4: Three open squares, tie is unavoidable.
    r1 = ['p1','p2','p1']
    r2 = [None,None,None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.distinct_node_count(node) != 13:
        test_results.append("GT Node Count: \tFails Test 4")
    # Test 5: Three possibilities, victory can be attained.
    r1 = ['p1','p1','p2']
    r2 = [None,None,None]
    r3 = ['p1','p2','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    node = game_tree.GameStateNode(ttt)
    node.grow()
    if game_tree.distinct_node_count(node) != 10:
        test_results.append("GT Node Count: \tFails Test 5")
    if LENGTH == 'l':
        # Test 6: Total distinct nodes possible in Tic Tac Toe. 
        r1 = [None,None,None]
        r2 = [None,None,None]
        r3 = [None,None,None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        node = game_tree.GameStateNode(ttt)
        node.grow()
        if game_tree.distinct_node_count(node) != 5478:
            test_results.append("GT Node Count: \tFails Test 6")
        passmsg = "GT Node Count: \tPasses All  6 Tests"
    else:
        passmsg = "GT Node Count: \tPasses All  5 Tests (1 omitted)"

    # Did all tests pass?
    if len(test_results) == 0:
        test_results.append(passmsg)
    return test_results

def test_minimax():
    test_results = []
    # Test 1: One move, p1 up, tie unavoidable.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,'p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(INF)
    if mm_result != ((1,1), 0):
        test_results.append("MM MiniMax: \tFails Test 1")
    # Test 2: One move, p2 up, victory unavoidable.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,'p2']
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
    mm_result = ttt.minimax(INF)
    if mm_result != ((1,1), 1):
        test_results.append("MM MiniMax: \tFails Test 2")
    # Test 3: Two open squares, choosing either results in a tie.
    r1 = ['p1','p2','p1']
    r2 = ['p2',None,None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(INF)
    if mm_result[1] != 0:
        test_results.append("MM MiniMax: \tFails Test 3")
    # Test 4: Three open squares, tie is unavoidable.
    r1 = ['p1','p2','p1']
    r2 = [None,None,None]
    r3 = ['p2','p1','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(INF)
    if mm_result[1] != 0:
        test_results.append("MM MiniMax: \tFails Test 4")
    # Test 5: Three open squares, victory can be attained.
    r1 = ['p1','p1','p2']
    r2 = [None,None,None]
    r3 = ['p1','p2','p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(INF)
    if mm_result != ((1,0), 1):
        test_results.append("MM MiniMax: \tFails Test 5")
    # Test 6: Two open squares, p1 is up, can draw or lose.
    r1 = ['p1','p2','p1']
    r2 = ['p1',None,'p2']
    r3 = ['p2',None,'p2']
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(INF)
    if mm_result != ((2,1), 0):
        test_results.append("MM MiniMax: \tFails Test 6")
    # Test 7: Empty board, foresight 1, p1 up, p1 should predict win.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(1)
    if mm_result != ((1,1), (8-4)/8.0):
        test_results.append("MM MiniMax: \tFails Test 7")
    # Test 8: Empty board, foresight 2, p1 up, p1 should predict win.
    r1 = [None, None, None]
    r2 = [None, None, None]
    r3 = [None, None, None]
    ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
    mm_result = ttt.minimax(2)
    if mm_result[1] != (5-4)/8.0:
        test_results.append("MM MiniMax: \tFails Test 8")
    if LENGTH == 'l' or LENGTH == 'm':
        # Test 9: Empty board, draw should be anticipated, p1 is up.
        r1 = [None, None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 0:
            test_results.append("MM MiniMax: \tFails Test 9")
        # Test 10: Empty board, draw should be anticipated, p2 is up.
        r1 = [None, None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 0:
            test_results.append("MM MiniMax: \tFails Test 10")
        # Test 11: Corner taken, p2 is up, should expect draw.
        r1 = ['p1', None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 0:
            test_results.append("MM MiniMax: \tFails Test 11")
        # Test 12: Side taken, p2 is up, should expect draw.
        r1 = [None, 'p1', None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 0:
            test_results.append("MM MiniMax: \tFails Test 12")
        # Test 13: Center taken, p1 is up, should expect draw.
        r1 = [None, None, None]
        r2 = [None, 'p2', None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 0:
            test_results.append("MM MiniMax: \tFails Test 13")
        # Test 14: After corner, p2 picks side, p1 shuold expect draw.
        r1 = ['p1', None, None]
        r2 = [None, 'p2', None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 0:
            test_results.append("MM MiniMax: \tFails Test 14")
        # Test 15: After corner, p1 picks side, p2 should expect win.
        r1 = ['p2', 'p1', None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 1:
            test_results.append("MM MiniMax: \tFails Test 15")
        # Test 16: After corner, p2 picks corner, p1 should expect win.
        r1 = ['p1', None, 'p2']
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        mm_result = ttt.minimax(INF)
        if mm_result[1] != 1:
            test_results.append("MM MiniMax: \tFails Test 16")
        passmsg = "MM MiniMax: \tPasses All 16 Tests"
        
    else:
        passmsg = "MM MiniMax: \tPasses All  8 Tests (8 omitted)"
    # Did all tests pass?        
    if len(test_results) == 0:
        test_results.append(passmsg)
    return test_results

if __name__ == '__main__':
    print "\nNote: If you have not completed all the functions and methods" + \
          "\nyet, comment out the appropriate lines in the 'if __name__ ==\n" + \
          "'__main__':' part of this file."
    print "\nPerform a short, medium, or long test? Short will omit any\n" + \
          "tests that might take a long time to run, medium will also\n" + \
          "run tests that won't take long to run after coding the\n" + \
          "enhancements, and long will run all the tests."
    correct = False
    while not correct:
        inp = raw_input("?: ")
        if inp.lower() == 'short':
            LENGTH = 's'
            correct = True
        elif inp.lower() == 'medium':
            LENGTH = 'm'
            correct = True
        elif inp.lower() == 'long':
            LENGTH = 'l'
            correct = True
    results = []
    start = time.time()
    # ----------------------------------------------------------------------#
    # Comment out some of the following lines if you have not completed     #
    # the method or function that that suite is testing                     #
    # ----------------------------------------------------------------------#
    results.extend(test_ttt_winner())
    results.extend(test_ttt_string())
    results.extend(test_ttt_nextmove())
    results.extend(test_ttt_makemove())
    results.extend(test_ttt_heuristic())
    results.extend(test_gt_leafcount())
    results.extend(test_gt_nodecount())
    results.extend(test_minimax())
    # ----------------------------------------------------------------------#
    run_time = str(round(time.time() - start, 3))
    print "\n\n\n                Timo Test v2.0\n" + \
          "          Pissing you off since 2010!"
    print "\n             *** Test Results ***\n"
    for item in results:
        print "     " + item
    print "\n\t\t\tTime Taken: " + run_time + " seconds"
    print 