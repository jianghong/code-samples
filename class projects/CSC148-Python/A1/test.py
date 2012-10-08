import media
from shape import Shape
from oval import Oval
from rectangle import Rectangle
from line import Line
from priorityqueue import PriorityQueue
from collage import Collage


e = PriorityQueue()    
d = Oval(30, 30, 30, 20, media.red, 0)
e.enqueue(d)
g = Rectangle(0, 0, 20, 20, media.blue,0)
e.enqueue(g)
h = Line(115, 85, 125, 85, media.black, 0)
e.enqueue(h)
print e
a = Collage('data.txt')
b = Collage('test2.txt')
 
c = PriorityQueue()

m = PriorityQueue()
m.enqueue(d)
m.enqueue(Rectangle(1,1,1,1,'white',2))
m.enqueue(h)
