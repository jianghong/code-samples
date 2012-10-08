import media

def red_average(pic):
    '''Return the average red value of the entire Picture pic as an int.'''

    # Find the total amount of pixels in the picture.
    sum_red = 0
    height = media.get_height(pic)
    width = media.get_width(pic)
    total_pixel = height * width
    
    # Go through every pixel to obtain the red value and add it to the \
    # sum.
    for pixel in pic:
        red = media.get_red(pixel)
        sum_red += red
    
    # Calculate the average red of entire picture
    average = sum_red / total_pixel
    return int(average)

def green_average(pic):
    '''Return the average green value of the entire Picture pic as an int.'''
    
    sum_green = 0
    height = media.get_height(pic)
    width = media.get_width(pic)
    total_pixel = height * width
    
    for pixel in pic:
        green = media.get_green(pixel)
        sum_green += green
    
    average = sum_green / total_pixel
    return int(average)
    
def blue_average(pic):
    '''Return the average blue value of the entire Picture pic as an int.'''
    
    sum_blue = 0
    height = media.get_height(pic)
    width = media.get_width(pic)
    total_pixel = height * width
    
    for pixel in pic:
        blue = media.get_blue(pixel)
        sum_blue += blue
    
    average = sum_blue / total_pixel
    return int(average)

def scale_red(pic, new_red):
    '''Set the average red of a Picture pic to a new average new_red'''
    
    #Find the average red of a picture using red_average.
    #Use the given general formula to determine pixel_ratio.
    average_red = red_average(pic)
    pixel_ratio = float(new_red)/ average_red
    
    #Find the new red value using pixel_ratio.
    #Go through every pixel and set the current red value to the new red value.
    #If the new red value exceeds 255, set it to 255.
    for pixel in pic:
        red = media.get_red(pixel)
        target_red = pixel_ratio * red
        if target_red > 255.0:
            target_red = 255
        change_red = media.set_red(pixel, int(target_red))

def scale_blue(pic, new_blue):
    '''Set the average blue of a Picture pic to a new average new_blue'''
    
    average_blue = blue_average(pic)
    pixel_ratio = float(new_blue) / average_blue
    
    for pixel in pic:
        blue = media.get_blue(pixel)
        target_blue = pixel_ratio * blue
        if target_blue > 255.0:
            target_blue = 255
        change_blue = media.set_blue(pixel, int(target_blue))

def scale_green(pic, new_green):
    '''Set the average green of a Picture pic to a new average new_green'''
    
    average_green = green_average(pic)
    pixel_ratio = float(new_green) / average_green
    
    for pixel in pic:
        green = media.get_green(pixel)
        target_green = pixel_ratio * green
        if target_green > 255.0:
            target_green = 255
        change_green = media.set_green(pixel, int(target_green))

        
def expand_height(pic, expand_factor):
    '''Create a new picture new_pic that has an expanded height of pic by a \
    factor of expand_factor.'''

    #Create a new picture with an expanded height of expand_factor.
    #Set the new picture's intitial RGB values to 0.
    height = expand_factor * media.get_height(pic)
    width = media.get_width(pic)
    new_pic = media.create_picture(width, height, media.black) 
    
    #Iternate through all pixels in new_pic and take the color components \
    # from pic and copy them onto new_pic
    for pixel in new_pic:
        # Obtain the x and y coordinates in new_pic
        x = media.get_x(pixel)
        y = media.get_y(pixel)
        
        # Use x, y to get the location and color components of pic
        # Add and set the pixels in new_pic to the colors in pic
        new_pixel = media.get_pixel(pic, x, y / expand_factor)
        new_red = new_pixel.get_red() + pixel.get_red() 
        new_blue = new_pixel.get_blue() + pixel.get_blue() 
        new_green = new_pixel.get_green() + pixel.get_green() 
        media.set_red(pixel, new_red)
        media.set_blue(pixel, new_blue)
        media.set_green(pixel, new_green) 
    
    return new_pic
    
def expand_width(pic, expand_factor):
    '''Create a new picture new_pic that has an expanded width of pic by a \
     factor of expand_factor.'''
     
    height = media.get_height(pic)
    width = expand_factor * media.get_width(pic)
    new_pic = media.create_picture(width, height, media.black) 
    
    for pixel in new_pic:
        x = media.get_x(pixel)
        y = media.get_y(pixel)
        new_pixel = media.get_pixel(pic, x / expand_factor, y )
        new_red = new_pixel.get_red() + pixel.get_red() 
        new_blue = new_pixel.get_blue() + pixel.get_blue() 
        new_green = new_pixel.get_green() + pixel.get_green() 
        media.set_red(pixel, new_red)
        media.set_blue(pixel, new_blue)
        media.set_green(pixel, new_green)
        
    return new_pic


def reduce_height(pic, factor):
    '''Create a new picture newpic that has a reduced height of pic by a \
    factor of factor.'''
      
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

def reduce_width(pic, factor):
    '''Create a new picture newpic that has a reduced width of pic by a \
    factor of factor.'''
      
    new_height = pic.get_height()
    new_width = (pic.get_width() + factor - 1) / factor
    newpic = media.create_picture(new_width, new_height, media.black)
    
    for pixel in pic:
        x = media.get_x(pixel)
        y = media.get_y(pixel)
        newpixel = media.get_pixel(newpic, x/factor, y)
        new_red = newpixel.get_red() + pixel.get_red()/factor
        new_blue = newpixel.get_blue() + pixel.get_blue()/factor
        new_green = newpixel.get_green() + pixel.get_green()/factor
        media.set_red(newpixel, new_red)
        media.set_blue(newpixel, new_blue)
        media.set_green(newpixel, new_green)
        
    return newpic
    
def distance(pixel, pixel2):
    '''Return an int that is the distance between the RGB vaules of pixel \
    and pixel2.'''
    
    # Obtain the RGB values of pixel and pixel2.
    red = pixel.get_red()
    blue = pixel.get_blue()
    green = pixel.get_green()
    red2 = pixel2.get_red()
    blue2 = pixel2.get_blue()
    green2 = pixel2.get_green()
    
    # Calcultae the sum of the absolute values of the differences of the \
    # RGB values.
    distance = abs(red - red2) + abs(blue - blue2) + abs(green - green2)
    
    return distance

def simple_difference(pic, pic2):
    '''Return an int that is the sum of the differences between each pixel in \
    pic and pic2.'''
    
    sum_difference = 0
    
    # Use distance function to calculate the total sum of all pixels between \
    # pic and pic2.
    for pixel in pic:
        x_pic = media.get_x(pixel)
        y_pic = media.get_y(pixel)
        pixel2 = media.get_pixel(pic2, x_pic, y_pic)
        difference = distance(pixel, pixel2)
        sum_difference += difference
        
    return sum_difference

def smart_difference(pic, pic2):
    '''Return the simple_difference of two pictures after setting the
    dimensions of the pictures equal and scaling their averages to be 
    the same.'''
    
    # Obtain the dimensions of both pictures.
    height = media.get_height(pic)
    width = media.get_width(pic)
    height2 = media.get_height(pic2)
    width2 = media.get_width(pic2)
    
    # Go through the four cases of comparison.
    # Reduce height and width of pic to match pic2.
    if height >= height2 and width >= width2:
        factor_h = height / height2
        factor_w = width / width2
        picnew = reduce_height(pic, factor_h)
        pic1new = reduce_width(picnew, factor_w)
        pic2new = pic2
    
    # Reduce height of pic2 to patch pic and width of pic to match pic2.
    elif height <= height2 and width >= width2:
        factor_h = height2 / height
        factor_w = width / width2
        pic1new = reduce_height(pic2, factor_h)
        pic2new = reduce_width(pic, factor_w)
    
    # Reduce height of pic to match pic2  and width of pic2 to match pic.
    elif height >= height2 and width <= width2:
        factor_h = height / height2
        factor_w = width2 / width
        pic1new = reduce_height(pic, factor_h)
        pic2new = reduce_width(pic2, factor_w)
        
    # Reduce height and width of pic2 to match pic.
    elif height <= height2 and width <= width2:
        factor_h = height2 / height
        factor_w = width2 / width
        picnew = reduce_height(pic2, factor_h)
        pic2new = reduce_width(picnew, factor_w)
        pic1new = pic
        
    # Scale the RGB values of pic2new to those of pic1new
    red = red_average(pic1new)
    blue = blue_average(pic1new)
    green = green_average(pic1new)
    scale_red(pic2new, red)
    scale_blue(pic2new, blue)
    scale_green(pic2new, green)
    
    # Use simple_difference to calculate and return an int.
    simple_d = simple_difference(pic1new, pic2new)
    return simple_d

if __name__ == "__main__":
    pic = media.load_picture(media.choose_file())
    pic2 = media.load_picture(media.choose_file())
    

    