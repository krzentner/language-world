
    - When the robot's gripper is not near the plate, the robot should move gripper to plate.
    - When the robot's gripper is near the plate, the robot should push plate to goal.

The task `button-press-front` requires the robot to push the button from the front.
To push the button from the front reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with the button, the robot should put gripper in front of button.
    - When the robot's gripper is horizontally aligned with the button and the robot's gripper is in front of the button, the robot should push the button.

The task `button-press-bottom` requires the robot to push the button from the bottom.
To push the button from the bottom reliably, the robot should perform the following steps:
    - When the robot's gripper is not aligned with button and below the button, the robot should put gripper below button.
    - When the robot's gripper is aligned with button and below the button, the robot should push the button.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with door handle, the robot should put the gripper above the door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is open, the robot should grab door handle.
    - When the robot's gripper is vertically aligned with door handle, the robot should push door closed.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg, the robot should align peg to hole.
    - When the peg is horizontally aligned with the hole, the robot should drop the peg into the hole.
""",

    """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down