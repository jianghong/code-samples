"""A node in a Trie. Do not modify this file. In fact, you should not
submit this file -- we will use our own, unmodified version, of this
file when testing your code.
"""

class TrieNode(object):
    """A node in a Trie. TrieNode has the following attributes:
     -- _data: data stored in this TrieNode.
     -- _children: a dictionary that maps characters to TrieNodes; the
        children of this TrieNode.
    """

    def __init__(self, data=None, children=None):
        """Create a new TrieNode that stores 'data' and has children
        'children'.
        -- data: the data stored in the new TrieNode.
        -- children: the children of the new TrieNode or None. If
        'children' is None, a node with no children, {}, is created.
        """

        self._data = data
        if children is None:
            self._children = {}
        else:
            self._children = children

    def data(self):
        """Return the data stored in this TrieNode."""

        return self._data

    def set_data(self, data):
        """Set the _data of this TrieNode to 'data'."""

        self._data = data
        
    def children(self):
        """Return the children of this TrieNode."""

        return self._children

    def is_leaf(self):
        """Return True, if this TrieNode has no children, and False,
        otherwise."""

        return not len(self._children)
    
    def __str__(self):
        """Return a string representation of this TrieNode."""

        return str(self.data())
