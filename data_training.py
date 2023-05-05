from itertools import count
import cv2
import pickle




try:
    with open('parking_area','rb') as f:
        parking_list = pickle.load(f)
except:
    parking_list = []
    
    
width = 45
height = 150




def draw_parking(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        parking_list.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(parking_list):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                parking_list.pop(i)
    with open("parking_area","wb") as f:
        pickle.dump(parking_list,f)


while True:
    image = cv2.imread("parking1.jpg")
    image_resize = cv2.resize(image,(640,480))
    for pos in parking_list:
        cv2.rectangle(image_resize,pos,(pos[0]+width,pos[1]+height),(0,255,0),2)
    cv2.imshow("parking",image_resize)
    cv2.setMouseCallback("parking",draw_parking)
    cv2.waitKey(0)