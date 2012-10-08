import media

def red_average(pic):
    '''Returns the average red value of the entire Picture pic as an int.'''

    sum_red = 0
    height = media.get_height(pic)
    width = media.get_width(pic)
    total_pixel = height * width
    
    for pixel in pic:
        red = media.get_red(pixel)
        sum_red += red
    
    average = sum_red / total_pixel
    return int(average)

def scale_red(pic, int):
    
    for pixel in pic:
        media.set_red(pixel, int)

if __name__ == "__main__":
    pic = media.load_picture(media.choose_file())
    pic2 = media.load_picture(media.choose_file())