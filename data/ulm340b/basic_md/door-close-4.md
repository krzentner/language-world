

    - When the robot's gripper is near the door handle, the robot should close the gripper on the door handle.
    - When the robot's gripper is forward aligned with the door handle, the robot should push the door closed to the goal.

Please remember that the robot should be able to perform the task in the presence of visual distractors and random noise.

Let's start!

"""

button_press_topdown = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

Please remember that the robot should be able to perform the task in the presence of visual distractors and random noise.

Let's start!

"""

peg_insert_side = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

Please remember that the robot should be able to perform the task in the presence of visual distractors and random noise.

Let's start!

"""

drawer_open = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer