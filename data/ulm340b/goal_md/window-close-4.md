
'''

[eod] [code]from typing import List, Tuple, Any


def to_list(v: Any) -> List[Any]:
    if v is None:
        return []
    elif isinstance(v, (list, tuple)):
        return list(v)
    else:
        return [v]


def to_tuple(v: Any) -> Tuple[Any, ...]:
    if v is None:
        return ()
    elif isinstance(v, (list, tuple)):
        return tuple(v)
    else:
        return (v,)
[eod] [code]import cv2
import mediapipe as mp
import time
import numpy as np
from draw_circle import *

class HandDetector():

    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.detection_con, self.track_con)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx,