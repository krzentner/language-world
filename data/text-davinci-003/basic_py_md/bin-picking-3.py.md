 

If check("the robot's gripper is not near the cube"):
    robot.reach("to cube")
if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
    robot.put("gripper above the cube")
if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near the cube"):
    robot.close("gripper around the cube")
if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
    robot.lift("the cube from the bin")
if check("the robot’s gripper is above the cube and the robot’s gripper is closed"):
    robot.put("cube in target bin")