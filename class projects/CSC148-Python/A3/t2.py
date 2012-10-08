from lextrie import LexTrie
import draw_trie

a = LexTrie()
a.insert('cool', 'cools data')
a.insert('coo', 'coos data')
a.insert('cook', 'cooks data')
a.insert('bang', 'bangs data')
a.insert('mega', 'megas data')
print draw_trie.draw_trie(a)
print a.find_all('')