
"""

task_info_list_val = [
    "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.",
    "The task `window-close` requires the robot to slide the window closed to the right.",
    "To slide the window closed to the right reliably, the robot should perform the following steps:",
    "    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.",
    "    - When the robot's gripper is near the window handle, the robot should slide window right.",
    "    - When the robot's gripper is in front of the window handle, the robot should push window right harder.",
    "The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.",
    "To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:",
    "    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.",
    "    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.",
    "    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.",
    "    - When peg is horizontally aligned with hole, the robot should insert peg into hole.",
    "The task `button-press-topdown` requires the robot to push the button down from above.",
    "To push the button down from above reliably, the robot should perform the following steps:",
    "    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.",
    "    - When the robot's gripper is vertically aligned with button, the robot should push down on button.",
    "The task `door-open` requires the robot to pull the door open.",
    "To pull the door open reliably, the robot should perform the following steps:",
    "    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.",
    "    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.",
    "    - When the robot's