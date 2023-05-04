

Please write a few if statements to accomplish this task.
You should be able to use only 3 statements.
If your code requires more statements, then please try to think of a simpler solution to this task.

To learn more about this task, you can read this paper [Chen2020](https://arxiv.org/abs/1904.03972).

"""

if __name__ == "__main__":
    try:
        from .robot_program import *
    except ImportError:
        try:
            from robot_program import *
        except ImportError:
            pass

    print("\nBegin program")

    robot = Robot()

    print("\nBegin task")
    beginTask()

    print("## push: slide the puck to the target location")
    push(robot)
    robot.stop()

    print("## reach: reach to the target location")
    reach(robot)
    robot.stop()

    print("## window-close: slide the window closed to the right")
    window_close(robot)
    robot.stop()

    print("## peg-insert-side: grab the peg and insert it into the hole from the side")
    peg_insert_side(robot)
    robot.stop()

    print("## drawer-open: pull the drawer open")
    drawer_open(robot)
    robot.stop()

    print("## window-open: slide the window open to the left")
    window_open(robot)
    robot.stop()

    print("## pick-place: pick up the puck and hold it at the target location")
    pick_place(robot)
    robot.stop()

    print("## drawer-close: push the drawer close")
    drawer_close(robot)
    robot.stop()

    print("## door-open: pull the door open")
    door_open(robot)
    robot.stop()

    print("## button-press-topdown: push the button down from above")
    button_press_topdown(robot)
    robot.stop()

    print("\nEnd task")
    endTask()

    print("\nEnd program")
[eod] [code]import argparse
import os
from copy import deepcopy

from utils.logger import Logger

from configs import global_config
from models.model_runner import Runner, ModelOutput
from 