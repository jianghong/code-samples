from gametrie import GameTrie
from lextrie import LexTrie
import draw_trie

a = LexTrie()
a.insert('c','c data')
a.insert('b', 'b data')
a.insert('ea', 'da data')
a.insert('gae', 'ea, data')
print draw_trie.draw_trie(a)
b = GameTrie(a._root, 3)
print draw_trie.draw_trie(b)