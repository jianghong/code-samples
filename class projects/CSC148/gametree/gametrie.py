"""A game trie in a game of Ghost.

A game trie is a player's mental image of the game. The data of a
TrieNode in this trie is True if this node is winning and False
otherwise.

GameTrie supports the following operations (in addition to those of
Trie):
 -- is_winning(node): return whether the TrieNode 'node' is winning.
"""

from trie import Trie, TrieNode

class GameTrie(Trie):
    """A game trie in a game of Ghost. GameTrie has the following
    attributes:
    -- _num_players: the number of players in the game.
    -- _root: the root TrieNode.
    """

    def __init__(self, start_node, num_players):
        """Create and return a GameTrie that corresponds to a lexicon
        subtrie rooted at node 'start_node', for a game with
        'num_players' players.

        -- start_node: a TrieNode in a LexTrie. The resulting GameTrie
        corresponds to a subtrie rooted at this node.
        -- num_players: the number of players in this game.

        Assumptions:
        -- 'start_node' is not a leaf node.
        -- 'num_players' >= 2.
        -- It is this player's turn in the game.
        """
        
        def _eval_node(node, num_players, count):
            """Return True if node is a winning node and False if node is a 
            losing node."""
            
            # Base case: node completes a word
            if node.data():
                return (count - 1) % num_players != 0
            # Case for current player's turn
            if count % num_players == 0:
                for trienode in node.children().values():
                        if _eval_node(trienode, num_players, count + 1):
                            return True
                return False
            # Case for not current player's turn
            else:
                for trienode in node.children().values():
                    if not _eval_node(trienode, num_players, count + 1):
                        return False
                return True
        
        def _insert_eval(root, node, num_players, count):
            """Traverse through trie rooted at node and build exact trie onto
            root. Set data of all TrieNodes under root to True or False
            using _eval_node along the way."""
            
            root.set_data(_eval_node(node, num_players, count))
            if node.children():
                for key in node.children():
                    root._children[key] = TrieNode() 
                    _insert_eval(root._children[key], node.children()[key], 
                                 num_players, count + 1)

        Trie.__init__(self)
        self._num_players = num_players
        _insert_eval(self._root, start_node, self._num_players, 0)
        
    def is_winning(self, node):
        """Return True if TrieNode 'node' is winning."""

        return node.data()
