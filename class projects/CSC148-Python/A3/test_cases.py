# -------------------- #
#        About         #
# -------------------- #

'''
Version:       2.0
Author:        Timo Vink
Contributions: c0dialke (GameTrie Test Case 5)
               Xiangxin Jing (GameTrie Test Case 6)
               Jiaming Cao (Found Typo)
'''

# -------------------- #
#       Settings       #
# -------------------- #

# Change to True/False to run/don't run certain test suites. If you fail tests
# in suites other than GameTrie, I suggest leaving the GameTrie tests disabled
# until you pass them since it will increase the running time of the remaining
# tests by several seconds.
trie_insert_completed = True
trie_find_node_completed = True
lextrie_find_all_completed = True
gametrie_completed = True

# Displays or hides the time it took to run the tests.
show_running_time = True

# Show more detailed error messages.
show_detailed_errors = True

# -------------------- #
#      Test Stuff      #
# -------------------- #

import trie
import trienode
import lextrie
import gametrie
import time

RESULTS = ([],[])
S_TEST_RES = None
L_TEST_RES = None
TEST_PASSED = None

def test_trie_insert():
    global S_TEST_RES
    global L_TEST_RES
    global TEST_PASSED
    S_TEST_RES, L_TEST_RES = [], []
    
    # Test 1: Insert 1 node (the 'word' "a").
    TEST_PASSED = True
    t = trie.Trie()
    try:
        t.insert('a', 'The letter A')
        user = t._root.children().keys()
        expected = ['a']
        if user != expected:
            add_fail('Trie Insert', 1.1, "ERROR: expected _root.children().keys() to be '" + str(expected) + "', but got '" + str(user) + "'")            
        else:
            user = t._root.children()['a'].children()
            expected = {}
            if user != expected:
                add_fail('Trie Insert', 1.2, "ERROR: expected _root.children()['a'].children() to be '" + str(expected) + "', but got '" + str(user) + "'")
            user = t._root.children()['a'].data()
            expected = 'The letter A'
            if user != expected:
                add_fail('Trie Insert', 1.3, "ERROR: expected _root.children()['a'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
    except Exception, e:
        add_fail('Trie Insert', 1, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Insert', 1)
        
    # Test 2: Insert 2 nodes (the 'word' "fg").
    TEST_PASSED = True
    t = trie.Trie()
    try:
        t.insert('fg', 'The word FG')
        user = t._root.children().keys()
        expected = ['f']
        if user != expected:
            add_fail('Trie Insert', 2.1, "ERROR: expected _root.children().keys() to be '" + str(expected) + "', but got '" + str(user) + "'")
        else:
            user = t._root.children()['f'].data()
            expected = None
            if user != expected:
                add_fail('Trie Insert', 2.2, "ERROR: expected _root.children()['f'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
            user = t._root.children()['f'].children().keys()
            expected = ['g']
            if user != expected:
                add_fail('Trie Insert', 2.3, "ERROR: expected _root.children()['f'].children().keys() to be '" + str(expected) + "', but got '" + str(user) + "'")                                
            else:
                user = t._root.children()['f'].children()['g'].data()
                expected = 'The word FG'
                if user != expected:
                    add_fail('Trie Insert', 2.4, "ERROR: expected _root.children()['f'].children()['g'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
    except Exception, e:
        add_fail('Trie Insert', 2, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Insert', 2)
        
    # Test 3: Empty trie, insert 2 nodes (the 'word' "xy") then update it's data.
    TEST_PASSED = True
    t = trie.Trie()
    try:
        t.insert('xy', 'Dummy Data')
        t.insert('xy', 'Actual Data')
        user = t._root.children().keys()
        expected = ['x']
        if user != expected:
            add_fail('Trie Insert', 3.1, "ERROR: expected _root.children().keys() to be '" + str(expected) + "', but got '" + str(user) + "'")            
        else:
            user = t._root.children()['x'].data()
            expected = None
            if user != expected:
                add_fail('Trie Insert', 3.2, "ERROR: expected t._root.children()['x'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
            user = t._root.children()['x'].children().keys()
            expected = ['y']
            if user != expected:
                add_fail('Trie Insert', 3.3, "ERROR: expected _root.children()['x'].children().keys() to be '" + str(expected) + "', but got '" + str(user) + "'")
            else:
                user = t._root.children()['x'].children()['y'].data()
                expected = 'Actual Data'
                if user != expected:
                    add_fail('Trie Insert', 3.4, "ERROR: expected t._root.children()['x'].children()['y'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
    except Exception, e:
        add_fail('Trie Insert', 3, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Insert', 3)

    # Test 4: Empty trie, insert 2 words, which overlap.
    TEST_PASSED = True
    t = trie.Trie()
    try:
        t.insert('test', 'The word TEST')
        t.insert('tent', 'The word TENT')
        user = [t._root.children().keys(),t._root.children()['t'].children().keys(),t._root.children()['t'].children()['e'].children().keys()]
        user[2].sort()
        expected = [['t'],['e'],['n','s']]
        if user != expected:
            add_fail('Trie Insert', 4.1, "ERROR: expected the first 3 layers of children to be '" + str(expected) + "', but got '" + str(user) + "'")
        else:
            user = t._root.children()['t'].children()['e'].children()['s'].children()['t'].data()
            expected = 'The word TEST'
            if user != expected:
                add_fail('Trie Insert', 4.2, "ERROR: expected _root.children()['t'].children()['e'].children()['s'].children()['t'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
            user = t._root.children()['t'].children()['e'].children()['n'].children()['t'].data()
            expected = 'The word TENT'
            if user != expected:
                add_fail('Trie Insert', 4.3, "ERROR: expected t._root.children()['t'].children()['e'].children()['n'].children()['t'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
    except Exception, e:
        add_fail('Trie Insert', 4, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Insert', 4)
        
    # Test 5: Insert a word and an overlapping longer word.
    TEST_PASSED = True
    t = trie.Trie()
    try:
        t.insert('cook','The word COOK')
        t.insert('cookie','COOKIES!! :)')
        user = t._root.children()['c'].children()['o'].children()['o'].children()['k'].data()
        expected = 'The word COOK'
        if user != expected:
            add_fail('Trie Insert', 5.1, "ERROR: expected _root.children()['c'].children()['o'].children()['o'].children()['k'].data() to be '" + str(expected) + "', but got '" + str(user) + "'")
        user = t._root.children()['c'].children()['o'].children()['o'].children()['k'].children().keys()
        expected = ['i']
        if user != expected:
            add_fail('Trie Insert', 5.2, "ERROR: expected _root.children()['c'].children()['o'].children()['o'].children()['k'].children().keys() to be '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('Trie Insert', 5, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Insert', 5)
    
    # Test 6: Insert all the words from "short.txt".
    TEST_PASSED = True
    t = trie.Trie()
    try:
        word_file = open("short.txt")
        for line in word_file.readlines():
            pair = line.split('::')
            t.insert(pair[0], pair[1].rstrip())
        word_file.close()
        user = str(t)
        expected = "None {c: None {o: None {o: COO Coo {k: COOK Cook {}, l: COOL Cool {e: None {r: COOLER Cooler {}}}}}}, b: None {a: None {r: BAR Bar {i: None {s: None {t: None {a: None {s: BARISTAS Baristas {}}}}}}, g: BAG Bag {}, n: None {k: BANK Bank {}, n: None {e: None {r: BANNER Banner {}}}}}}}"
        if user != expected:
            add_fail('Trie Insert', 6.1, "ERROR: expected the string representation of the tree to be '" + str(expected) + "', but got '" + str(user) + "'")            
    except IOError, e:
        add_fail('Trie Insert', 6, get_exception(e) + ": You should put 'short.txt' in the same folder as this file.")
    except Exception, e:
        add_fail('Trie Insert', 6, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Insert', 6)
        
    # Append the results
    if L_TEST_RES:
        RESULTS[0].extend(S_TEST_RES)
        RESULTS[1].extend(L_TEST_RES)
    else:
        RESULTS[0].append("Trie Insert: \t   Passes All 6 Tests")

def test_trie_find_node():
    global S_TEST_RES
    global L_TEST_RES
    global TEST_PASSED
    S_TEST_RES, L_TEST_RES = [], []
    
    # Test 1: Empty trie, try finding the empty string.
    TEST_PASSED = True
    t = trie.Trie()
    try:
        user = t.find_node('')
        expected = t._root
        if user != expected:
            add_fail('Trie Find Node', 1.1, "ERROR: expected find('') to return the root node, but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('Trie Find Node', 1, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Find Node', 1)    
    
    # Test 2: Empty trie, try finding a random word.
    TEST_PASSED = True
    t = trie.Trie()
    try:
        user = t.find_node('blah')
        expected = None
        if user != expected:
            add_fail('Trie Find Node', 2.1, "ERROR: expected find('blah') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('Trie Find Node', 2, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Find Node', 2)
        
    # Test 3: One word trie, try finding that word.
    TEST_PASSED = True
    t = trie.Trie()
    t._root.children()['o'] = trienode.TrieNode()
    t._root.children()['o'].children()['p'] = trienode.TrieNode()
    t._root.children()['o'].children()['p'].children()['q'] = trienode.TrieNode('abcdef')
    try:
        node = t.find_node('opq')
        user = node
        expected = t._root.children()['o'].children()['p'].children()['q']
        if user != expected:
            add_fail('Trie Find Node', 3.1, "ERROR: expected find_node('opq') to return node 'opq', but got node '" + str(user) + "'")            
        else:
            user = node.children()
            expected = {}
            if user != expected:
                add_fail('Trie Find Node', 3.2, "ERROR: expected t.find('opq').children() to return '" + str(expected) + "', but got '" + str(user) + "'")            
            user = node.data()
            expected = 'abcdef'
            if user != expected:
                add_fail('Trie Find Node', 3.3, "ERROR: expected t.find('opq').data() to return '" + str(expected) + "', but got '" + str(user) + "'")                            
    except Exception, e:
        add_fail('Trie Find Node', 3, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Find Node', 3)
    
    # Test 4: One word trie, try finding a longer word that uses that prefix.
    TEST_PASSED = True
    t = trie.Trie()
    t._root.children()['s'] = trienode.TrieNode()
    t._root.children()['s'].children()['t'] = trienode.TrieNode()
    t._root.children()['s'].children()['t'].children()['u'] = trienode.TrieNode('ghijkl')
    try:
        user = t.find_node('stuvwx')
        expected = None
        if user != expected:
            add_fail('Trie Find Node', 4.1, "ERROR: expected find_node('opq') to return '" + str(expected) + "', but got '" + str(type(user)) + "'")            
    except Exception, e:
        add_fail('Trie Find Node', 4, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Find Node', 4)
        
    # Test 5: One word trie, try finding a shorter word.
    TEST_PASSED = True
    t = trie.Trie()
    t._root.children()['d'] = trienode.TrieNode()
    t._root.children()['d'].children()['o'] = trienode.TrieNode()
    t._root.children()['d'].children()['o'].children()['g'] = trienode.TrieNode('woof woof')
    try:
        user = t.find_node('do')
        expected = t._root.children()['d'].children()['o']
        if user != expected:
            add_fail('Trie Find Node', 5.1, "ERROR: expected find_node('do') to return node 'do', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('Trie Find Node', 5, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('Trie Find Node', 5)
    
    # Append the results
    if L_TEST_RES:
        RESULTS[0].extend(S_TEST_RES)
        RESULTS[1].extend(L_TEST_RES)
    else:
        RESULTS[0].append("Trie Find Node: \t   Passes All 5 Tests")
        
def test_lextrie_find_all():
    global S_TEST_RES
    global L_TEST_RES
    global TEST_PASSED
    S_TEST_RES, L_TEST_RES = [], []
    
    # Test 1: One word trie, find all words with the empty string prefix.
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode('The letter T')
    try:
        user = t.find_all('')
        expected = ['t']
        if user != expected:
            add_fail('LexTrie Find All', 1.1, "ERROR: expected find_all('') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 1, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 1)
        
    # Test 2: One letter trie, find all words with that one letter prefix.
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode('The letter T')
    try:
        user = t.find_all('t')
        expected = ['t']
        if user != expected:
            add_fail('LexTrie Find All', 2.1, "ERROR: expected find_all('t') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 2, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 2)    
        
    # Test 3: Like Test #2 but with a tree of height 3
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode()
    t._root.children()['t'].children()['o'] = trienode.TrieNode()
    t._root.children()['t'].children()['o'].children()['p'] = trienode.TrieNode('The word TOP')
    try:
        user = t.find_all('top')
        expected = ['top']
        if user != expected:
            add_fail('LexTrie Find All', 3.1, "ERROR: expected find_all('top') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 3, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 3)
        
    # Test 4: Two word trie (no common letters), find all words
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode()
    t._root.children()['t'].children()['o'] = trienode.TrieNode('The word TO')
    t._root.children()['h'] = trienode.TrieNode()
    t._root.children()['h'].children()['i'] = trienode.TrieNode('The word HI')
    try:
        user = t.find_all('')
        user.sort()
        expected = ['hi', 'to']
        if user != expected:
            add_fail('LexTrie Find All', 4.1, "ERROR: expected find_all('') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 4, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 4)
    
    # Test 5: Two word trie (no common letters), find all words that start with 'h'
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode()
    t._root.children()['t'].children()['o'] = trienode.TrieNode('The word TO')
    t._root.children()['h'] = trienode.TrieNode()
    t._root.children()['h'].children()['i'] = trienode.TrieNode('The word HI')
    try:
        user = t.find_all('h')
        user.sort()
        expected = ['hi']
        if user != expected:
            add_fail('LexTrie Find All', 5.1, "ERROR: expected find_all('h') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 5, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 5)    
        
    # Test 6: Short word and longer overlapping word.
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['d'] = trienode.TrieNode()
    t._root.children()['d'].children()['o'] = trienode.TrieNode('The word DO')
    t._root.children()['d'].children()['o'].children()['t'] = trienode.TrieNode()
    t._root.children()['d'].children()['o'].children()['t'].children()['s'] = trienode.TrieNode('The word DOTS')
    try:
        user = t.find_all('do')
        user.sort()
        expected = ['do','dots']
        if user != expected:
            add_fail('LexTrie Find All', 6.1, "ERROR: expected find_all('do') to return '" + str(expected) + "', but got '" + str(user) + "'")            
        user = t.find_all('dots')
        expected = ['dots']
        if user != expected:
            add_fail('LexTrie Find All', 6.2, "ERROR: expected find_all('dots') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 6, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 6)  
        
    # Test 7: Try using a nonempty prefix and an empty tree.
    TEST_PASSED = True
    t = lextrie.LexTrie()
    try:
        user = t.find_all('blahblah')
        user.sort()
        expected = []
        if user != expected:
            add_fail('LexTrie Find All', 7.1, "ERROR: expected find_all('blahblah') to return '" + str(expected) + "', but got '" + str(user) + "'")            
    except Exception, e:
        add_fail('LexTrie Find All', 7, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('LexTrie Find All', 7)  
        
    # Append the results
    if L_TEST_RES:
        RESULTS[0].extend(S_TEST_RES)
        RESULTS[1].extend(L_TEST_RES)
    else:
        RESULTS[0].append("LexTrie Find All: \t   Passes All 7 Tests")

def test_gametrie():
    global S_TEST_RES
    global L_TEST_RES
    global TEST_PASSED
    S_TEST_RES, L_TEST_RES = [], []

    # Test 1: One letter Trie, tree should be losing.
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode('The letter T')
    try:
        g = gametrie.GameTrie(t._root, 2)
        user = bool(g._root.children()['t'].data())
        expected = False
        if user != expected:
            add_fail('GameTrie', 1.1, "ERROR: expected _root.children['t'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
        else:
            user = bool(g._root.data())
            expected = False
            if user != expected:
                add_fail('GameTrie', 1.2, "ERROR: expected _root.data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
    except Exception, e:
        add_fail('GameTrie', 1, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('GameTrie', 1)
    
    # Test 2: Two letter Trie, 2p game, tree should be winning. 
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode()
    t._root.children()['t'].children()['o'] = trienode.TrieNode('The word TO')
    try:
        g = gametrie.GameTrie(t._root, 2)
        user = bool(g._root.children()['t'].children()['o'].data())
        expected = True
        if user != expected:
            add_fail('GameTrie', 2.1, "ERROR: expected _root.children()['t'].children()['o'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
        else:
            user = bool(g._root.children()['t'].data())
            expected = True
            if user != expected:
                add_fail('GameTrie', 2.2, "ERROR: expected _root.children()['t'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
            else:
                user = bool(g._root.data())
                expected = True
                if user != expected:
                    add_fail('GameTrie', 2.3, "ERROR: expected _root.data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
    except Exception, e:
        add_fail('GameTrie', 2, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('GameTrie', 2)
        
    # Test 3: Two letter Trie, 3p game, tree should still be winning. 
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['t'] = trienode.TrieNode()
    t._root.children()['t'].children()['o'] = trienode.TrieNode('The word TO')
    try:
        g = gametrie.GameTrie(t._root, 3)
        user = bool(g._root.children()['t'].children()['o'].data())
        expected = True
        if user != expected:
            add_fail('GameTrie', 3.1, "ERROR: expected _root.children()['t'].children()['o'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
        else:
            user = bool(g._root.children()['t'].data())
            expected = True
            if user != expected:
                add_fail('GameTrie', 3.2, "ERROR: expected _root.children()['t'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
            else:
                user = bool(g._root.data())
                expected = True
                if user != expected:
                    add_fail('GameTrie', 3.3, "ERROR: expected _root.data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
    except Exception, e:
        add_fail('GameTrie', 3, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('GameTrie', 3)
        
    # Test 4: Two word Trie, 2p game, root should still be winning. 
    TEST_PASSED = True
    t = lextrie.LexTrie()
    t._root.children()['z'] = trienode.TrieNode('The letter Z')
    t._root.children()['d'] = trienode.TrieNode()
    t._root.children()['d'].children()['o'] = trienode.TrieNode('The word DO')
    try:
        g = gametrie.GameTrie(t._root, 2)
        user = bool(g._root.children()['d'].children()['o'].data())
        expected = True
        if user != expected:
            add_fail('GameTrie', 4.1, "ERROR: expected _root.children()['d'].children()['o'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
        else:
            user = bool(g._root.children()['d'].data())
            expected = True
            if user != expected:
                add_fail('GameTrie', 4.2, "ERROR: expected _root.children()['d'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
        user = bool(g._root.children()['z'].data())
        expected = False
        if user != expected:
            add_fail('GameTrie', 4.3, "ERROR: expected _root.children()['z'].data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
        if TEST_PASSED:
            user = bool(g._root.data())
            expected = True
            if user != expected:
                add_fail('GameTrie', 4.4, "ERROR: expected _root.data() to be '" + str(expected) + "', but was '" + str(user) + "'")            
    except Exception, e:
        add_fail('GameTrie', 4, get_exception(e) + ": " + str(e))
    if TEST_PASSED:
        add_success('GameTrie', 4)
        
    # Test 5: c0dialke's Test Cases, 2p, 3p, 4p, and 5p versions of short.txt
    TEST_PASSED = True
    if 'Passes All' in RESULTS[0][0] and 'Insert' in RESULTS[0][0]:
        t = lextrie.LexTrie()
        try:
            word_file = open("short.txt")
            for line in word_file.readlines():
                pair = line.split('::')
                t.insert(pair[0], pair[1].rstrip())
            word_file.close()
            user = str(gametrie.GameTrie(t._root, 2))
            expected = 'True {c: False {o: False {o: False {k: True {}, l: True {e: True {r: True {}}}}}}, b: True {a: True {r: False {i: True {s: True {t: True {a: True {s: True {}}}}}}, g: False {}, n: True {k: True {}, n: True {e: True {r: True {}}}}}}}'
            if user != expected:
                add_fail('GameTrie', 5.1, "ERROR: expected the string representation of the tree to be '" + str(expected) + "', but got '" + str(user) + "'")            
            user = str(gametrie.GameTrie(t._root, 3))
            expected = 'True {c: True {o: True {o: True {k: False {}, l: False {e: True {r: True {}}}}}}, b: True {a: True {r: True {i: True {s: True {t: True {a: True {s: True {}}}}}}, g: True {}, n: True {k: False {}, n: True {e: True {r: True {}}}}}}}'
            if user != expected:
                add_fail('GameTrie', 5.2, "ERROR: expected the string representation of the tree to be '" + str(expected) + "', but got '" + str(user) + "'")            
            user = str(gametrie.GameTrie(t._root, 4))
            expected = 'True {c: True {o: True {o: True {k: True {}, l: True {e: True {r: True {}}}}}}, b: True {a: True {r: True {i: True {s: True {t: True {a: True {s: True {}}}}}}, g: True {}, n: True {k: True {}, n: True {e: True {r: True {}}}}}}}'
            if user != expected:
                add_fail('GameTrie', 5.3, "ERROR: expected the string representation of the tree to be '" + str(expected) + "', but got '" + str(user) + "'")            
            user = str(gametrie.GameTrie(t._root, 5))
            expected = 'True {c: True {o: True {o: True {k: True {}, l: True {e: False {r: False {}}}}}}, b: False {a: False {r: True {i: True {s: True {t: True {a: True {s: True {}}}}}}, g: True {}, n: False {k: True {}, n: False {e: False {r: False {}}}}}}}'
            if user != expected:
                add_fail('GameTrie', 5.4, "ERROR: expected the string representation of the tree to be '" + str(expected) + "', but got '" + str(user) + "'")            
    
        except IOError, e:
            add_fail('GameTrie', 5, get_exception(e) + ": You should put 'short.txt' in the same folder as this file.")
        except Exception, e:
            add_fail('GameTrie', 5, get_exception(e) + ": " + str(e))
        if TEST_PASSED:
            add_success('GameTrie', 5)
    else:
        add_fail('GameTrie', 5, "WARNING: This test did not run since 'insert()' is required for this test. This test will automatically run once all test cases for insert() pass.")
    
    # Test 6: Xiangxin Jing's Test Cases. Counts losing nodes in large GameTries.
    TEST_PASSED = True
    if 'Passes All' in RESULTS[0][0] and 'Insert' in RESULTS[0][0]:
        try:
            user = gametrie_test('short.txt', 3, '')
            expected = [9, 3]
            if user != expected:
                add_fail('GameTrie', 6.1, "ERROR: gametrie_test returns data in the format [inserted_nodes, num_losing_nodes]. It should've returned '" + str(expected) + "', but got '" + str(user) + "'")            
            user = gametrie_test('medium.txt', 4, 'c')
            expected = [8070, 972]
            if user != expected:
                add_fail('GameTrie', 6.2, "ERROR: gametrie_test returns data in the format [inserted_nodes, num_losing_nodes]. It should've returned '" + str(expected) + "', but got '" + str(user) + "'")            
            user = gametrie_test('long.txt', 4, 'c')
            expected = [80362, 4269]
            if user != expected:
                add_fail('GameTrie', 6.3, "ERROR: gametrie_test returns data in the format [inserted_nodes, num_losing_nodes]. It should've returned '" + str(expected) + "', but got '" + str(user) + "'")            
        except IOError, e:
            add_fail('GameTrie', 6, get_exception(e) + ": You should put 'short.txt', 'medium.txt', and 'long.txt' in the same folder as this file.")
        except Exception, e:
            add_fail('GameTrie', 6, get_exception(e) + ": " + str(e))
        if TEST_PASSED:
            add_success('GameTrie', 6)
    else:
        add_fail('GameTrie', 6, "WARNING: This test did not run since 'insert()' is required for this test. This test will automatically run once all test cases for insert() pass.")   
        
    # Append the results
    if L_TEST_RES:
        RESULTS[0].extend(S_TEST_RES)
        RESULTS[1].extend(L_TEST_RES)
    else:
        RESULTS[0].append("GameTrie: \t\t   Passes All 6 Tests")

def gametrie_test(path, p, prefix):
    def _test_find_nodes(start_node, lst):
        lst.append(start_node.data())
        for c in start_node.children():
            _test_find_nodes(start_node.children()[c], lst)        

    def test_count_nodes(start_node):
        lst = []
        _test_find_nodes(start_node, lst)
        return sum(1 for i in lst if not i)

    new_lextrie = lextrie.LexTrie(path)
    inserted = len(new_lextrie.find_all(''))
    my_gametrie = gametrie.GameTrie(new_lextrie.find_node(prefix), p)	  
    return [inserted, test_count_nodes(my_gametrie._root)]

def get_exception(e):
    string = str(type(e))
    i1 = string.rfind('.') + 1
    i2 = string.rfind("'")
    return string[i1:i2]
    
def add_fail(func, test_num, e):
    global TEST_PASSED
    if func == 'GameTrie':
        string = ':\t\t=> Fails Test '
    else:
        string = ':\t=> Fails Test '    
    S_TEST_RES.append(func + string + str(test_num))
    L_TEST_RES.append(func + " - Test " + str(test_num) + ":\n    " + str(e) + "\n")
    TEST_PASSED = False
    
def add_success(func, test_num):
    if func == 'GameTrie':
        string = ': \t\t   Passes Test '
    else:
        string = ': \t   Passes Test '
    S_TEST_RES.append(func + string + str(test_num))

if __name__ == '__main__':
    start = time.time()    
    if trie_insert_completed:
        test_trie_insert()
    else:
        RESULTS[0].append("Trie Insert:\t=> Test Skipped")
        RESULTS[1].append("Trie Insert:\n    Test skipped, you can change this at the top of the test file.\n")
    if trie_find_node_completed:
        test_trie_find_node()
    else:
        RESULTS[0].append("Trie Find Node:\t=> Test Skipped")
        RESULTS[1].append("Trie Find Node:\n    Test skipped, you can change this at the top of the test file.\n")
    if lextrie_find_all_completed:
        test_lextrie_find_all()
    else:
        RESULTS[0].append("LexTrie Find All:\t=> Test Skipped")
        RESULTS[1].append("LexTrie Find All:\n    Test skipped, you can change this at the top of the test file.\n")
    if gametrie_completed:
        test_gametrie()
    else:
        RESULTS[0].append("GameTrie:\t\t=> Test Skipped")
        RESULTS[1].append("GameTrie:\n    Test skipped, you can change this at the top of the test file.\n")
    run_time = str(round(time.time() - start, 3))
    print "\n\n\n               Timo's Tests v3.0\n"
    print "              *** Test Results ***\n"
    for item in RESULTS[0]:
        print "     " + item
    if show_running_time:
        print "\n\t\t\t   Time Taken: " + run_time + " seconds"
    if show_detailed_errors and len(RESULTS[1]):
        print "\n\n\n            *** Detailed Results ***\n"
        for item in RESULTS[1]:
            print item
    print 