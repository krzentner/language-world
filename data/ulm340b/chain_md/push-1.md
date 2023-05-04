:
    Steps:  1. Push puck towards goal
    Since the goal is on the same horizontal surface as the puck, and the puck is not attached to anything, we can just push it there.
    - When the puck is not near goal, the robot should push puck to goal.
    (if needed): To push puck to goal reliably, the robot should perform the following steps:
        Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Push puck towards goal  4. Move puck to goal
        First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
        - When the robot's gripper is not above the puck, the robot should place gripper above puck.
        If the gripper isn't around the puck, put it around the puck.
        - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
        As long as the gripper is around the puck, we can probably slide it by pushing.
        - When the robot's gripper is around puck, the robot should slide puck to goal.
        If the gripper is near the puck and we were sliding it, but then the puck stops sliding, maybe we should just pick it up and place it at the goal.
        - When the robot's gripper is near puck and the robot's gripper is closed, the robot should place puck at goal.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Insert the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    -