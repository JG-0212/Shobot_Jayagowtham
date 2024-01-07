import cv2
#from picamera2 import Picamera2, Preview
#from libcamera import controls
#picam2 = Picamera2()
#picam2.start()
from roboflow import Roboflow
rf = Roboflow(api_key="OGCV1pPJDtCRgU2K1s3r")
project = rf.workspace().project("jg-intern")
model = project.version(4).model
cap = cv2.VideoCapture(0)

z = 50
#the distance from camera and our object in cm

frame_length = 43.5
frame_width = 32.625
pixel_length = 640
pixel_width = 480
#camera specs

y_calibration = 0.00075 #units/cm
x_calibration = 0.001 #units/cm

#image resolution = (480,640,3)
while True:
    ret,img =cap.read()
    if ret==1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        predictions = model.predict(img, confidence=40,overlap=10).json()
        #this is a dictionary
        detections=[]
        #print(type(predictions))
        for object in predictions:
            #print(type(predictions[object]))
            if isinstance(predictions[object],list) and predictions[object]:
                temp = {}
                temp['x']=predictions[object][0]['x']
                temp['y']=predictions[object][0]['y']
                temp['width']=predictions[object][0]['width']
                temp['height']=predictions[object][0]['height']
                temp['class']=predictions[object][0]['class']
                detections.append(temp)

        #print(predictions)
        #print(detections)
        for bounding_box in predictions['predictions']:
                xo_pixel = bounding_box['x']
                yo_pixel = bounding_box['y']
                x_real = (xo_pixel*frame_length)/(pixel_length)
                y_real = (yo_pixel*frame_width)/(pixel_width)

                x_robot = x_real*x_calibration
                y_robot = y_real*y_calibration

                x1 = bounding_box['x'] - bounding_box['width'] / 2
                x2 = bounding_box['x'] + bounding_box['width'] / 2
                y1 = bounding_box['y'] - bounding_box['height'] / 2
                y2 = bounding_box['y'] + bounding_box['height'] / 2
                start_point = (int(x1), int(y1))
                end_point = (int(x2), int(y2))
                cv2.rectangle(img, start_point, end_point, color=(0,0,255), thickness=2)
                cv2.putText(img,bounding_box["class"],(int(x1), int(y1) - 10),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 0.6,color = (0,255, 0),thickness=2)
                cv2.putText(img,"x:"+("%.2f"%x_real)+"cm "+"y:"+("%.2f"%y_real)+"cm ",(int(xo_pixel), int(yo_pixel)),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 0.6,color = (255, 0, 0),thickness=2)

        cv2.imshow('Camera', img)
        key =cv2.waitKey(1)
        if(key==27):
            break
        #print(img.shape)
cap.release()
cv2.destroyAllWindows()