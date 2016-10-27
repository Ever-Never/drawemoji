#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import os.path
import sys

cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
print('Looking for files at {}'.format(cwd))
image = Image.new('RGBA', (608,272), (255,255,255,0))
font = ImageFont.truetype(os.path.join(cwd, 'fonts/TwitterColorEmoji-SVGinOT.ttf'), 40)
ctx = ImageDraw.Draw(image)
ctx.text((10,10), u'🦄', font=font, fill=(0,0,0,255))
image.save(os.path.join(cwd, 'image.png'))
