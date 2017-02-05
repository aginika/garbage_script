#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageChops, ImageEnhance
import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "ex) damage_image.py ok ng diff"
        exit()

    ok_image = Image.open(sys.argv[1])
    ng_image = Image.open(sys.argv[2])

    diff1 = ImageChops.subtract(ng_image, ok_image)
    diff1 = ImageEnhance.Contrast(diff1).enhance(10).convert("L")
    diff2 = ImageChops.subtract(ok_image, ng_image)
    diff2 = ImageEnhance.Contrast(diff2).enhance(10).convert("L")
    diff = ImageChops.add(diff1, diff2)
    diff = diff.point(lambda x: 0 if x<1 else 255, '1')
    diff.save(sys.argv[3])
