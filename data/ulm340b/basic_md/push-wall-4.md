

    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.
"""

instruction_with_answer_with_pronoun = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, it should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and its gripper is open, it should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, it should pull door open.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with drawer handle, it should put gripper above drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and its gripper is not around drawer handle, it should put gripper around drawer handle.
    - When the robot's gripper is around drawer handle, it should pull away from drawer.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, it should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, it should push drawer closed.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, it should put gripper above button.
    - When the robot's gripper is vertically aligned with button, it should push down on button.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
