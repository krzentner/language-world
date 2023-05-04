
To grab the cube and move sideways it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the cube  2. Drop gripper around the cube  3. Close gripper around the cube  4. Move the cube to the goal
    Put the gripper above the cube.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    If the gripper is not around the cube and the gripper is open, we should drop the gripper around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is near the cube and closed, we've probably got a grasp.
    - When the robot's gripper is above the cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location and the robot's gripper is open

The task `insert-peg-hole-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    Put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    If the