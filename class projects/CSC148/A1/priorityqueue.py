from shape import Shape

class PriorityQueue(object):
    '''PriorityQueue stores a list of objects with priority values. priority 
    determines the order for dequeueing from the PriorityQueue.'''
    
    def _find_high_priority(self, pq_list):
        '''Return index of the object with the highest priority value.'''
        
        # Initialize highest_priority variable
        highest_priority = pq_list[0]
        # Save index of highest priority to j, i for index counting
        j = 0
        i = 0
        for item in pq_list:
            if item.get_priority() < highest_priority:
                highest_priority = item.get_priority()
                j = i
            i += 1
        return j
    
    def __init__(self, lst=None):
        '''Initialize a PriorityQueue with a list of objects. Default is an
        empty list.'''
        
        if lst == None:
            lst = []
        self.pq_list = lst
    
    def __str__(self):
        '''Return a string representation for each object in the PriorityQueue
        in an order determined by priority value.'''
        
        # Clone the internal list of the PriorityQueue to help determine
        # dequeue order
        clone = self.pq_list[:]  # clone is needed because pop is used
        final_string = ''
        while len(clone) != 0:
            index = self._find_high_priority(clone)
            final_string += clone[index].__str__() + ", priority = %s " \
                         % clone[index].get_priority() + "\n"
            clone.pop(index)
        return final_string.strip()
    
    def enqueue(self, item):
        '''Add an object to the PriorityQueue.'''
        
        self.pq_list.append(item)
        
    def dequeue(self):
        '''Remove and return an object with the highest priority from 
        the PriorityQueue'''
        
        index = self._find_high_priority(self.pq_list)
        return self.pq_list.pop(index)
    
    def size(self):
        '''Return the number of objects in the PriorityQueue.'''
        
        return len(self.pq_list)
