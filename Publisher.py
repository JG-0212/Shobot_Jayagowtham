# Do not skip line 2
#!/usr/bin/env python
  
#import rospy
#import pyrealsense2 as rs
import json
import numpy as np

import cv2
#from std_msgs.msg import String
#loading the model from a website using API key
from roboflow import Roboflow
rf = Roboflow(api_key="OGCV1pPJDtCRgU2K1s3r")
project = rf.workspace().project("jg-intern")
model = project.version(2).model



#from ur5_tf.msg import InfoData, InfoDataArray # import the custom messages
  
  
def publisher():
    #pub = rospy.Publisher('Parameters',String, queue_size=10)
    #pub = rospy.Publisher('/infodata', InfoDataArray, queue_size=1) # create the publisher
    #rospy.init_node('Object_detector_model', anonymous=True)
    #rate = rospy.Rate(10)
    #infodata = InfoData() # create the infodata message
    #infodata_array = InfoDataArray() # create the infodata array
    #Starting the camera
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            #ret==1 means the frame is captured without any issue
            if ret:
                #converting the image from BGR to RGB
                frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
                cv2.imshow("image",frame)
                #converting the prediction from a dictionary to string
                pred = model.predict(frame,confidence=6-,overlap=60)
                temp =pred.json()
                pred.plot()
            #x_coord = temp["predictions"]["x"]
            #y_coord = temp["predictions"]["y"]
            #infodata.x= x_coord
            #infodata.y= y_coord
            #data = json.dumps(model.predict(frame,confidence=40, overlap=30).json())
            #rospy.loginfo(data)
            #pub.publish(data)
            #pub.publish(infodata_array.infos)
            #rate.sleep()
    finally:
        #releasing the camera
        cap.release()
  
if __name__=="__main__":
    publisher()