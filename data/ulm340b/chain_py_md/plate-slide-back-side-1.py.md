

"""

# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate
    #  3. Line plate up with the goal
    #  4. Slide plate back into goal
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate"):
        robot.put("gripper below plate")
    if check("the robot's gripper is near plate"):
        robot.slide("plate side-ways into goal")
    
    
    
    
    
    

[eod] [code]# coding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 