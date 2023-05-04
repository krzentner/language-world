
    Steps:  1. Put gripper above box lid  2. Drop gripper around box lid  3. Close gripper around box lid  4. Lift box lid  5. Place box lid on top of the box




"""

import random
import numpy as np

from task_generator import task_generator



task_names = ['push', 'window-close', 'window-open', 'button-press-topdown', 'pick-place', 'drawer-open', 'drawer-close', 'door-open', 'peg-insert-side', 'push-right', 'push-left', 'push-forward', 'push-forward-harder', 'reach', 'slide', 'box-close']

task_descriptions = {
    'push': (
        "The task `push` requires the robot to slide the puck to the target location.\n"
        "To slide the puck to the target location reliably, the robot should perform the following steps:\n"
        "    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal\n"
        "The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.\n"
        "- When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.\n"
        "If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.\n"
        "- When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.\n"
        "If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.\n"
        "- When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal."
    ),
    'window-close': (
        "The task `window-close` requires the robot to slide the window closed to the right.\n"
        "To slide the window closed to the right reliably, the