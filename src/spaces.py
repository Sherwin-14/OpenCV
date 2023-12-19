import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photos/abc.jpg')
cv.imshow('abc',img)

plt.imshow(img)
plt.show()

"""
#BGR TO Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#BGR TO HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR TO RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(img)
plt.show()
"""


cv.waitKey(0)