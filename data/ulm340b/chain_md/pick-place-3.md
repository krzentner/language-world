
    Steps:  1. Put gripper above puck  2. Grab puck with gripper  3. Put gripper above goal  4. Hold the puck over the goal
    The robot can pick up the puck by grasping it with the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to grasp it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should grab the puck.
    Now that the robot is holding the puck, we can move the robot's gripper to the target location. If the target location isn't below the gripper as seen from above, move the gripper above the target location.
    - When the robot's gripper is not above the goal and the robot's gripper is not vertically aligned with the goal, the robot should put the gripper above the goal.
    Now that the robot is near the target location, let's hold the puck there.
    - When the robot's gripper is near the goal, the robot should hold the puck at the goal.


The task `door-lock-insert` requires the robot to insert the peg into the hole of the door lock from above.
To insert the peg into the hole of the door lock from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Insert the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is