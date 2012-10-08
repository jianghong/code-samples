'''A Stack ADT implemented with a List.'''

class Stack(object):
    '''A Stack ADT
    
    This ADT supports the following operations:
    
    - push(item): add an item to the top of the Stack
    - pop(): remove and return an item from the top of the Stack
    - size(): return the size of the stack
    
    '''

    def __init__(self):
        '''Create an empty Stack.'''

        self.stack_list = []
        self.size = 0

    def __str__(self):
        '''Return a string representation of this Stack.'''
        
        return_string = ""
        for item in self.stack_list:
            return_string = str(item) + "\n" + return_string
        return return_string[:-1]
        
    def size(self):
        '''Return this number of items in this Stack.'''

        return self.size

    def is_empty(self):
        '''Return TRUE if the stack is empty.'''
        
        return self.size == 0
    
    def pop(self):
        '''Remove and return the top element of this Stack.'''

        self.size -= 1
        return self.stack_list.pop(self.size)
    
    def push(self, item):
        '''Add the given item on top of this Stack.'''

        self.size += 1
        self.stack_list.append(item)
    
        
        