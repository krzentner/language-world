
    Steps:  1. Move gripper into alignment with handle from side  2. Push handle down from side
    Line up the robot's gripper with the handle as seen from the side.
    - When the robot's gripper is not horizontally aligned with the handle, move the robot's gripper until the robot's gripper is horizontally aligned with the handle
    Once it's aligned, we can just push the handle down.
    - When the robot's gripper is horizontally aligned with the handle, move the robot's gripper until the robot's gripper is above the handle

The task `pick-place-with-obstacle` requires the robot to pick up the puck and hold it at the target location, while avoiding hitting the obstacle with the gripper.
To pick up the puck and hold it at the target location, while avoiding hitting the obstacle with the gripper reliably, the robot should perform the following steps:
    Steps:  1. Avoid obstacle  2. Put gripper above puck  3. Grab the puck  4. Move the puck to the goal
    AVOID THE OBSTACLE!!!!
    - When the robot's gripper is above obstacle, move the robot's gripper until the robot's gripper is forward aligned with obstacle
    As long as the gripper isn't above the puck, move the gripper above the puck.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper is not below the puck, close it.
    - When the robot's gripper is not below the puck and the robot's gripper is not left of the puck, move the robot's gripper until the robot's gripper is closed and the robot's gripper is vertically aligned with the puck
    As long as the gripper is not left of the puck, pull the gripper left to grab the puck.
    - When the robot's gripper is closed and the robot's gripper is not left of the puck and the puck is not below the robot's gripper, move the robot's gripper until the robot's gripper is closed and the puck is below the robot's gripper
    Now, we can move the puck to the goal.
    - When the robot's gripper is closed and the robot's gripper is left of the puck, move the robot's gripper until the robot's gripper is near the target location

The task `peg-unstack` requires the robot to grab the top peg and lift it up, removing it from the stack.