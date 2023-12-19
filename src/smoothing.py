import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cats',img)

#Averaging
average=cv.blur(img,(3,3))
cv.imshow('average blur',average)

#Gaussian Blur-less blurring than averaging method,but it is more natural when compared to averaging.
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian',gauss)

#Median Blur-it is bascially same as averaging.instead of finding the average of surrounding pixels ,median of the surrounding pixels is calculated. it is generally more effective in reducing the noiseand is not meant for high kernel sizes.
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

#Bilateral Blurring-applies blurring and retains the edges in the images.higher vallues of parameters for median and bilateral fucnions end up giving a washed up/smudged image. 
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)