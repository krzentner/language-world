
    Steps:  1. Go to the target location
    We just need to reach the target location.
    - When the robot's gripper is not near the target location, move the robot's gripper until the robot's gripper is near the target location

The task `c-shape-insert` requires the robot to pick up the c-shape and insert it into the goal hole.
To pick up the c-shape and insert it into the goal hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the c-shape  2. Grab the c-shape with the gripper  3. Line the c-shape up with the hole  4. Insert the c-shape sideways into the hole
    First, put the gripper above the c-shape.
    - When the robot's gripper is not above the c-shape, move the robot's gripper until the robot's gripper is above the c-shape
    As long the gripper is around the c-shape and the c-shape isn't lined up with the hole, line up the c-shape with the hole.
    - When c-shape is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the c-shape and the robot's gripper is closed
    If the c-shape is lined up with the hole to the side, insert it.
    - When the robot's gripper is around the c-shape and the c-shape is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is horizontally aligned with hole

The task `peg-insert-front` requires the robot to grab the peg and insert it into the hole from the front.
To grab the peg and insert it into the hole from the front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Push the peg forwards into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes behind the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is behind the robot's gripper and the peg is not forward aligned with the robot'