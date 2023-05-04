
    Steps:  1. Put gripper in front of the wall  2. Move the gripper on the top of the wall  3. Put gripper above button  4. Push down on the button from the top
    Because there is a wall, we first need to put the gripper in front of the wall.
    - When the robot's gripper is not in front of the wall, the robot should put gripper in front of wall.
    Now that the gripper is in front of the wall, put it on the top of the wall.
    - When the robot's gripper is in front of the wall and the robot's gripper is not on top of the wall, the robot should put gripper on the wall.
    Now that the gripper is on the wall, put the gripper above the button.
    - When the robot's gripper is on the wall and the robot's gripper is not above button, the robot should put gripper above button.
    Now that the gripper is above button, push down on it.
    - When the robot's gripper is above button, the robot should push down on the button from the top.

The task `lever-pull` requires the robot to grab the lever handle and pull it.
To grab the lever handle and pull it reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above lever handle  2. Grab the lever handle with the gripper  3. Pull lever handle back
    First, put the gripper above the lever handle.
    - When the robot's gripper is not vertically aligned with lever handle, the robot should put gripper above lever handle.
    If the lever handle becomes left of the gripper, go back to putting the gripper above the lever handle.
    - When lever handle is not left of the robot's gripper and lever handle is not forward aligned with the robot's gripper, the robot should grab lever handle.
    If the lever handle is forward aligned with the gripper, try to pull it back.
    - When lever handle is forward aligned with the robot's gripper, the robot should pull lever handle.

The task `block-stack` requires the robot to pick up the block and place it on top of another block.
To pick up the block and place it on top of another block reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above block  2. Drop gripper around block  3. Close gripper around block  4. Put gripper on top of the block  5. Drop block
 