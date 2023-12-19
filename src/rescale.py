import cv2 as cv

img = cv.imread('Photos/Amazon-Emblem.jpg')

#cv.imshow('Amazon-Emblem',img)

def rescaleFrame(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #Only works for live video
    capture.set(3,width)
    capture.set(4,height)


capture=cv.VideoCapture('Videos/abc.mp4')

while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame)

    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 