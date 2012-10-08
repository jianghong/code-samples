from lextrie import LexTrie
import cProfile as Profile
from gametrie import GameTrie
    
def compare_with_diagrams():
      def build_simple_trie(lexicon, num_players):
	    lt = LexTrie()
	    for k,d in lexicon.iteritems():
		  lt.insert(k, d)
	    gt = GameTrie(lt._root, num_players)
	    return (lt, gt)

      # Compare with diagram:
      scores = {
	    'b': True,
	    'ba': True,
	    'bar': False,
	    'bari': True,
	    'baris': True,
	    'barist': True,
	    'barista': True,
	    'baristas': True,
	    'ban': True,
	    'bann': True,
	    'banne': True,
	    'banner': True,
	    'bank': True,
	    'bag': False,
	    'c': False,
	    'co': False,
	    'coo': False,
	    'cool': True,
	    'coole': True,
	    'cooler': True,
	    'cook': True,
	    }
      
      scores2 = {
	    'b': True,
	    'ba': True,
	    'bar': True,
	    'bari': True,
	    'baris': True,
	    'barist': True,
	    'barista': True,
	    'baristas': True,
	    'ban': True,
	    'bann': True,
	    'banne': True,
	    'banner': True,
	    'bank': False,
	    'bag': True,
	    'c': True,
	    'co': True,
	    'coo': True,
	    'cool': False,
	    'coole': True,
	    'cooler': True,
	    'cook': False,
	    }

      lex = {
	    "cool":"Cool's Data",
	    "coo":"Coo's Data",
	    "bar":"Bar's Data",
	    "cooler":"Cooler's Data",
	    "baristas":"Baristas's Data",
	    "cook":"Cook's Data",
	    "banner":"Banner's Data",
	    "bag":"Bag's Data",
	    "bank":"Bank's Data"}
      
      t = {2:scores,3:scores2}
      for players in [2,3]:
	    print "Evaluating the diagram with %s players" %(players)
	    #Profile.run("build_simple_trie(lex, players)")
	    lt,gt = build_simple_trie(lex, players)
	    mistakes = []
	    for i in t[players]:
		  if not gt.find_node(i).data() == t[players][i]:
			mistakes.append((i, t[num_play][i], gametrie.find_node(i).data()))
	    if not mistakes:
		  print "TRIES MATCH DIAGRAMS"
	    else:
		  for mis in mistakes:
			print "MISMATCH:For %s expected %s but found %s" %(mis)
compare_with_diagrams()