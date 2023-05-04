

And then write the steps of the algorithm, using the methods described in the previous tasks.
When you finish writing your program, please tell me the full source code.
"""


def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab the peg with the gripper
    #  3. Pull out the peg out of hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is not above the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("above the peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("above the peg", close_gripper=True)
[eod] [code]# 10171번_빗물

## 물이 고인 깊이 = 가장 긴 두 장애물 간의 거리 - 더 낮은 장애물의 높이
## 가장 긴 두 장애물 간의 거리 : 높이가 가장 높은 인덱스 - 높이가 가장 낮은 인덱스
## 더 낮은 장애물의 높이 : 높이가 가장 낮은 인덱스에 해당하는 건물 높이
## 12
## 10
## 7
## 11
## 7
## 5
## 4
## 12
## 15
## 5
## 7
## 1
## 3

## 가장 긴 두 장애물 간의 거리 = 가장 높이 높은 인덱스 - 높이가 가장 낮은 인덱스
## 높이가 가장 높은 인덱스는 높이를 저장하는 리스트에서 최대값을 주는 인덱스
## 높이가 가장 낮은 인덱스는 높이를 저장하는 리스트에서 최소값을 주는 인덱스
## -> 이 둘의 차가 가장 긴 두 장애물간의 거리

import sys

A = int(sys.stdin.readline())
B = list