

Steps:
  1. Put gripper above wall
  2. Push gripper against the wall in desired shovelling direction
  3. Push puck until it is past the wall

First, put the gripper up above the wall and line it up with the shoving direction.
if check("the robot's gripper is not above the wall and the robot's gripper is not aligned with the shoving direction"):
    robot.put("gripper above wall")

Once lined up, push the beat by pushing the gripper against the wall.
if check("the robot's gripper is aligned with the shoving direction and the robot's gripper is not pushing against the wall"):
    robot.push("gripper against wall")

Once the beat is pushed past the wall, continue pushing it towards the goal.
if check("the puck is past the wall and the robot's gripper is pushing against the wall"):
    robot.push("puck towards goal")