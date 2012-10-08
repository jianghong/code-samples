from gametrie import GameTrie
from lextrie import LexTrie
import draw_trie

def lose_count(trie):
    """Return the number of losing nodes in a trie."""
    
    def _lose_count(node):
        """Helper"""
        
        count = 0
        if not node.data():
            count += 1
        if node.children():
            for node in node.children().values():
                count += _lose_count(node)
        return count
    return _lose_count(trie._root)
        
    
#a = LexTrie("short.txt")
#print len(a.find_all(''))
#b = GameTrie(a._root, 3)
#print lose_count(b)
c = LexTrie("medium.txt")
g = c.find_node('c')
d = GameTrie(g, 4)
print lose_count(d)
e = LexTrie("long.txt")
print len(e.find_all(""))
f = GameTrie(e.find_node('c'), 4)
print lose_count(f)