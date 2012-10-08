import media
from shape import Shape

class Line(Shape):
    '''A Line shape inherited from Shape that stores information of
    the Line to be drawn onto a scene.'''
    
    def __init__(self, x=0, y=0, end_x=0, end_y=0, col=media.white, 
                 priority=0):
        '''Initialize Line with starting point at x,y(both default to 0)
        and ending point at end_x, end_y(both default to 0) with color col
        (default to white) and priority(default to 0).'''
        
        super(Line, self).__init__(x, y, col, priority)
        self.end_x = end_x
        self.end_y = end_y
    
    def __str__(self):
        '''Return a string representation of this Line by indicating it's
        starting x,y and ending x,y values.'''
        
        return "Line @ ( " + str(self.x) + " , " + str(self.y) + " ) to ( " + \
               str(self.end_x) + " , " + str(self.end_y) + " )"
    
    def draw(self, pic):
        '''Draw this Line on picture pic.'''
        
        media.add_line(pic, self.x, self.y, self.end_x, self.end_y, 
                       self.colour)
