""" 

Test cases for trie.py, lextrie.py, gametrie.py
Release v1.2 on March 14, 2011
Made by Kevin Ha Dial (c0dialke)

These are just very simple test cases and will not guarantee your program is perfect.
Please continue testing your program afterwards.

Note: 
Use comments or docstrings if the program crashes (I was too lazy to make a legit test file).
Some of my test cases are based on the object's string output and not the actual object.

"""

from trienode import TrieNode
from trie import *
from lextrie import * 
from gametrie import *
import draw_trie

print "\nTest cases for assignemtn 3 (v1.0) by Kevin Ha Dial"
print "\n__________start testing Trie__________\n"
t = Trie()
t.insert('dog', 'single-dog')
t.insert('dogs', 'pluarl-dogs')
t.insert('test', 'test')
t.insert('tent', 'tent')

# Test insert by printing the trie
print 'testing inserting nodes--------', str(t) == "None {d: None {o: None {g: single-dog {s: pluarl-dogs {}}}}, t: None {e: None {s: None {t: test {}}, n: None {t: tent {}}}}}"


# Test find_node by searching for nodes.
dog_n = t.find_node("dog")
tent_n = t.find_node("tent")
te_n = t.find_node("te")
zz_n = t.find_node("zz")
blank_n = t.find_node("")

print 'testing find dog node--------', str(dog_n) == 'single-dog'
print 'testing find tent node--------', str(tent_n) == "tent"
print 'testing find te node--------', str(te_n) == "None"
print 'testing find zz node--------', str(zz_n) == "None"
print 'testing find blank node (should be the root)--------', blank_n == t._root


print "\n__________start testing LexTrie__________\n"

# Test find_all in lextrie
words_def = []
words_def.append(('dog', 'single-dog'))
words_def.append(('dogs', 'pluarl-dogs'))
words_def.append(('test', 'test'))
words_def.append(('tent', 'tent'))

lex = LexTrie(words_def)

prefix_words1 = lex.find_all('do')
prefix_words2 = lex.find_all('t')
prefix_words3 = lex.find_all('')
prefix_words4 = lex.find_all('zz')

print 'testing find_all "do" ', sorted(prefix_words1) == ['dog', 'dogs']
print 'testing find_all "t" ', sorted(prefix_words2) == ['tent', 'test']
print 'testing find_all "" ', sorted(prefix_words3) == ['dog', 'dogs', 'tent', 'test']
print 'testing find_all "zz" ', sorted(prefix_words4) == []


print "\n__________start testing GameTrie__________\n"

ll = []
ll.append(('coo', 'coo'))
ll.append(('bar', 'bar'))
ll.append(('cooler', 'cooler'))
ll.append(('baristas', 'baristas'))
ll.append(('cool', 'cool'))
ll.append(('cook', 'cook'))
ll.append(('bank', 'bank'))
ll.append(('banner', 'banner'))
ll.append(('bag', 'bag'))
llex = LexTrie(ll)

gg2 = GameTrie(llex._root, 2)
print draw_trie.draw_trie(gg2)
output2 = 'True {c: False {o: False {o: False {k: True {}, l: True {e: True {r: True {}}}}}}, b: True {a: True {r: False {i: True {s: True {t: True {a: True {s: True {}}}}}}, g: False {}, n: True {k: True {}, n: True {e: True {r: True {}}}}}}}'

gg3 = GameTrie(llex._root, 3)
print draw_trie.draw_trie(gg3)
output3 = 'True {c: True {o: True {o: True {k: False {}, l: False {e: True {r: True {}}}}}}, b: True {a: True {r: True {i: True {s: True {t: True {a: True {s: True {}}}}}}, g: True {}, n: True {k: False {}, n: True {e: True {r: True {}}}}}}}'

print 'testing 2 player game--------', str(gg2) == output2
print 'testing 3 player game--------', str(gg3) == output3
