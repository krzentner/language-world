
'''

prompt_unplug = '''


The task `peg-unplug-side` requires the robot to grab the peg and pull the it out from the side.
To grab the peg and pull the it out from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Slide the peg sideways out of the hole  4. Pull the peg out
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    If the gripper is still mostly around the peg, we can pull the peg out.
    - When peg is horizontally aligned with hole and the robot's gripper is forward aligned with the peg, move the robot's gripper until the robot's gripper is almost vertically aligned with the peg

The task `button-press` requires the robot to push the button down.
To push the button down reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from in front  2. Push down on the button
    To line up the robot's gripper as viewed from in front, you should do this.
    - When the robot's gripper is not horizontally aligned with button, move the robot's gripper until the robot's gripper is horizontally aligned with button and the robot's gripper is closed
    When the robot's gripper is horizontally aligned with the button, we can just push down on the button.
    - When the robot's gripper is horizontally aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    We don't need to be careful about the direction, since the