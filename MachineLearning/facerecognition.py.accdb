import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

#plot image by default BGR
img = cv2.imread('') 
plt.imshow(img) 

#plt image BGR2RGB
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#FaceAnalyzer function
 predictions = DeepFace.analyze(img) 
 type(predictions)  
 predictions['dominant_emotion'] 
 
#we are trying to draw a ractangle across the face
faceCascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 #print(faceCascade.empty())
faces = faceCascade.detectMultiScale(gray,1.1,4)

#Draw a rectangle around tha faces
for(x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
   plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  

font = cv2.FONT_HERSHEY_SIMPLEX

    # Use putText() method for 
    # inserting text on video
 cv2.putText(img, 
                 predictions['dominant_emotion'],
                 (50, 50),
                 font, 3,
                 (0, 255, 0),
                 2,
                 cv2.LINE_4) ;

 plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

                