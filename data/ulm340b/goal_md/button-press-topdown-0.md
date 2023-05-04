
    Steps:  1. Move gripper above button  2. Push gripper down against the button
    First, put the gripper roughly above button, so that we don't bump it while trying to press it.
    - When the robot's gripper is not above the button, move the robot's gripper until the robot's gripper is above the button
    Now that the gripper is above the button, try pushing it.
    - When the robot's gripper is above button and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the button and the robot's gripper is closed

The task `sweep` requires the robot to sweep the puck to the target location.
To sweep the puck to the target location reliably, what steps the robot should perform?
    Steps:  1. Move gripper above the puck  2. Push gripper into top of puck  3. Sweep puck sideways to goal
    The robot can push the puck by pressing it down from above and moving the gripper to the side. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to press the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    If the gripper is near the puck, we've probably pressed the puck down and can now sweep it to the target location.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?
    Steps:  1. Put gripper left of the door handle  2. Push the door closed
    First, put the gripper left of the door handle.
    - When the robot's gripper is not left of the door handle, move the robot's gripper until the robot's gripper is left of the door handle
    If the robot'