

    [ ] 1) When the plate is not above the target location, the robot should put the gripper above the plate.
    [ ] 2) When the robot's gripper is above the plate and the plate is not near the target, the robot should push the plate to the target.
    [ ] 3) When the plate is near the target, the robot should put the plate at the target.
"""

instructions = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably,