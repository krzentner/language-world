

You may want to use some of the code from the other functions above.

If you get stuck and want to see an example solution,
you can view the script [on GitHub](https://github.com/alexirpan/ai-experiments/blob/main/robot/robot-prompt/prompt.py)
(which should be linked as the first line of the code above).
"""
[eod] [code]import numpy as np
import argparse
import imutils
import random
import cv2
import torch

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-m", "--model", required=True,
	help="path to trained model")
ap.add_argument("-y", "--yolo", required=True,
	help="base path to YOLO directory")
args = vars(ap.parse_args())

# construct the argument parser and parse the arguments


# load YOLO object detector trained on COCO dataset (80 classes)
print("[INFO] loading YOLO from disk...")

net = cv2.dnn.readNetFromDarknet(args["yolo"], args["model"])

# load image from disk
image = cv2.imread(args["image"])
image = imutils.resize(image, width=400)

(H, W) = image.shape[:2]
# determine only the *output* layer names that we need from YOLO
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# construct a blob from the input image and then perform a forward
# pass of the YOLO object detector, giving us our bounding boxes and
# associated probabilities
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
	swapRB=True, crop=False)
net.setInput(blob)
start = time.time()
layerOutputs = net.forward(ln)
end = time.time()


# initialize our lists of detected bounding boxes, confidences, and
# class IDs, respectively
boxes = []
confidences = []
classIDs = []

# loop over each of the layer outputs
for output in layerOutputs:
	# loop over each of the detections
	for detection in output:
		# extract the class ID and confidence (i.e., probability) of
		# the current object detection
		scores = detection