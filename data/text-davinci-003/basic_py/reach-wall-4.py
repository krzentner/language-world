
    if check("the robot's gripper is not horizontally aligned and is not above the wall"):
        robot.align("gripper to wall")
    if check("the robot's gripper is horizontally aligned and is above the wall and the robot's gripper is not above the target location"):
        robot.drop("gripper over target location over wall") 
    if check("the robot's gripper is above the target location"):
        robot.reach("to goal")