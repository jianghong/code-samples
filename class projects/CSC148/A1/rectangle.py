import media
from shape import Shape

class Rectangle(Shape):
    '''A Rectangle shape inherited from Shape that stores information of
    the Rectangle to be drawn onto a scene. x, y value will be the
    top left corner of the rectangle.'''
    
    def __init__(self, x=0, y=0, width=0, height=0, col=media.white, 
                 priority=0):
        '''Initialize a Rectangle with top left corner of rectangle
        at x, y(x and y are positive integers and default to 0 if not 
        specified) width,height(default value 0), colour(default white) and 
        priority(default 0).'''
        
        super(Rectangle, self).__init__(x, y, col, priority)
        self.width = width
        self.height = height
        
    def __str__(self):
        '''Return the string representation of this Rectangle by indicating its 
        top left corner coordinates, height and width.'''
        
        return "Rectangle @ ( " + str(self.x) + " , " + str(self.y) + \
               " ) height = " + str(self.height) + ", width = " + \
               str(self.width)
    
    def draw(self, pic):
        '''Draw this Rectangle on picture pic.'''
        
        media.add_rect_filled(pic, self.x, self.y, self.width, self.height,
                              self.colour)
