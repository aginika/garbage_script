#!/usr/bin/env python
from PIL import Image, ImageDraw
import sys
import numpy as np

class ImageScratcher(object):
    options=[]
    input_filename=""
    output_filename=""
    iamge=None
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.image = Image.open(self.input_filename)

    def damage(self):
        self.image.save(self.output_filename)

    def setOption(self, options):
        self.options = options

    def selectColor(self, mode, type):        
        #black
        if (type == 1):
            if mode == "RGB":
                return (0,0,0)
            elif mode == "RGBA":
                return (0,0,0,255)
            else:
                return 0
        #white
        elif (type == 2):
            if mode == "RGB":
                return (255, 255, 255)
            elif mode == "RGBA":
                return (255, 255, 255, 255)
            else:
                return 255
        #random
        elif (type == 3):
            if mode == "RGB":
                return (np.random.randint(256),
                        np.random.randint(256),
                        np.random.randint(256))
            elif mode == "RGBA":
                return (np.random.randint(256),
                        np.random.randint(256),
                        np.random.randint(256),
                        255)
            else:
                return np.random.randint(256)
        #extract color from picture
        elif (type == 4):
            x = np.random.randint(self.image.size[0])
            y = np.random.randint(self.image.size[1])
            return self.image.getpixel((x,y))

#Options
#[0] min_length
#[1] max_length
#[2] color_type(1: black 2: white 3: random 4: extract from picture)
#[3] min_time
#[4] max_time
#[5] min_width
#[6] max_width

class LineImageScratcher(ImageScratcher):
    def damage(self):
        min_size = 0
        max_size = self.image.size[1]
        min_draw_num = 1
        max_draw_num = 3
        color_type = 3
        min_width = 1
        max_width = 10
        print self.options
        if( len(self.options) == 7):
            min_size = int(self.options[0])
            max_size = int(self.options[1])
            color_type = int(self.options[2])
            min_draw_num = int(self.options[3])
            max_draw_num = int(self.options[4])
            min_width = int(self.options[5])
            max_width = int(self.options[6])
            print "options", self.options
        size = max_size - min_size
        width = np.random.randint(min_width, max_width+1)

        times = np.random.randint(min_draw_num, max_draw_num + 1)
        imageDraw = ImageDraw.Draw(self.image)
        for i in range(times):
            color = self.selectColor(self.image.mode, color_type)
            x1 = np.random.randint(self.image.size[0])
            y1 = np.random.randint(self.image.size[1])
            x_size = np.random.randint(min_size, max_size+1) * np.random.choice([-1, 1])
            y_size = np.random.randint(min_size, max_size+1) * np.random.choice([-1, 1])
            imageDraw.line((x1,
                            y1,
                            x1+x_size,
                            y1+y_size),fill=color, width=width)
        super(LineImageScratcher, self).damage()


#Options
#[0] min_size
#[1] max_size
#[2] min_num
#[3] max_num
#[4] color_type(1: black 2: white 3: random 4: extract from picture)
class SquareImageScratcher(ImageScratcher):
    def damage(self):
        min_size = 1
        max_size = self.image.size[1]/2
        min_draw_num = 1
        max_draw_num = 3
        color_type = 3
        if( len(self.options) == 5):
            min_size = int(self.options[0])
            max_size = int(self.options[1])
            min_draw_num = int(self.options[2])
            max_draw_num = int(self.options[3])
            color_type = int(self.options[4])

        times = np.random.randint(min_draw_num, max_draw_num + 1)
        imageDraw = ImageDraw.Draw(self.image)
        for i in range(times):
            color = self.selectColor(self.image.mode, color_type)
            size1 = np.random.randint(min_size, max_size+1)
            size2 = np.random.randint(min_size, max_size+1)
            x1 = np.random.randint(self.image.size[0] - size1)
            y1 = np.random.randint(self.image.size[1] - size2)
            imageDraw.rectangle((x1,
                                 y1,
                                 x1 + size1,
                                 y1 + size2),fill=color, outline=color)
        super(SquareImageScratcher, self).damage()

#Options
#[0] min_radius
#[1] max_radius
#[2] min_num
#[3] max_num
#[4] color_type(1: black 2: white 3: random 4: extract from picture)

class EllipseImageScratcher(ImageScratcher):
    def damage(self):
        min_size = 5
        max_size = 10
        min_draw_num = 1
        max_draw_num = 3
        color_type = 1
        if( len(self.options) == 5):
            min_size = int(self.options[0])
            max_size = int(self.options[1])
            min_draw_num = int(self.options[2])
            max_draw_num = int(self.options[3])
            color_type = int(self.options[4])
        size = max_size - min_size

        imageDraw = ImageDraw.Draw(self.image)
        times = np.random.randint(min_draw_num, max_draw_num + 1)
        for i in range(times):
            color = self.selectColor(self.image.mode, color_type)
            ellipseSizeX = np.random.randint(size) + min_size
            ellipseSizeY = np.random.randint(size) + min_size
            x1 = np.random.randint(self.image.size[0])
            y1 = np.random.randint(self.image.size[1])
            imageDraw.ellipse((x1,
                               y1,
                               x1 + ellipseSizeX,
                               y1 + ellipseSizeY),fill=color, outline=color)
        super(EllipseImageScratcher, self).damage()

class ImageOverlayImageScratcher(ImageScratcher):
    def damage(self):
        imageDraw = ImageDraw.Draw(self.image)
        imageDraw.line((np.random.randint(self.image.size[0]),
                        np.random.randint(self.image.size[1]),
                        np.random.randint(self.image.size[0]),
                        np.random.randint(self.image.size[1])),fill=128)
        super(ImageOverlayImageScratcher, self).damage()

class AllRandomImageScratcher(ImageScratcher):
    def damage(self):
        randomtype = np.random.randint(3)#4)
        scratcher = None
        if randomtype == 0:
            scratcher = LineImageScratcher(self.input_filename, self.output_filename)
        elif randomtype == 1:
            scratcher = SquareImageScratcher(self.input_filename, self.output_filename)
        elif randomtype == 2:
            scratcher = EllipseImageScratcher(self.input_filename, self.output_filename)
        #elif randomtype == 3:
        #    scratcher = ImageOverlayImageScratcher(self.input_filename, self.output_filename)
        scratcher.damage()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "ex) damage_image.py input_image_filename output_image_filename damageType(1~4) (options)"
        print "       damageType 1 : LineScratch"
        print "       damageType 2 : SquareScratch"
        print "       damageType 3 : ElipseScratch"
        print "       damageType 4 : ImageOverlayScratch"
        print "       damageType 5 : AllRandomScratch"
        exit()

    imageScratcher = None

    if int(sys.argv[3]) == 1:
        imageScratcher = LineImageScratcher(sys.argv[1], sys.argv[2])
    elif int(sys.argv[3]) == 2:
        imageScratcher = SquareImageScratcher(sys.argv[1], sys.argv[2])
    elif int(sys.argv[3]) == 3:
        imageScratcher = EllipseImageScratcher(sys.argv[1], sys.argv[2])
    #elif int(sys.argv[3]) == 4:
    #    imageScratcher = ImageOverlayImageScratcher(sys.argv[1], sys.argv[2])
    elif int(sys.argv[3]) == 5:
        imageScratcher = AllRandomImageScratcher(sys.argv[1], sys.argv[2])
    else:
        print "Not defined image scratch type"
        exit()

    if len(sys.argv) > 4:
        imageScratcher.setOption(sys.argv[4:])
    imageScratcher.damage()
   
