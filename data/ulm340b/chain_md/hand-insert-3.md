
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Slide puck over to the goal
    The robot should first put the gripper above the puck.
    - When the robot's gripper is not above puck, the robot should place gripper above puck.
    If the robot's gripper is not around puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to slide the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is near puck and the robot's gripper is closed, the robot should slide puck to goal.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?
    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window