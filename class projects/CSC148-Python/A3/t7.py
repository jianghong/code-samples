from lextrie import LexTrie
import cProfile as Profile
from gametrie import GameTrie

def xiangs_stats():
      def test_count_nodes(start_node):
	    lst = []
	    _test_find_nodes(start_node, lst)
	    return sum(1 for i in lst if not i)

      def _test_find_nodes(start_node, lst):
	    lst.append(start_node.data())
	    for c in start_node.children():
		  _test_find_nodes(start_node.children()[c], lst)
		
      def assess(path, p, prefix):
	    new_lextrie = LexTrie(path)
	    total = len(open(path).readlines())
	    inserted = len(new_lextrie.find_all(''))
	    print "Inserted %s of %s total found in file" %(inserted, total)
	    my_gametrie = GameTrie(new_lextrie.find_node(prefix), p)	  
	    print "total losing nodes: %s for gametrie with prefix %s and %s players" %(
		test_count_nodes(my_gametrie._root), prefix, p)
	    
      assess('short.txt',3,'')
      assess('medium.txt',4,'c')
      assess('long.txt',4,'c')
    
xiangs_stats()
