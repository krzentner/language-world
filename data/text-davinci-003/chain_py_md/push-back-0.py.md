

Steps:
  1. Put gripper below puck
  2. Push gripper into the bottom of puck
  3. Slide puck to goal
 
The robot can slide the puck by trapping it by pushing up on it from
below and moving the gripper.

If the puck isn't above the gripper as seen from below, move the gripper
below the puck.

if check("the robot's gripper is not below puck and the robot's gripper is not vertically aligned with the puck"):
    robot.put("the gripper below the puck")

If the gripper is aligned with the puck but not near it, move the gripper
up to the puck to slide it.

if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
    robot.push("the gripper into the puck")

If the gripper is near the puck, we've probably trapped the puck and can
slide it to the target location.

Close the gripper to make sure we keep control of the puck.

if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
    robot.slide("the puck to the goal")