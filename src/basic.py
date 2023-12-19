import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

# Converting to grayscale --- here an image which has three channels (BGR) is converted into a grayscale image and for that puprose a specific function is used.
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur -- remvoes noise form the image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade-- to get of rid of the edges we can apply blur 
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

#Dilate-dilate the image using structirng elemnts thee structuring elemensts are canny 
dilated=cv.dilate(canny,(7,7),iterations=1)
cv.imshow('Dilated',dilated)

#Resize-- on background the interpolation happnes and there are three major interpolations first one is INTER_AREA used when we are shrinking hte image ,while INTER_LINEAR,OR INTER_CUBIC used when we are zooming the image inter_cunbic being the slowest of all three
resize=cv.resize(img,(500,500))
cv.imshow('Resized',resize)

#Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)