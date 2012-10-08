import media
import Image
from mosaic import Mosaic
from os import path, listdir
from math import sqrt, pow
from ImageChops import difference
from fractal_mosaic import FractalMosaic

#a = media.create_picture(5,5, media.Color(1, 5, 0))
#a.save_as('c.bmp')
#b = Image.open('c.bmp')
#for i in list(b.histogram())[256:512]:
    #print i

        
def _colour_average(image):
    """Return a tuple that contains the average RGB value of image."""
    
    histo = image.histogram()
    average_red, average_green, average_blue = 0, 0, 0
    size = image.size[0] * image.size[1]
    for i in xrange(256):
        average_red += (i * histo[:256][i])
        average_green += (i * histo[256:512][i])
        average_blue += (i * histo[512:][i])
    return (average_red / size, average_green / size, 
            average_blue / size)

def _distance(col1, col2):
    """Return the euclidean of col1 and col2. col1 and col2 are both
    tuples representing RGB colour values."""
    
    red1, blue1, green1 = col1[0], col1[1], col1[2]
    red2, blue2, green2 = col2[0], col2[1], col2[2]
    distance = sqrt(pow((red1 - red2), 2) + pow((blue1 - blue2), 2) + 
                    pow((green1 - green2), 2)) 
    return distance

def _average_pixel_distance(pic1, pic2):
    """Return a tuple containing the average colour distance between
    pixels of pic1 and pic2, and pic1 resized to match pic2."""

    resized = pic1.resize(pic2.size)
    size = pic2.size[0] * pic2.size[1]
    pixel_difference = difference(pic1, pic2).getdata()
    pixel_distance = sum([(((data[0] ** 2) + (data[1] ** 2) + 
                            (data[2] ** 2)) ** 0.5) 
                          for data in pixel_difference]) / size
    return (pixel_distance, resized)

def _matching(pic, threshold, images):
    """Return an image from images if the pixel distance between image
    and pic is less than threshold.
    -pic is a picture
    -images is a dictionary database of image:colour average of image
    -threshold determines the lowest colour distance of two pictures
    to be considered 'matching'.
    """
    
    result = min([_average_pixel_distance(im, pic) for im in images])
    if result[0] < threshold:
        return result[1]
    return False

class tMosaic(object):
    
    def __init__(self, path):
        """Create a picture database that stores all images from directory 
        specified by path."""
        
        self.PICTURE_DATABASE = listdir(path)
        self.path = path
        self.mosaic = None
        
    def _closest_match(self, pic, images):
        """Return an image from images, with closest average colour value
        to pic's average colour value, resized to match pic.
        -pic is a picture
        -images is a list of strings that are filenames of pictures
        """
        
        pic_col = _colour_average(pic)
        closest = (256, None)
        for im in images:
            image = Image.open(path.join(self.path, im))
            distance = _distance(pic_col, _colour_average(image))
            if distance < closest[0]:
                closest = (distance, image)
        resized = closest[1].resize(pic.size)
        return resized
    
    def _images_database(self, dirlist):
            """Return a list of lists length 2 with images from dirlist 
            as the first element in nested lists and their average colour value 
            as the second element. i.e. 
            [[image.jpg, _colour_average], [image2, _colour_average] ]
            -dirlist is a list of filenames for images."""
            
            outer = []
            for im in dirlist:
                inner = []
                image = Image.open(path.join(self.path, im))
                inner.append(image)
                inner.append(_colour_average(image))
                outer.append(inner)
            return outer

d = FractalMosaic("C:\Z\CSC148\A4\dali")
d.create_mosaic('karan.jpg', 20, 60)
d.save_as("fun.jpg")
a = Image.open('karan.jpg')
b = Image.open('46_dali.tif')
#k = Mosaic("C:\Z\CSC148\A4\dali")
#k.create_mosaic('lol.jpg', 5)
#k.save_as("test_fun.jpg")
#l = os.listdir("C:\Z\CSC148\A4\dali")
#a = Image.open('karan.jpg')
#i = tMosaic("C:\Z\CSC148\A4\dali")
#size = a.size
#b = a.crop((0,0, size[0]/2, size[1]/2))
#c = b.crop((0,0, b.size[0]/2, b.size[1]/2))
#d = c.crop((0,0, c.size[0]/2, c.size[1]/2))
#e = d.crop((0,0, d.size[0]/2, d.size[1]/2))
#f = e.crop((0,0, e.size[0]/2, e.size[1]/2))
#a.paste(b)