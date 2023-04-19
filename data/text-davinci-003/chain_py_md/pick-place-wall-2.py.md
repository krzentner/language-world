

Steps:
 1. Put gripper right of puck and wall
 2. Drop gripper around puck
 3. Slide puck away from wall and to side of wall
 4. Close gripper around puck
 5. Move puck around wall to goal

First, we need to put the gripper near the puck but not too close to the wall.
if check("the robot's gripper is not between the puck and the wall and the robot's gripper is not horizontally aligned with the puck"):
    robot.put("gripper right of puck and wall")

Once the gripper is between the puck and the wall, we can move the gripper to the side of pucks, to grab it.
if check("the robot's gripper is between the puck and wall and the robot's gripper is not around puck"):
    robot.drop("gripper around puck")

Next, we can slide the puck away from the wall and to the side of the wall.
if check("the puck is near the wall and the robot's gripper is around puck"):
    robot.slide("puck away from wall and to side of wall")

Now that the puck is in a position we can close the gripper to hold it.
if check("the puck is to the side of the wall and the robot's gripper is open"):
    robot.close("gripper around puck")

Finally, we can move the puck around the wall to the goal.
if check("the robot's gripper is closed around the puck and the goal is to the side of the wall"):
    robot.move("puck around wall to goal")