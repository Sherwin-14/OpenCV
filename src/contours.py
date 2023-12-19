import cv2 as cv
import numpy as np

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape,dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('Cnnay Edges',canny)

## contours can be called as edges.

#ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)

#use canny method first and then find contours rather than threshoding the image and then finding the contours because simple thresholding has its own disadvantages.

contours,heiracrchies=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)