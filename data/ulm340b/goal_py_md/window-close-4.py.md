

When the robot's gripper is near the window handle we can probably slide the window closed now by moving the gripper right.
"""

# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
[eod] [code]#!/usr/bin/env python3

import sys
import string
import math

class Vocab:
    def __init__(self):
        self.word2idx = {'<PAD>': 0, '<UNK>': 1, '</S>': 2, '<SOS>': 3}
        self.idx2word = {0: '<PAD>', 1: '<UNK>', 2: '</S>', 3: '<SOS>'}
        self.word2count = {}

    def index(self, word):
        if word not in self.word2idx:
            self.word2idx[word] = len(self.word2idx)
            self.idx2word[len(self.idx2word)] = word
            self.word2count[word] = 0
        return self.word2idx[word]

    def count(self, word):
        if word not in self.word2idx:
            self.index(word)
        if word not in self.word2count:
            self.word2count[word] = 0
        self.word2count[word] += 1
        return self.word2count[word]

    def get_words(self):
        return list(self.word2idx.keys())[4:]

    def get_idxs(self):
        return list(self.word2idx.values())[