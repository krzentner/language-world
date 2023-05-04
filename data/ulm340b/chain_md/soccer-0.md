
    Steps:  1. Put gripper above soccer ball  2. Push gripper into top of soccer ball  3. Slide soccer ball to goal
    The soccer ball can be pushed in a similar way to sliding the puck. Because the soccer ball is larger, we don't have to be as careful when trying to slide it.
    - When the robot's gripper is not vertically aligned with soccer ball, the robot should put gripper above soccer ball.
    If the soccer ball is above the gripper as seen from above, put the gripper down around the soccer ball.
    - When the robot's gripper is vertically aligned with the soccer ball, the robot should push gripper into the soccer ball.
    When the gripper is near the soccer ball, the ball is probably trapped. Close the gripper to be sure and push the ball to the goal.
    - When the robot's gripper is near the soccer ball, the robot should slide soccer ball to goal.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Move the robot's gripper roughly towards the door handle  2. Push the door closed
    Because the door is large and the gripper just needs to hit it, not grab it, just point the gripper roughly towards the door handle and push.
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
    If the gripper is near the door handle, push the door closed.
    - When the robot's gripper is near door handle, the robot should push door closed.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Drop the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
  