from PIL import Image
from os import listdir, path

class Mosaic(object):
    """A Mosaic class that can create, store and save a photomosaic image."""
    
    def __init__(self, path):
        """Create a picture database that stores all images from directory 
        specified by path."""
                
        self.PICTURE_DATABASE = listdir(path)
        self.path = path
        self.mosaic = None
        
    def _images_database(self, dirlist):
            """Return a list of lists with images from dirlist 
            as the first element in nested lists and their average colour value 
            as the second element. i.e. 
            [[image.jpg, _colour_average], [image2, _colour_average]]
            -dirlist is a list of filenames for images."""
            
            outer = []
            for i in xrange(len(dirlist)):
                inner = []
                image = Image.open(path.join(self.path, dirlist[i]))
                inner.append(image)
                inner.append(_colour_average(image))
                outer.append(inner)
            return outer
        
    def _closest_match(self, pic, images):
            """Return an image from database, with closest average colour value
            to pic's average colour value, resized to match pic.
            -pic is a picture
            -images is a list database of lists containing
            [image, colour average of image]
            """
            
            pic_col = _colour_average(pic)
            # Store the image with the smallest _distance from pic in a list 
            # to resize
            closest = min([[_distance(pic_col, image[1]), image[0]]
                            for image in images])
            resized = closest[1].resize(pic.size)
            return resized
        
    def create_mosaic(self, filename, min_size):
        """Create and store a photomosaic version of a single picture specified
        by filename. min_size determines the smallest height or width of 
        the picture to start replacing with pictures in PICTURE_DATABASE."""
    
        def _create_mosaic(image, min_size, database):
            """Create and store a photomosaic version of image. min_size 
            determines the smallest height or width of the picture to start 
            replacing with pictures from database."""
               
            size = image.size
            width, height = size[0], size[1]
            if width < min_size or height < min_size:
                # Find an image from database with smallest distance
                best_match = self._closest_match(image, database)
                return best_match
            else:
                # Recurse on four different quadrants
                q1 = (0, 0, (width / 2), (height / 2))
                q2 = ((width / 2), 0, width, (height / 2))
                q3 = (0, (height / 2), (width / 2), height)
                q4 = ((width / 2), (height / 2), width, height)             
                image.paste(_create_mosaic(image.crop(q1), min_size, 
                                            database), q1)
                image.paste(_create_mosaic(image.crop(q2), min_size,
                                           database), q2)
                image.paste(_create_mosaic(image.crop(q3), min_size,
                                           database), q3)
                image.paste(_create_mosaic(image.crop(q4), min_size,
                                           database), q4)
            return image
                
        pic = Image.open(filename)
        database = self._images_database(self.PICTURE_DATABASE)
        self.mosaic = _create_mosaic(pic, min_size, database)
        return self.mosaic

    def save_as(self, filename):
        """Save the stored photomosaic as a jpg file named filename."""
        
        if self.mosaic:
            self.mosaic.save(filename, 'JPEG')

#====START: Helper Functions for importing============================
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
    distance = (((red1 - red2) ** 2) + ((blue1 - blue2) ** 2) + \
             ((green1 - green2) ** 2)) ** 0.5
    return distance
#====END========================================================
