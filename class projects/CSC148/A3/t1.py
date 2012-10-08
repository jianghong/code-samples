from trie import Trie
import draw_trie

a = Trie()
a.insert('c', 'cools data')
a.insert('co', 'cools2 data')
a.insert('coo', 'coos data')
a.insert('cool', 'coos2 data')
a.insert('cook','cooks data')
a.insert('bank', 'banks data')
a.insert('bang', 'bangs data')
print draw_trie.draw_trie(a)
print a.data('cool')
print a.data('coo')
b = Trie()
b.data('c')
