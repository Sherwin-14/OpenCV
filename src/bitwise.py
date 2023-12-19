import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise AND-intersecting
bitwise_ands=cv.bitwise_and(rectangle,circle)
cv.imshow('BitwiseAND',bitwise_ands)

#bitwise OR-non-intersecting +intersecting
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_or)

#bitwise XOR-non-inersecting
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise',bitwise_xor)

#bitiwse NOT-reversing of colors
bitwsie_NOT=cv.bitwise_not(rectangle,circle)
cv.imshow('Bitwise not',bitwsie_NOT)

cv.waitKey(0)