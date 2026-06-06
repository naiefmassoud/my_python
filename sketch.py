#!/usr/bin/env python3

""" Photo Sketching Using Python """
import cv2 as cv
img = cv.imread("naief.png")

## Image to Gray Image
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

## Gray Image to Inverted Gray Image
inverted_gray_image = 255-gray_image

## Blurring The Inverted Gray Image
blurred_inverted_gray_image = cv.GaussianBlur(inverted_gray_image, (19,19),0)

## Inverting the blurred image
inverted_blurred_image = 255-blurred_inverted_gray_image

### Preparing Photo sketching
sketck = cv.divide(gray_image, inverted_blurred_image,scale= 256.0)

### Transform into Thumbnail
#maxsize = (1024,1024)
#imThumb = cv.resize(sketck,maxsize,interpolation=cv.CV_INTER_AREA)

"""
cv.imshow("Original Image",img)
cv.imshow("Pencil Sketch", sketck)
cv.waitKey(0)
"""
cv.imwrite("image_sketch.png", sketck)
#cv.imwrite("image_sketch_thumb.png", imThumb)


##################################
# importing Image class from PIL package
from PIL import Image

# creating a object
image = Image.open(r"image_sketch.png")
MAX_SIZE = (300, 300)

image.thumbnail(MAX_SIZE)

# creating thumbnail
image.save('image_sketch_thumb.png')
image.show()
##################################
