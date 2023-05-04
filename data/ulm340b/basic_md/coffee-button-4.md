

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, what steps the robot should perform?

The task `peg-unstack` requires the robot to grab the peg and unstack it from the tower.
To grab the peg and unstack it from the tower reliably, what steps the robot should perform?

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?

The task `peg-remove` requires the robot to grab the peg and remove it from the hole.
To grab the peg and remove it from the hole reliably, what steps the robot should perform?


"""

################################################################
#
#   EXPERIMENT_INSTRUCTIONS
#
################################################################

def get_instructions(task_key):
    instr_dict = {"drawer-open": "To pull the drawer open reliably, the robot should perform the following steps: \n \n    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle. \n    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle. \n    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.",
                  
                  "window-close": "To slide the window closed to the right reliably, the robot should perform the following steps: \n \n    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle. \n    - When the robot's gripper is near the window handle, the robot should slide window right. \n    - When the robot's gripper is in front of the window handle, the robot should push window right harder.", 
                  
                  "peg-insert-side": "To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps: \n \n    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg. \n    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg. \n    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should