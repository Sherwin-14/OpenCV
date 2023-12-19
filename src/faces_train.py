import os
import cv2 as cv
import numpy as np

people=['Ben Affleck','Mindy Kaling']
DIR=r'C:\Users\Asus\Desktop\Faces'

haar_Cascade=cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_Cascade.detectMultiScale(gray,1.1,4)

            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training Done ----------')

features=np.array(features,dtype='object')
labels=np.array(labels)

face_recongizer=cv.face.LBPHFaceRecognizer_create()

#Train the reconginezer

face_recongizer.train(features,labels)


face_recongizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)