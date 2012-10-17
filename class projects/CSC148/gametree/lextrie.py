"""A lexicon trie.

To create a non-empty lexicon Trie, the user needs to supply either a
list of tuples (word, data), or a path to an input file. The format of
the input file is:

<word0>::<word0's definition>
<word1>::<word1's definition>
...

<wordi's definition> then becomes the data field of a TrieNode that
corresponds to the string <wordi>.

LexTrie supports the following operations (in addition to those of Trie):

-- is_word(word): return whether 'word' is a valid word in this Trie.
-- find_all(prefix): return a list of (valid) words with prefix 'prefix'.
"""

from trie import Trie, TrieNode

class LexTrie(Trie):
    """A lexicon Trie. LexTrie has the following attributes:
     -- _root: a TrieNode; the root of this Trie.
    """

    def __init__(self, words=None):
        """Create a Trie from 'words'. If 'words' is not specified,
        create an empty Trie.

        -- words: either a (string) file path or a (word, data) list.
        """

        Trie.__init__(self)
        if words:
            if isinstance(words, str):
                self._read_words(words)
            else:
                for (word, data) in words:
                    self.insert(word, data)
                    
    def is_word(self, word):
        """Return True if 'word' is a valid word and False otherwise."""

        return self.data(word) is not None

    def find_all(self, prefix):
        """Return a list of valid words with prefix 'prefix' in this
        Trie.

        -- prefix: a string; all valid words from this Trie that begin
        with 'prefix' are returned."""

        def _find_all(trienode, mem, valid_words=[]):
            """Return a list of valid words starting from trienode. mem is a 
            string that is used to remember the word up until root."""
        
            if trienode.data(): 
                valid_words.append(mem)
            if trienode.children():
                for children in trienode.children():
                    _find_all(trienode.children()[children], mem + children,
                                  valid_words)
            return valid_words
        # Return all words if prefix is empty string
        if prefix == '':
            return _find_all(self._root, prefix)
        if self.find_node(prefix):
            return _find_all(self.find_node(prefix), prefix)
        return []

    def _read_words(self, path):
        """Insert every word from the word input file 'path' into this
        Trie.

        -- path: a string; a full path to the input file."""

        word_file = open(path)
        for line in word_file.readlines():
            pair = line.split('::')
            self.insert(pair[0], pair[1].rstrip())
        word_file.close()
