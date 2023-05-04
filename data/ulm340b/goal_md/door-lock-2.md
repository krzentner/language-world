
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull the handle and close the door  4. Release the handle and turn the dial
    First, put the gripper above door handle, so that the robot can open the door easily.
    - When the robot's gripper is not above door handle, move the robot's gripper until the robot's gripper is above door handle
    Once the gripper is above door handle, we can grab the dial by dropping it and closing it.
    - When the robot's gripper is above door handle and the robot's gripper is not around door handle, move the robot's gripper until the robot's gripper is forward aligned with door handle and the robot's gripper is closed
    We can open the door easily once the robot has grabbed the door handle.
    - When the robot's gripper is around door handle, move the robot's gripper until the robot's gripper is left of door handle
    Once the door is opened, we can release the handle and turn the dial to lock the door.
    - When the robot's gripper is left of door handle, move the robot's gripper until the robot's gripper is near the door handle

The task `pick-place-topdown` requires the robot to pick up the puck from above and hold it at the target location.
To pick up the puck from above and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Close the gripper on top of the puck  3. Move the puck to the goal
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with puck, move the robot's gripper until the robot's gripper is vertically aligned with puck and the robot's gripper is closed
    Now that the gripper is lined up, close it on the puck.
    - When the robot's gripper is near puck, move the robot's gripper until the robot's gripper is around puck
    If the gripper is closed on top of the puck, we can just move the gripper to the target location.
    - When the robot's gripper is above puck, move the robot's gripper until the robot's gripper is near the target location

The task `button-press-side` requires the robot to push the button