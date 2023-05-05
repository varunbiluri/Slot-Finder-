import  cv2
import pickle
import numpy as np
import csv




try:
    with open("parking_area","rb") as f:
        parking_list = pickle.load(f)
except:
    parking_list = []
    
    

def freeSpace(spaceCount):
    data = [spaceCount]
    with open('freespace.csv',mode='w',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(data)

def checking(video_resize):
    spaceCount = 0
    for pos in parking_list:
        x,y = pos
        video = video_resize[y:y+height,x:x+width]
        count = cv2.countNonZero(video)
        if count < 1500:
            spaceCount += 1
            color = (0,255,0)
            tickness = 2
        else:
            color = (0,0,255)
            tickness = 2
        cv2.rectangle(video_pos,pos,(x+width,y+height),color,tickness)
    cv2.rectangle(video_pos,(40,30),(300,80),(180,0,180),-1)
    cv2.putText(video_pos,f'Free Slots:{spaceCount}/{len(parking_list)}',(50,60),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,255,255),2)
    freeSpace(spaceCount)
    


width = 45
height = 150

capture = cv2.VideoCapture("parking.mp4")


while True:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES,0)
    success , image = capture.read()
    
    video_pos = cv2.resize(image,(640,480))
    
    imageGray = cv2.cvtColor(video_pos,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",imageGray)
    
    imageBlur = cv2.GaussianBlur(imageGray,(3,3),1)
    cv2.imshow("blur",imageBlur)
    
    imageThreshold = cv2.adaptiveThreshold(imageBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    cv2.imshow("thershold",imageThreshold)
    
    imageMeadianBlur = cv2.medianBlur(imageThreshold,5)
    cv2.imshow("mblur",imageMeadianBlur)
    
    kernel = np.ones((3,3),np.uint8)
    
    imageDilate = cv2.dilate(imageMeadianBlur,kernel,iterations=1)
    cv2.imshow("dilate",imageDilate)
    
    checking(imageDilate)
    
    cv2.imshow("image",video_pos)
    
    cv2.waitKey(10)