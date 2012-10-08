from priorityqueue import PriorityQueue
from oval import Oval
from rectangle import Rectangle
from line import Line
import media

def convert_colour(colour_string):
    '''Convert the colour named in the input string into a Color object
    by looking up the entry for this colour in the media dictionary.'''
   
    return media.__dict__.get(colour_string)

class Collage(object):
    '''Store Shape objects in a PriorityQueue ready to be drawn and shown.'''
    
    def _info_to_shape(self, info):
        '''Return a Shape object initialized with attributes from the list
        info.'''
        
        new_shape = None
        if info[0] == 'oval':
            new_shape = Oval(int(info[1]), int(info[2]), int(info[3]), 
                         int(info[4]), convert_colour(info[5]), 
                         int(info[6]))
        elif info[0] == 'rectangle':
            new_shape = Rectangle(int(info[1]), int(info[2]), int(info[3]), 
                         int(info[4]), convert_colour(info[5]), 
                         int(info[6]))
        elif info[0] == 'line':
            new_shape = Line(int(info[1]), int(info[2]), int(info[3]), 
                         int(info[4]), convert_colour(info[5]), 
                         int(info[6]))
        
        return new_shape
    
    def _draw_collage(self, pqueue, picture):
        '''Draw objects dequeued from PriorityQueue pqueue onto picture.'''
        
        while pqueue.size() != 0:
            shape_to_draw = pqueue.dequeue()
            shape_to_draw.draw(picture)
    
    def __init__(self, filename):
        '''Initialize Collage object with information extracted from 
        file filename and stored in a PriorityQueue.'''
        
        data_file = open(filename, 'r')
        line = data_file.readline()
        info = line.strip().split(', ')
        self.pic = media.create_picture(int(info[0]), int(info[1]), 
                                        convert_colour(info[2]))
        self.queue = PriorityQueue()
        line = data_file.readline()
        while line.strip():
            info = line.strip().split(', ')
            # Determine Shape to add to PriorityQueue and enqueue it
            new_shape = self._info_to_shape(info)
            self.queue.enqueue(new_shape)
            line = data_file.readline()
        self._draw_collage(self.queue, self.pic)
    
    def get_picture(self):
        '''Return picture stored in the assembled Collage.'''
        
        return self.pic
    
    def show(self):
        '''Display Collage in a viewing window.'''
        
        media.show(self.pic)
