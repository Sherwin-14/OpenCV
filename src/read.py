import cv2 as cv

#img = cv.imread('Photos/Amazon-Emblem.jpg')

#cv.imshow('Amazon-Emblem',img)


#Reading video

capture=cv.VideoCapture('Videos/abc.mp4')

while True:
    isTrue,frame=capture.read()
    
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()    
