

'''

# Door unlocking

print('\n# door-unlock: turn the dial on the door\ndef door_unlock(robot):\n')


# Steps:
#  1. Put gripper above dial
#  2. Move gripper around dial
#  3. Turn dial to open
#  4. Open the door




print('if check("the robot\'s gripper is not above the dial"):')
print('  robot.put("the gripper above the dial")')
print('if check("the robot\'s gripper is above the dial and the robot\'s gripper is not around the dial"):')
print('  robot.put("the gripper around the dial")')
print('if check("the robot\'s gripper is around the dial and the dial is not turned"):')
print('  robot.turn("the dial")')
print('if check("the dial is turned"):')
print('  robot.open("the door")')
print('')












[eod] [code]from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import sys
sys.path.append('.')
import datasets

#print(datasets.__file__)


plt.ion()   # interactive mode

data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

data_dir = '/opt/ml/input/data/train/'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),