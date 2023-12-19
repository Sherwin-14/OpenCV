import cv2 as cv
import numpy as np

img=cv.imread('Photos/sherkhan.jpg')

cv.imshow('Sher',img)


#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimesnions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimesnions)

translated_image=translate(img,100,100)

cv.imshow('Translated',translated_image)

cv.waitKey(0)

# -x-->left
# -y-->UP
# x-->Right
#y-->Down

# Roatation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
cv.imshow('Rotated',rotated) 

roatted_again=rotate(img,35)
cv.imshow('roatated_again',roatted_again)

#Flipping
flip=cv.flip(img,-1)
cv.imshow('Flip',flip)


cv.waitKey(0)