# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:21:18 2019

@author: Hp
"""

#Image processing using PIL
from PIL import Image
img = Image.open("sample.jpg")
img = Image.open("sample.jpg").convert('LA')
img.save('greyscale.png')
img.show()
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.save("rotate.jpg")
img_rotate.show()

small_im = img.resize((160, 204), resample=Image.BICUBIC)
small_im.save('small.jpg')
small_im.show()

img.thumbnail((75,75))
print(img.width, img.height)
img.save('thumbnail.jpg')
