import cv2 as cv

img=cv.imread('Photos/bollywood-tolly-main.jpg')
cv.imshow('Ratan Tata',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Ratan Tata',gray)

haar_Cascade=cv.CascadeClassifier('haar_face.xml')

face_rect=haar_Cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=11)

print(f'Number of faces found ={len(face_rect)}')

for (x,w,y,h) in face_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces',img)  

cv.waitKey(0)