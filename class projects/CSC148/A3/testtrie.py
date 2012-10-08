"""Test module Trie."""

import unittest
from trie import Trie

class TrieEmptyTestCase(unittest.TestCase):
    '''Test retrieving from empty Trie.'''
    
    def setUp(self):
        """Set up an empty trie."""
        
        self.trie = Trie()
        
    def tearDown(self):
        """Clean up."""
        
        self.trie = None
            
    def testData(self):
        """Test the data() method."""
        
        assert self.trie.data("coo") is None,\
               'found something in an empty trie!'
        
class TrieSingleTestCase(unittest.TestCase):
    '''Test inserting a single word into an empty Trie and
    retrieving it.'''

    def setUp(self):
        """Set up a single word trie."""
        
        self.trie = Trie()
        self.populate()
        
    def populate(self):
        """Populate the trie."""

        self.trie.insert("coo", "Coo's Data")
        
    def tearDown(self):
        """Clean up."""
        
        self.trie = None

    def testData(self):
        """Test the data() method with existing word."""
        
        found = self.trie.data("coo")
        assert found == "Coo's Data",\
               "found " + found + ", but expected Coo's Data"

    def testDataNotThere(self):
        """Test the data() method with non-existing word."""
        
        found = self.trie.data("not there")
        assert found is None,\
               "found " + found + ", but expected None"

class TrieSimpleTestCase(unittest.TestCase):
    '''Test inserting several words, with some common prefixes, into
    a Trie and retrieving them.'''

    def setUp(self):
        """Set up a simple trie. The words are the same as in the file
        short.txt."""
        
        self.trie = Trie()
        self.populate()
        
    def populate(self):
        """Populate the trie."""

        self.trie.insert("coo", "Coo's Data")
        self.trie.insert("cool", "Cool's Data")
        self.trie.insert("coo", "Coo's Data")
        self.trie.insert("bar", "Bar's Data")
        self.trie.insert("cooler", "Cooler's Data")
        self.trie.insert("baristas", "Baristas's Data")
        self.trie.insert("cook", "Cook's Data")
        self.trie.insert("banner", "Banner's Data")
        self.trie.insert("bag", "Bag's Data")
        self.trie.insert("bank", "Bank's Data")
        
    def tearDown(self):
        """Clean up."""
        
        self.trie = None

    def testData0(self):
        """Test the data() method with valid word."""
        
        found = self.trie.data("coo")
        assert found == "Coo's Data",\
               "found " + found + ", but expected Coo's Data"

    def testData1(self):
        """Test the data() method with valid word."""
        
        found = self.trie.data("bar")
        assert found == "Bar's Data",\
               "found " + found + ", but expected Bar's Data"

    def testData2(self):
        """Test the data() method with valid word that contains
        another valid word as prefix."""
        
        found = self.trie.data("cooler")
        assert found == "Cooler's Data",\
               "found " + found + ", but expected Cooler's Data"

    def testData3(self):
        """Test the data() method with valid word that contains
        another valid word as prefix."""
        
        found = self.trie.data("cool")
        assert found == "Cool's Data",\
               "found " + found + ", but expected Cool's Data"

    def testData4(self):
        """Test the data() method with terminal valid word."""
        
        found = self.trie.data("baristas")
        assert found == "Baristas's Data",\
               "found " + found + ", but expected Baristas's Data"

    def testData5(self):
        """Test the data() method with terminal valid word."""
        
        found = self.trie.data("banner")
        assert found == "Banner's Data",\
               "found " + found + ", but expected Banner's Data"

    def testDataNotIn(self):
        """Test the data() method with non-existant word."""
        
        found = self.trie.data("notHere")
        assert found is None,\
               "found " + found + ", but expected None"

    def testDataNotAWord(self):
        """Test the data() method with non-existent word that contains
        a valid word as prefix."""
        
        found = self.trie.data("barr")
        assert found is None,\
               "found " + found + ", but expected None"

def empty_suite():
    """Return a test suite for an empty trie."""
    
    return unittest.TestLoader().loadTestsFromTestCase(TrieEmptyTestCase)

def single_suite():
    """Return a test suite for a single-word trie."""

    return unittest.TestLoader().loadTestsFromTestCase(TrieSingleTestCase)

def simple_suite():
    """Return a test suite for a larger, simple trie."""

    return unittest.TestLoader().loadTestsFromTestCase(TrieSimpleTestCase)

if __name__ == '__main__':
    """Go!"""

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(empty_suite())
    runner.run(single_suite())
    runner.run(simple_suite())
