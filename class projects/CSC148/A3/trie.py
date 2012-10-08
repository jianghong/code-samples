"""A naive implementation of the trie data type.

Trie supports the following operations:

-- data(word): return the data of the TrieNode associated with 'word'.
-- find_node(word): return the TrieNode associated with 'word'.
-- insert(word, data): insert a new TrieNode.
"""

from trienode import TrieNode

class Trie(object):
    """A Trie of TrieNodes. Trie has the following attributes:
     -- _root: a TrieNode; the root of this Trie.
    """

    def __init__(self):
        """Create an empty Trie."""

        self._root = TrieNode()
                    
    def insert(self, word, data):
        """Insert the string 'word' with data 'data' into this Trie.

        -- word: the string with which the newly inserted 'data' will
           be associated.
        -- data: the data which will be stored in the TrieNode
           associated with the string 'word'.

        If there is a TrieNode associated with the word 'word' in this
        Trie, then _data of this TrieNode is updated to 'data'. Otherwise,
        enough new TrieNodes are created and inserted into this Trie, to
        create a TrieNode associated with 'word'.
        """
        
        def _insert(root, word, data):
            """Create and attach enough TrieNodes associated with word 'word'
            onto root."""
            
            # Base case, associates data with the final letter of word
            if len(word) == 1:    
                root.children()[word] = TrieNode(data)
            else:
                # Create new TrieNode only if letter is not in Trie
                if word[0] not in root.children():
                    root.children()[word[0]] = TrieNode()
                return _insert(root.children()[word[0]], word[1:], data)
        if self.find_node(word):
            self.find_node(word).set_data(data)
        else:
            return _insert(self._root, word, data)

    def find_node(self, word):
        """Return the TrieNode that corresponds to the string 'word'
        in this Trie. Return None if there is no such TrieNode in this
        Trie.
        -- word: a string; the TrieNode that corresponds to 'word'
        (if it exists) is returned.
        """
        
        def _find_node(root, word):
            """Return the TrieNode that corresponds to the string 'word' in 
            Trie rooted at root. Return None if no such TrieNode is found."""
            
            if len(word) <= 1:
                if word in root.children():
                    return root.children()[word]
            else:
                # Continue checking letters in word until its found
                if word[0] in root.children():
                    return _find_node(root.children()[word[0]], word[1:])
                else:  # Stop when the next letter is no longer in Trie
                    return None
        if word == '':
            return self._root
        return _find_node(self._root, word)
                    
    def data(self, word):
        """Return the data associated with the string 'word' in this
        Trie.  Return None if 'word' is not in the Trie.
        """

        try:
            return self.find_node(word).data()
        except AttributeError:
            return None

    def __str__(self):
        """Return a (really bad) string representation of this
        Trie. Helps with debugging."""

        return _str(self._root)

def _str(node):
    """Return a (really bad) string representation of the trie rooted
    at TrieNode 'node'. Helps with debugging."""

    res = str(node) + " {"
    for key in node.children():
        res += key + ": " + _str(node.children()[key]) + ", "
    if node.children():
        return res[:-2] + "}"
    return res + "}"
