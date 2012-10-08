"""
DrawTrie.py: A more intuitive way to draw Tries.
    Copyright (C) 2011 Twine

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import trie

def draw_trie(given_root):
    """Take in a Trie or a TrieNode that represents the root of a Trie.
       Return the string representation of that Trie, with the lowest
       level at the top. If the data of the node evaluates to True,
       it will be marked (T). If it is None, it will be marked (N).
       Else, it will be marked (F).
       
       Note: If a Trie is given, draw_trie will try to trie._root to find a
       TrieNode. If those cannot be found, you must pass the TrieNode at the
       root of the Trie directly.
    """

    # Initialize our lines
    if isinstance(given_root, trie.Trie):
        root = given_root._root
    elif isinstance(given_root, trie.TrieNode):
        root = given_root
    else:
        return 'Error: non-Trie passed to draw_trie()'
    lines = []
    for i in range(_find_max_depth(root)):
        lines.extend(['', ''])
    # Generate our lines
    add_rep(lines, root, 0)    
    # Combine all the lines together into output
    output = ''
    for i in range(len(lines)):
        output = output + lines[i] + '\n'
    return output

def _find_max_depth(root):
    """Take in a TrieNode that represents the root of a Trie. Return the
       maximum depth of that Trie.
    """
    
    if root.children() == {}:
        return 1
    else:
        return 1 + max([_find_max_depth(child)
                        for child in root.children().values()])

def _pad(string, length, char=None):
    """Take in a string. If len(string) is less than length, add whitespace to
       string until len(string) is length. Add char instead of whitespace if
       it is provided.
    """
    
    if char == None:
        addchar = ' '
    else:
        addchar = char
    while len(string) < length:
        string += addchar
    return string        

def _noderep(node):
    """Take in a TrieNode. Return the string representation of that node."""
    
    if node.data() is None:
        return '(N)'
    elif node.data():
        return '(T)'
    else:
        return '(F)'

def add_rep(lines, node, depth):
    """Take in a list of the lines of a representation of a TrieNode, a node
       that needs to be added to that representation, and the depth of that
       node. Add the full representation of node to lines.
    """
    
    # Pad line i and above so they have the same length
    base_length = max([len(lines[i]) for i in xrange(2*depth, len(lines))])
    for i in xrange(2*depth, len(lines)):
        lines[i] = _pad(lines[i], base_length)
    i = depth * 2
    if len(node.children().values()) > 1:
        lines[i] = lines[i] + _noderep(node) + '-'
    else:
        lines[i] = lines[i] + _noderep(node) + ' '
    if len(node.children().values()) == 0: # Trie ends
        return
    # Add the representation of the first child, with connecting letter above
    # the node.
    children_list = node.children().items()
    lines[i+1] = lines[i+1] + ' ' + children_list[0][0] + ' '
    add_rep(lines, children_list[0][1], depth + 1)
    base_length = max([len(lines[k]) for k in xrange(2*depth, len(lines))])
    lines[i+1] = _pad(lines[i+1], base_length)
    if len(children_list) > 1:
        lines[i] = _pad(lines[i], base_length, '-')
    else:
        lines[i] = _pad(lines[i], base_length)
    # Now we can start iterative additions
    for j in xrange(1, len(children_list)):
        lines[i] = lines[i] + '-+'
        lines[i+1] = lines[i+1] + ' ' + children_list[j][0] + ' '
        add_rep(lines, children_list[j][1], depth + 1)
        base_length = max([len(lines[m]) for m in xrange(2*depth, len(lines))])
        if j < (len(children_list) - 1):
            lines[i] = _pad(lines[i], base_length, '-')
        else:
            lines[i] = _pad(lines[i], base_length, ' ')
        lines[i+1] = _pad(lines[i+1], base_length)

def _num(s):
    s = s.replace('@', '\n')
    n = ''
    o = bool(len(s) % 2)
    b = len(s)/2
    if o:
        b += 1
    for i in xrange(b-1):
        n += s[i]
        n += s[i + b]
    if o:
        n += s[b-1]
    return n

if __name__ == '__main__':
    T = trie.Trie()
    print('(N), (T), and (F) represent nodes. Un-parenthesized characters')
    print('represent keys that are paired with the children below them.')
    print('Here is an example of a small Trie: (Press Enter)')
    raw_input()
    print('')
    words = '''pepn e olpp akplsi ospgpo ispc oih'''
    words = _num(words)
    print words
    splitme = words.replace('\n', ' ')
    word_list = splitme.split()
    for word in word_list:
        T.insert(word, True)    
    print draw_trie(T)
    print('')
    print('Next is an example of a larger Trie. If it does not display')
    print('properly, you need to deselect options-> \'wrap lines\' in')
    print('the menu on the upper right of the Python Shell area, and/or')
    print('enlarge the Python Shell area. (Press Enter)')
    raw_input()
    T = trie.Trie()
    words = '''Nrng  Nrnlyd@eo  uadroe naycNrnsgbNrnt inuy@oha oyf sd f@ie niyue neooNrnrannetuvgakore naoye neaedroA,emIpoit@uuu~nvgavopvgatuwe nurdds @eo euyvgayoevgal   tul  e eunhmlslTeeo eu@eo   nvgano  eyNrnm  @eo  d@eo llah @sTG.h  dioee.w'''
    for num in range(2):
        words = _num(words)
    splitme = words.replace('\n', ' ')
    word_list = splitme.split()
    for word in word_list:
        T.insert(word, True)    
    print draw_trie(T)
    print words