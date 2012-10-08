import media

def reduce_height(pic, factor):
    '''Replace these words with a suitable docstring for this function.'''
      
    # Create a new Picture with the appropriate new height and old width, and
    # initialize the colour to black (all colour components are zero).
    new_width = pic.get_width()
    new_height = (pic.get_height() + factor - 1) / factor
    newpic = media.create_picture(new_width, new_height, media.black)
    
    # Iterate through all the Pixels in the large image, and copy
    # a portion of that Pixel's colour components into the correct 
    # Pixel position in the smaller image.
    for pixel in pic:
        # Find the corresponding Pixel in the new Picture.
        x = media.get_x(pixel)
        y = media.get_y(pixel)
        newpixel = media.get_pixel(newpic, x, y/factor)
        
        # Add the appropriate fraction of this Pixel's colour components
        # to the components of the corresponding Pixel in the new Picture.
        new_red = newpixel.get_red() + pixel.get_red()/factor
        new_blue = newpixel.get_blue() + pixel.get_blue()/factor
        new_green = newpixel.get_green() + pixel.get_green()/factor
        media.set_red(newpixel, new_red)
        media.set_blue(newpixel, new_blue)
        media.set_green(newpixel, new_green)
        
    return newpic
    

if __name__ == "__main__":
    pic = media.load_picture(media.choose_file())
    
