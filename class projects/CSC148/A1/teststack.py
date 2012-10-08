"""Test module Stack."""

import unittest
from stack import Stack, StackEmptyError

class StackEmptyTestCase(unittest.TestCase):
    """Test behaviour of an empty Stack."""
   
    def setUp(self):
        """Set up an empty stack."""
        
        self.stack = Stack()
        
    def tearDown(self):
        """Clean up."""
        
        self.stack = None
            
    def testIsEmpty(self):
        """Test is_empty() on empty Stack."""
        
        assert self.stack.is_empty(),\
               'is_empty returned False on an empty Stack!'
        
    def testTop(self):
        """Test top() on an empty Stack."""

        try:
            self.stack.top()
            assert False,\
                   'top() on an empty Stack succeeded!' 
        except StackEmptyError:
            pass

    def testPop(self):
        """Test pop() on an empty Stack."""

        try:
            self.stack.pop()
            assert False,\
                   'pop() on am empty Stack succeeded!' 
        except StackEmptyError:
            pass

    def testPush(self):
        """Test push to empty Stack."""

        self.stack.push("foo")
        assert self.stack.top() == "foo",\
               'Wrong item on top of the Stack! Expected "foo" here.'
               
class StackAllTestCase(unittest.TestCase):
    """Comprehensive tests of (non-empty) Stack."""

    def setUp(self):
        """Set up an empty stack."""
        
        self.stack = Stack()
        
    def tearDown(self):
        """Clean up."""
        
        self.stack = None

    def testAll(self):
        """Test pushing and popping multiple elements."""

        for item in range(20):
            self.stack.push(item)
            assert not self.stack.is_empty(),\
                   'is_empty() returned True on a non-empty Stack!'
            assert self.stack.top() == item,\
                   ('Something wrong on top of the Stack! Expected ' +
                    str(item) + '.')

        expect = 19
        while not self.stack.is_empty():
            assert self.stack.pop() == expect,\
                   ('Something wrong on top of the Stack! Expected ' +
                    str(expect) + '.')
            expect = expect - 1
        
def empty_suite():
    """Retrun a test suite for an empty Stack."""
    
    return unittest.TestLoader().loadTestsFromTestCase(StackEmptyTestCase)

def all_suite():
    """Retrun a comprehensive test suite for a non-empty Stack."""

    return unittest.TestLoader().loadTestsFromTestCase(StackAllTestCase)

# go!
runner = unittest.TextTestRunner()
runner.run(empty_suite())
runner.run(all_suite())
