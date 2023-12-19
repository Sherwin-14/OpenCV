import numpy as np
import cv2 as cv

haar_cascade=cv.CascadeClassifier('haar_face.xml')

people=['Ben Affleck','Mindy Kaling']
features=np.load('features.npy',allow_pickle=True)
labels=np.load('labels.npy',allow_pickle=True)

face_recongizer=cv.face.LBPHFaceRecognizer_create()
face_recongizer.read('face_trained.yml')

img=cv.imread(r'C:\Users\Asus\Desktop\Faces\Ben Affleck\2.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#Detect the face in the image
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]
    label,confidence=face_recongizer.predict(faces_roi)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    print(f'{people[label]} with confidenece of {confidence}')

cv.imshow('Detected Image',img)

cv.waitKey(0)
