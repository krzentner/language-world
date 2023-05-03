
    if check("the robot's gripper is not near the cube"):
        robot.move("gripper near the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.grab("the cube")
    if check("the cube is in the robot's gripper"):
        robot.move("cube to goal")
    if check("the robot's gripper is near the goal"):
        robot.release("cube from gripper")