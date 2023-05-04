
    - When the robot's gripper is not vertically aligned with the wrench, the robot should put gripper above wrench.
    - When wrench is not forward aligned with the robot's gripper, the robot should grab wrench.
    - When the robot's gripper is forward aligned with the wrench, the robot should grab peg.
    - When the robot's gripper is around peg, the robot should push peg down.

The task `push-back` requires the robot to push the button with a gripper's back.
To push the button with a gripper's back reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When button is below robot's gripper, the robot should push back on button.
"""

"""
Hello. Today I would like you to help me control a robot. The robot has two arms and two grippers that it can use to grab small objects.


The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's left gripper is not above puck and the robot's left gripper is not vertically aligned with the puck, the robot should put the left gripper above the puck.
    - When the robot's left gripper is vertically aligned with the puck and the robot's left gripper is not near puck, the robot should push the left gripper into the puck.
    - When the robot's left gripper is near the puck and the puck is below the robot's left gripper, the robot should slide the puck to the goal.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's left gripper is not vertically aligned with button, the robot should put left gripper above button.
    - When the robot's left gripper is vertically aligned with button, the robot should push down on button.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    - When the robot's left gripper is not near reach target, the robot should reach to goal.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's right gripper is not almost vertically aligned with door handle and the robot's left gripper is