import cv2
import numpy as np

MIN_MATCHES = 20
detector = cv2.ORB_create(nfeatures=5000)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
search_params = dict(checks=100)
flann = cv2.FlannBasedMatcher(index_params,search_params)

def load_input():
   
    input_image = cv2.imread('meluha.jpg')
    input_image = cv2.resize(input_image, (400,550),interpolation=cv2.INTER.AREA)  
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

     # find the keypoints with ORB
     keypoints, descriptors = detector.detectAndCompute(gray_image, None) 
      
     return gray_image, keypoints, descriptors 

def compute_matches(descriptors_input, descriptors_output):
      #Match descriptors
       if(len(descriptors_output)!=0 and len(descriptors_input)!=0):
            matches = flann.knnMatch(np.asarray(descriptors_input,np.float32),np.asarray(descriptors output, np.float32))
            good = []
            for m,n in matches:
                 if m.distance < 0.68*n.distance:  
                     good.append([m])
            return good
       else:
            return None 



  #Main Working Logic
  if __name__=='__main__':

    #Getting Information form the Input image
    input_image,input_keypoints, input_descriptors =load_input()   
    
    #Getting camera ready
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    while(ret):
        ret, frame = cap.read() 

    #Condition Check for error escaping
    if(len(input_keypoints)<MIN_MATCHES):
       continue

   #Resizing input image for fast computation
   frame = cv2.resize(frame, (700, 600))  
   frame_bw =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   #computing and matching the keypoints of input image and query image
    output_keypoints,output_descriptors = detector.detectAndCompute(frame_bw,None) 
    matches = compute_matches(input_descriptors,output_descriptors)

    if(matches!=None):
        output_final = cv2.drawMatchesKnn(input_image,input_keypoints,frame,output_keypoints,matches,None,flag) 
        cv2.imshow('Final Output', output_final)
    else:
        cv2.imshow('Final Output', frame)
    key = cv2.waitKey(5)
    if(key==27):
        break 