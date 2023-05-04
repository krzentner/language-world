
Steps:  1. Put gripper above the handle  2. Push gripper into the handle  3. Slide the handle down
First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, move the robot's gripper until the robot's gripper is vertically aligned with handle
    If the handle becomes left of the gripper, go back to putting the gripper above the handle. Because the handle is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the handle and the robot's gripper is closed
    If the robot's gripper is above the handle and the gripper is open, try closing it to push the handle down.
    - When the robot's gripper is above the handle and the robot's gripper is open, move the robot's gripper until the robot's gripper is above the handle and the robot's gripper is closed
    If the robot's gripper is above the handle and the gripper is closed, we've probably started pushing the handle down, and we should finish it off.
    - When the robot's gripper is forward aligned with the handle and the robot's gripper is closed, move the robot's gripper until the robot's gripper is horizontally aligned with handle
"""

_WELCOME_HINT = """\

    Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, move the robot's grip