
    - First put the gripper right of the window handle
"""


task_descriptions = """Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `button-press-side` requires the robot to push the button sideways.
To push the button sideways reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the button  2. Line up the gripper  3. Push down on the button from the side
    Because this is "sideways", we just need to line up the gripper in front. Line up the robot's gripper in front.
    - When the robot's gripper is not left of the button, move the robot's gripper until the robot's gripper is left of the button
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is left of the button and the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with button

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the