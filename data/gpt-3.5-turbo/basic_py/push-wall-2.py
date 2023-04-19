if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
    robot.put("the gripper above the puck")
if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
    robot.push("the gripper into the puck")
if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
    if check("there is a wall in the way"):
        robot.slide("the puck to the left or right of the wall")
        robot.move("the gripper to the other side of the wall")
        robot.slide("the puck to the goal")
    else:
        robot.slide("the puck to the goal")