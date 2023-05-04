

Your program should first check that the robot is vertically aligned with the drawer handle.
If not, it should put the robot's gripper above the handle.

Then, it should close the robot's gripper around the drawer handle.

If it's not already done, the robot should pull the drawer handle until its gripper is in front of the drawer handle.

If its gripper is in front of the drawer handle, it should push the drawer closed.


'''
def drawer_close(robot):
    # First check if the gripper is aligned with the handle
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.close("gripper around drawer handle")
        if check("the robot's gripper is in front of the drawer handle"):
            robot.push("the drawer closed")

drawer_close(robot)
[eod] [code]import cv2
import os
import numpy as np

cap = cv2.VideoCapture(0)

i=0
while True:
    check,frame=cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces=face.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
    for x,y,w,h in faces:
        roi_gray = gray[y:y+w, x:x+h]
        roi_color = frame[y:y+w, x:x+h]
        print(x,y)


    cv2.imshow('frame',gray)


    key = cv2.waitKey(1)
    if key == 27:
        break
    # if key == 259:
    #     i+=1
    #     cv2.imwrite(str(i)+'.jpg',gray)

cap.release()
cv2.destroyAllWindows()
[eod] [code]import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog

class App(object):
    def __init__(self, master):