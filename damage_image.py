#!/usr/bin/env python
from PIL import Image, ImageDraw
import sys
import numpy as np



class ImageScratcher(object):
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.image = Image.open(self.input_filename)

    def damage(self):
        self.image.save(self.output_filename)

class LineImageScratcher(ImageScratcher):
    def damage(self):
        imageDraw = ImageDraw.Draw(self.image)
        imageDraw.line((np.random.randint(self.image.size[0]),
                        np.random.randint(self.image.size[1]),
                        np.random.randint(self.image.size[0]),
                        np.random.randint(self.image.size[1])),fill=128)
        super(LineImageScratcher, self).damage()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "ex) damage_image.py input_image_filename output_image_filename damageType(1~4)"
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
    elif int(sys.argv[3]) == 4:
        imageScratcher = ImageOverlayImageScratcher(sys.argv[1], sys.argv[2])
    elif int(sys.argv[3]) == 5:
        imageScratcher = AllRandomImageScratcher(sys.argv[1], sys.argv[2])
    else:
        print "Not defined image scratch type"
        exit()

    imageScratcher.damage()
   
