To slide the puck to the target location with a small wall in the way reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Check if a wall is in the way  4a. If a wall is not in the way, slide the puck to goal  4b. If a wall is in the way, move the gripper to the other side of the wall  5. Slide the puck to the goal
First, put the gripper above the puck and then move the gripper down to the puck while checking if a wall is in the way.
    - When the robot's gripper is not above the puck or the robot's gripper is not aligned horizontally with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is aligned horizontally with the puck and the robot's gripper is not near the puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and we can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should check if a wall is in the way. If a wall is not in the way, the robot should slide the puck to the goal.
    If a wall is in the way, move the gripper to the other side of the wall and then slide the puck to the goal by pushing it with the gripper.