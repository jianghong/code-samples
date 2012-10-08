"""Test module GameTrie."""

import unittest
from lextrie import LexTrie
from gametrie import GameTrie

# Should any part of your code go wrong, scroll down to where the assert
# statements are. There, you'll find what the string representation of your trie
# should actually be. (hopefully)

class SingleTestCase(unittest.TestCase):
    """Game trie based on a single one-letter word lex trie, root is
    not winning."""

    def setUp(self):
        """Make a single one-letter word lex trie."""
        
        self.lextrie = LexTrie()
        self.lextrie.insert("a", "AAA")
        self.gametrie = GameTrie(self.lextrie._root, 2)
        
    def tearDown(self):
        """Clean up."""
        
        self.lextrie = None
        self.gametrie = None

    def test(self):
        """Test: the root of this trie should not be winning."""
        
        win = self.gametrie.is_winning(self.gametrie._root)
        assert not win,\
               "root should not be winning!"

class SimpleTestCase(unittest.TestCase):
    """Game trie based on a very simple lex trie, root is winning."""

    def setUp(self):
        """Make a simle lex trie."""

        self.lextrie = LexTrie()
        self.lextrie.insert("a", "AAA")
        self.lextrie.insert("bb", "BBB")
        self.gametrie = GameTrie(self.lextrie._root, 2)
        
    def tearDown(self):
        """Clean up."""
        
        self.lextrie = None
        self.gametrie = None

    def test(self):
        """Test: the root of this trie should be winning."""

        win = self.gametrie.is_winning(self.gametrie._root)
        assert win,\
               "root should be winning!"

class LargerTestCase(unittest.TestCase):
    """Set up for larger test cases."""
    
    def setUp(self, num_players):
        """Make a lex and game tries for a game with 'num_players'
        players. The words are the same as in the file short.txt."""

        self.lextrie = LexTrie()
        self.lextrie.insert("cool", "Cool's Data")
        self.lextrie.insert("coo", "Coo's Data")
        self.lextrie.insert("bar", "Bar's Data")
        self.lextrie.insert("cooler", "Cooler's Data")
        self.lextrie.insert("baristas", "Baristas's Data")
        self.lextrie.insert("cook", "Cook's Data")
        self.lextrie.insert("banner", "Banner's Data")
        self.lextrie.insert("bag", "Bag's Data")
        self.lextrie.insert("bank", "Bank's Data")
        self.gametrie = GameTrie(self.lextrie._root, num_players)
        
    def tearDown(self):
        """Clean up."""
        
        self.lextrie = None
        self.gametrie = None

    def winning(self, word):
        """Return whether playing 'word' results in a winning position."""
        
        return self.gametrie.is_winning(self.gametrie.find_node(word))

class LargerTestCaseTwoPlayers(LargerTestCase):
    """Test on a larger trie, two players."""

    def setUp(self):
        """Set up the game with 2 players."""
        
        LargerTestCase.setUp(self, 2)
        
    def testAllWinning(self):
        """Check that all strings that should be winning are winning."""
        
        allWinStrings = ["", "cool", "coole", "cooler", "cook",
                         "b", "ba", "ban", "bank", "bann", "banne", "banner",
                         "bari", "baris", "barist", "barista", "baristas"]
        errors = [prefx for prefx in allWinStrings if not self.winning(prefx)]
        assert not errors,\
               ("the following are incorrectly marked as not winning: " +
                str(errors))

    def testAllLosing(self):
        """Check that all strings that should not be winning are not
        winning."""

        allLoseStrings = ["c", "co", "coo", "bag", "bar"]
        errors = [prefix for prefix in allLoseStrings if self.winning(prefix)]
        assert not errors,\
               ("the following are incorrectly marked as winning: " +
                str(errors))
        
class CustomTestCase(unittest.TestCase):
    """Tests many base cases."""
    
    def setUp(self):
        """Initialize stuff."""
        self.lextrie = LexTrie()
        
    def tearDown(self):
        """Reset stuff."""
        self.lextrie = None
        self.gametrie = None

class CustomTestCase_OneWord2Players(CustomTestCase):
    """Test 1 word with 2 players."""
    
    def testWinningCase(self):
        """Test with a 4 letter word and 2 players."""
        
        self.lextrie.insert('code', 'secret')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'True {c: True {o: True {d: True {e: True {}}}}}', \
               'GameTrie fails single 4 letter word. You got ' + str(self.gametrie)
        
    def testLosingCase(self):
        """Test with a 3 letter word and 2 players."""
        
        self.lextrie.insert('cod', 'Fish, I think??')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'False {c: False {o: False {d: False {}}}}', \
               'GameTrie fails single 3 letter word. You got ' + str(self.gametrie)
        
class CustomTestCase_2WordsInOne2Players(CustomTestCase):
    """Test 2 words, where one is contained in the other with 2 players."""
    
    def testOnlyCase(self):
        """Test with a 3 letter word in a 4 letter word with 2 players."""
        
        self.lextrie.insert('cod', 'Fish??')
        self.lextrie.insert('code', 'secret')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'False {c: False {o: False {d: False {e: True {}}}}}', \
               'GameTrie fails with 2 words, one contained in the other. You got ' + str(self.gametrie)

class CustomTestCase_2WordsThisPlayerDecides2Players(CustomTestCase):
    """Test 2 words, where they have the same prefix, and player who made the
    gametrie decides the winning or losing node."""
    
    def setUp(self):
        """Additional setting up."""
        
        CustomTestCase.setUp(self)
        self.lextrie.insert('cow', 'cattle')
        self.lextrie.insert('code', 'secret')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        
    def testWordCode(self):
        """Test to see if the node corresponding to 'code' is correct."""
        
        assert self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['o'].children()['d'].children()['e']), \
               "Evaluated valid word 'code' as losing, when it is winning."
        
    def testWordCow(self):
        """Test to see if the node corresponding to 'cow' is correct."""
        
        assert not self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['o'].children()['w']), \
               "Evaluated valid word 'cow' as winning, when it is losing."
        
    def testConflictNodeCo(self):
        """Test to see if the node corresponding to 'co' is correct."""
        
        assert self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['o']), \
               "Evaluated word 'co' as losing, when it is winning."
        
    def testWholeCase(self):
        """Test to see if the whole GameTrie is lablled correctly."""
        
        assert str(self.gametrie) == 'True {c: True {o: True {d: True {e: True {}}, w: False {}}}}', \
               "Evaluated some part of the GameTrie wrong, You got " + str(self.gametrie)
        
class CustomTestCase_2WordsOtherPlayerDecides2Players(CustomTestCase):
    """Test 2 words where the other player decides if a node is winning or
    losing."""
    
    def setUp(self):
        """Additional setting up."""
        
        CustomTestCase.setUp(self)
        self.lextrie.insert('cow', 'cattle')
        self.lextrie.insert('chow', 'a way to say you are eating.')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        
    def testWordCow(self):
        """Test to see if the node corresponding to 'cow' is correct."""
        
        assert not self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['o'].children()['w']), \
               "Evaluated valid word 'cow' as winning, when it is losing."
        
    def testWordChow(self):
        """Test to see if the node corresponding to 'chow' is correct."""
        
        assert self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['h'].children()['o'].children()['w']), \
               "Evaluated valid word 'chow' as losing, when it is winning."
        
    def testConflictNodeC(self):
        """Test to see if the node corresponding to 'c' is correct."""
        
        assert not self.gametrie.is_winning(self.gametrie._root.children()['c']), \
               "Evaluated word 'c' as winning, when it is losing."
        
    def testWholeCase(self):
        """Test to see if the whole GameTrie is built properly."""
        
        assert str(self.gametrie) == 'False {c: False {h: True {o: True {w: True {}}}, o: False {w: False {}}}}', \
               "Evaluated some part of the GameTrie wrong. You got " + str(self.gametrie)
        
class CustomTestCase_2WordsThisPlayerChoosingAmongAllLosingOrAllWinning(CustomTestCase):
    """Test whether the correct decision is made when choosing among all winning
    or all losing nodes."""
    
    def testAllLosing(self):
        """Test when choosing among all losing leads to a loss."""
        
        self.lextrie.insert('hot', 'high temperature')
        self.lextrie.insert('how', 'beginning of a question')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'False {h: False {o: False {t: False {}, w: False {}}}}', \
               "Evaluated some part of the GameTrie wrong. You got " + str(self.gametrie)
        
    def testAllWinning(self):
        """Test when choosing among all winning leads to a win."""
        
        self.lextrie.insert('show', 'to reveal something')
        self.lextrie.insert('shin', 'part of the body')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'True {s: True {h: True {i: True {n: True {}}, o: True {w: True {}}}}}', \
               "Evaluated some part of the GameTrie wrong. You got " + str(self.gametrie)
        
class CustomTestCase_2WordsOtherPlayerChoosingAmongAllLosingOrAllWinning(CustomTestCase):
    """Test whether the correct decision is made when choosing among all winning
    or all losing nodes."""
    
    def testAllLosing(self):
        """Test when choosing among all losing leads to a loss."""
        
        self.lextrie.insert('shinn', 'anime character')
        self.lextrie.insert('shirt', 'thin piece of clothing')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'False {s: False {h: False {i: False {r: False {t: False {}}, n: False {n: False {}}}}}}', \
               "Evaluated some part of the GameTrie wrong. You got " + str(self.gametrie)
        
    def testAllWinning(self):
        """Test when choosing among all winning leads to a win."""
        
        self.lextrie.insert('shop', 'to buy many things')
        self.lextrie.insert('shot', 'firing of a bullet')
        self.gametrie = GameTrie(self.lextrie._root, 2)
        assert str(self.gametrie) == 'True {s: True {h: True {o: True {p: True {}, t: True {}}}}}', \
               "Evaluated some part of the GameTrie wrong. You got " + str(self.gametrie)
        
class CustomTestCase_ChildNodeOverridenByCurrentNodeThisPlayerLoses(CustomTestCase):
    """Test whether program overides child nodes when needed. This test results
    in this player losing.
    
    Test: Even though another player must choose between winning nodes, the
    current node is losing, because this player created a word.
    """
    
    def setUp(self):
        """Set up some extra stuff."""
        
        CustomTestCase.setUp(self)
        self.lextrie.insert('hold', 'to have something in possession')
        self.lextrie.insert('holder', 'someone who holds something')
        self.lextrie.insert('holdings', 'currently in possession of something')
        self.gametrie = GameTrie(self.lextrie._root, 3)
    
    def testWordHolder(self):
        """Test if the valid word 'holder' is evaluated correctly."""
        
        assert self.gametrie.is_winning(self.gametrie._root.children()['h'].children()['o'].children()['l'].children()['d'].children()['e'].children()['r']), \
               "Evaluated the valid word 'holder' as losing when it is winning."
    
    def testWordHoldings(self):
        """Test if the valid word 'holdings' is evaluated correctly."""
        
        assert self.gametrie.is_winning(self.gametrie._root.children()['h'].children()['o'].children()['l'].children()['d'].children()['i'].children()['n'].children()['g'].children()['s']), \
               "Evaluated the valid word 'holdings' as losing when it is winning."
        
    def testWordHold(self):
        """Test if the valid word 'hold' is evaluated correctly."""
        
        assert not self.gametrie.is_winning(self.gametrie._root.children()['h'].children()['o'].children()['l'].children()['d']), \
               "Evaluated the valid word 'hold' as winning when it is losing."
        
    def testWholeCase(self):
        """Test if the whole GameTrie is built correctly."""
        
        assert str(self.gametrie) == 'False {h: False {o: False {l: False {d: False {i: True {n: True {g: True {s: True {}}}}, e: True {r: True {}}}}}}}', \
               "Evaluated some part of the GameTrie wrong. You got " + str(self.gametrie)
        
class CustomTestCase_ChildNodeOverridenByCurrentNodeThisPlayerWins(CustomTestCase):
    """Test whether program overides child nodes when needed. This test results
    in this player winning.
    
    Test: Even though this player must choose between losing nodes, the
    current node is losing, because the other player created a word.
    """
    
    def setUp(self):
        """Set Up some extra stuff."""
        
        CustomTestCase.setUp(self)
        self.lextrie.insert('clo', 'not even a real word, but whatevs xD')
        self.lextrie.insert('clowned', "clown isn't a real word here")
        self.lextrie.insert('clouded', "cloud isn't a real word here either")
        self.gametrie = GameTrie(self.lextrie._root, 3)
        
    def testWordClowned(self):
        """Test to see if the valid word 'clowned' is labeled correctly."""
        
        assert not self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['l'].children()['o'].children()['w'].children()['n'].children()['e'].children()['d']), \
               "Evaluated the valid word 'clowned' as winning, when it is losing."
        
    def testWordClouded(self):
        """Test to see if the valid word 'clouded' is labeled correctly."""
        
        assert not self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['l'].children()['o'].children()['u'].children()['d'].children()['e'].children()['d']), \
               "Evaluated the valid word 'clowned' as winning, when it is losing."
        
    def testWordClowned(self):
        """Test to see if the valid word 'clowned' is labeled correctly."""
        
        assert self.gametrie.is_winning(self.gametrie._root.children()['c'].children()['l'].children()['o']), \
               "Evaluated the valid word 'clo' as losing, when it is winning."
        
    def testWholeCase(self):
        """Test to see if the whole GameTrie is labeled correctly."""
        
        assert str(self.gametrie) == 'True {c: True {l: True {o: True {u: False {d: False {e: False {d: False {}}}}, w: False {n: False {e: False {d: False {}}}}}}}}', \
               "Evaluated the GameTrie wrong somewhere. You got " + str(self.gametrie)

def single_suite():
    """Return a test suite for a single word trie, as above."""
    
    return unittest.TestLoader().loadTestsFromTestCase(SingleTestCase)

def simple_suite():
    """Return a test suite for a simple trie, as above."""

    return unittest.TestLoader().loadTestsFromTestCase(SimpleTestCase)

def larger_suite_2():
    """Return a larger test suite, as above, with 2 players."""

    return unittest.TestLoader().loadTestsFromTestCase(
        LargerTestCaseTwoPlayers)

def custom_suite_1():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_OneWord2Players)

def custom_suite_2():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_2WordsInOne2Players)

def custom_suite_3():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_2WordsThisPlayerDecides2Players)

def custom_suite_4():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_2WordsOtherPlayerDecides2Players)

def custom_suite_5():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_2WordsThisPlayerChoosingAmongAllLosingOrAllWinning)

def custom_suite_6():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_2WordsOtherPlayerChoosingAmongAllLosingOrAllWinning)

def custom_suite_7():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_ChildNodeOverridenByCurrentNodeThisPlayerLoses)

def custom_suite_8():
    """Return a custom test suite."""
    
    return unittest.TestLoader().loadTestsFromTestCase(CustomTestCase_ChildNodeOverridenByCurrentNodeThisPlayerWins)

if __name__ == '__main__':
    """Go!"""

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(single_suite())
    runner.run(simple_suite())
    runner.run(larger_suite_2())
    
    # Custom tests start here.
    runner.run(custom_suite_1())
    runner.run(custom_suite_2())
    runner.run(custom_suite_3())
    runner.run(custom_suite_4())
    runner.run(custom_suite_5())
    runner.run(custom_suite_6())
    runner.run(custom_suite_7())
    runner.run(custom_suite_8())
