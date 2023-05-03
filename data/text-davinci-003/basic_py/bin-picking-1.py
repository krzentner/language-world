
    if check("the robot's gripper is not vertically aligned with the cube"): 
        robot.put("gripper above cube")
    if check("the cube is not left of the robot's gripper and the cube is not forward aligned with the robot's gripper"): 
        robot.grab("cube")
    if check("the robot's gripper is near cube and the robot's gripper is not around cube"): 
        robot.grab("cube with the gripper")
    if check("the robot's gripper is around cube and the robot's gripper is not above bin"): 
        robot.move("above bin")
    if check("the robot's gripper is above bin and the robot's gripper is not above bin and the robot's gripper is open"): 
        robot.drop("cube into bin")