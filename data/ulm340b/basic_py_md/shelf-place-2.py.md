

(Note: your program will be graded on a robot that is holding a block.)
"""

def shelf_place(robot):
    #shelf_place: pick up the block and place it at the target location
    if check("the robot's gripper is not above the block and the robot's gripper is not near the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is above the block and the robot's gripper is not near the block"):
        robot.push("the gripper into the block")
    if check("the robot's gripper is near the block and the robot's gripper is not around the block"):
        robot.put("the gripper around the block")
    if check("the robot's gripper is around the block and the robot's gripper is open"):
        robot.close("the gripper around the block")
    if check("the robot's gripper is around the block"):
        robot.move("the block to the target")
    if check("the robot's gripper is near the target"):
        robot.open("the gripper around the block")
    if check("the robot's gripper is open"):
        robot.move("away from the block")
[eod] [code]import pandas as pd
import numpy as np


def gen_data():
    a = np.arange(10).reshape(5, 2)
    b = np.arange(10).reshape(2, 5)
    return pd.DataFrame(a, index=[
                         "A", "B", "C", "D", "E"], columns=["a", "b"]), pd.DataFrame(b, index=[
                                                                                        1, 2], columns=[
                                                                                                           "a", "b", "c", "d", "e"])


def test_join():
    df0, df1 = gen_data()
    assert df0.join(df1).to_string() == "              a  b  c  d  e\nA      0  1  2  3  4\nB      5  6  7  8  9\nC      0  1  2  3  4\nD      5  6  7  8  9\nE      0  1  2  3  4\