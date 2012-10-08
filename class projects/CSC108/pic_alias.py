import media

def distance(pixel, pixel2):
    red = pixel.get_red()
    blue = pixel.get_blue()
    green = pixel.get_green()
    red2 = pixel2.get_red()
    blue2 = pixel2.get_blue()
    green2 = pixel2.get_green()
    
    distance = abs(red - red2) + abs(blue - blue2) + abs(green - green2)
    return distance

def simple_difference(pic, pic2):
    for pixel in pic:
        x_pic = media.get_x(pixel)
        y_pic = media.get_y(pixel)
        pixel2 = media.get_pixel(pic2, x_pic, y_pic)
        difference = distance(pixel, pixel2)
        
    return difference
   

if __name__ == "__main__":
    pic = media.load_picture(media.choose_file())
    pic2 = media.load_picture(media.choose_file())