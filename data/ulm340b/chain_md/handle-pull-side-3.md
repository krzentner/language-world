
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, the robot should put gripper above handle.
    As long as the handle is still below the gripper, and the gripper is forward aligned with the handle, move the gripper down onto the handle.
    - When the robot's gripper is forward aligned with handle, the robot should grab handle.
    As long as the handle is forward aligned with the robot's gripper, pull the handle open.
    - When the robot's gripper is forward aligned with handle, the robot should pull handle open.

The task `peg-unplug-side` requires the robot to unplug the peg from the hole.
To unplug the peg from the hole reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the peg  2. Grab the peg with the gripper  3. Slide the peg to the side
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    If the peg is still mostly inside the hole, slide the peg to the side.
    - When peg is not horizontally aligned with hole and the robot's gripper is forward aligned with peg, the robot should remove peg from hole.
'''

instructions_test_1 = '''
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `pick-out` requires the robot to pick up the block in the middle out of the three blocks.
To pick up the block in the middle out of the three blocks reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the middle block  2. Grab the block in the middle with the gripper  3. Lift the block in the middle up out of the stack
    First, put the gripper above the middle block.
    - When the robot's gripper is not vertically aligned with middle block, the robot should put gripper above middle block.
    If the middle block becomes left of the gripper, go back to