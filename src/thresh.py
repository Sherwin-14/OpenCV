import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Simple Thresold
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse',thresh_inv)

#Adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,5)
cv.imshow('Adaptive threshold',adaptive_thresh)

cv.waitKey(0)