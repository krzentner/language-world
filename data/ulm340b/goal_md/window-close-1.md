
    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the robot's gripper is not vertically lined up with the window handle, we should move the gripper near the window handle to start pushing
    - When the robot's gripper is near the window handle, move the robot's gripper until the robot's gripper is forward aligned with the window handle
    If the robot's gripper is near the window handle we can probably slide the window closed now by moving the gripper right.
    - When the robot's gripper is in front of the window handle, move the robot's gripper until the robot's gripper is vertically aligned with the window handle

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, move the robot's gripper until the robot's gripper is around the door handle

The task `peg-unstack` requires the robot to pick up the top of the two stacked objects.
To pick up the top of the two stacked objects reliably, what steps the robot should perform?
    Steps:  1. Put gripper above top peg  2. Grab the top peg by closing gripper around it  3. Move peg up in the air
    Before we can grab the top peg, we need to put the gripper above it.
    - When the robot's gripper is not around the top peg and the robot's gripper is not above the top peg, move the robot's gripper until the robot's gripper is above the top peg
    As long as the gripper is around the top peg and the peg is not above the gripper, we can probably lift the peg.
    - When the robot's gripper is above the top peg and the top peg is not above the robot's