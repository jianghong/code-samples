from gametrie import GameTrie
from lextrie import LexTrie
import draw_trie

a = LexTrie()
a.insert('coo', 'coos data')
a.insert('cool', 'cools data')
a.insert('cooler', 'coolers data')
a.insert('cook', 'cooks data')
a.insert('bag', 'bags data')
a.insert('bank', 'banks data')
a.insert('banner', 'banners data')
a.insert('baristas', 'baristas data')
a.insert('bar', 'bars data')
print draw_trie.draw_trie(a)

b = GameTrie(a._root, 3)

print draw_trie.draw_trie(b)