import media
from shape import Shape

class Oval(Shape):
    '''An Oval shape inherited from Shape that stores information of
    the Oval to be drawn onto a scene. x, y value is the center
    of the Oval.'''
    
    def __init__(self, x=0, y=0, width=0, height=0, col=media.white, 
                 priority=0):
        '''Initialize an Oval with position centered at x, y
        (x and y are positive integers and default to 0 if not specified), 
        width,height(default value 0), colour(default white) 
        and priority(default 0).'''
        
        super(Oval, self).__init__(x, y, col, priority)
        self.width = width
        self.height = height
        
    def __str__(self):
        '''Return the string representation of this Oval by indicating its 
        center coordinates, height and width.'''
        
        return "Oval @ ( " + str(self.x) + " , " + str(self.y) + \
               " ) height = " + str(self.height) + ", width = " + \
               str(self.width)
        
    def draw(self, pic):
        '''Draw this Oval on picture pic.'''
        
        # Determine the top left corner of Oval to start drawing from
        drawing_x = self.x - (self.width / 2)
        drawing_y = self.y - (self.height / 2)

        media.add_oval_filled(pic, drawing_x, drawing_y, self.width, 
                              self.height, self.colour)
