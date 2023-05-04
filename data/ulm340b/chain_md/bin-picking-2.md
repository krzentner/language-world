
    Steps:  1. Put gripper above cube  2. Put gripper around cube  3. Close gripper around cube  4. Lift gripper  5. Move cube to goal
    First, put the gripper roughly above the cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above cube, the robot should place gripper above cube.
    If the gripper is not around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should put gripper around cube.
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    Now, lift the gripper to try to pull the cube up.
    - When the robot's gripper is above cube and the robot's gripper is closed, the robot should lift gripper.
    If the cube is above the robot's gripper, we have successfully lifted it up, so we should move it to the goal.
    - When cube is above the robot's gripper, the robot should move cube to goal.
"""


INSTRUCTIONS_WITH_FEEDBACK = """Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top

    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed

    If the gripper is not near