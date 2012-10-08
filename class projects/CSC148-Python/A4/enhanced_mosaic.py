from PIL import Image
from os import listdir, path
from ImageChops import difference
from mosaic import *

class EnhancedMosaic(FractalMosaic):
    """An EnhancedMosaic is a modified and enhanced version of the 
    FractalMosaic class."""
        
    def _matching(self, pic, threshold, images):
            """Return an image from images if the pixel distance between image
            and pic is less than threshold.
            -pic is a picture
            -images is a list database of lists containing:
            [image, colour average of image]
            -threshold determines the lowest colour distance of two pictures
            to be considered 'matching'.
            """
            
            def _average_pixel_distance(pic1, pic2):
                """Return a list containing the average colour distance between
                pixels of pic1 and pic2, and pic1 resized to match pic2."""
            
                resized = pic1.resize(pic2.size)
                size = pic2.size[0] * pic2.size[1]
                pixel_difference = difference(resized, pic2).getdata()
                pixel_distance = sum([(((data[0] ** 2) + (data[1] ** 2) + 
                                        (data[2] ** 2)) ** 0.5) 
                                      for data in pixel_difference]) / size
                return [pixel_distance, resized]
            
            for i in xrange(len(images)):
                average = _average_pixel_distance(images[i][0], pic)
                if average[0] < threshold:
                    return average[1]
            return False
        
    def create_mosaic(self, filename, min_size, threshold):
        """Create and store a photomosaic version of a single image specified
        by filename. min_size determines the lowest height or width of 
        the image to start replacing with images in PICTURE_DATABASE.
        threshold determines the lowest colour distance of two images to be
        considered 'matching'."""
        
        def _create_mosaic(image, min_size, threshold, database):
            """Create and store a photomosaic version of image. min_size 
            determines the smallest height or width of the picture to start 
            replacing with pictures from database.threshold determines 
            the lowest colour distance of two images to be considered 
            'matching'."""
               
            size = image.size
            width, height = size[0], size[1]
            if width < min_size or height < min_size:
                best_match = self._closest_match(image, database)
                image.paste(best_match, (0, 0))
                return image
            match = self._matching(image, threshold, database)
            if match:
                image.paste(match, (0, 0))
            else:
                q1 = (0, 0, (width / 2), (height / 2))
                q2 = ((width / 2), 0, width, (height / 2))
                q3 = (0, (height / 2), (width / 2), height)
                q4 = ((width / 2), (height / 2), width, height)             
                image.paste(_create_mosaic(image.crop(q1), min_size, threshold,
                                            database), q1)
                image.paste(_create_mosaic(image.crop(q2), min_size, threshold,
                                           database), q2)
                image.paste(_create_mosaic(image.crop(q3), min_size, threshold,
                                           database), q3)
                image.paste(_create_mosaic(image.crop(q4), min_size, threshold,
                                           database), q4)
            return image
        
        pic = Image.open(filename)
        database = self._images_database(self.PICTURE_DATABASE)
        self.mosaic = _create_mosaic(pic, min_size, threshold, database)
        return self.mosaic
