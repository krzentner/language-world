  


# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around cube"): 
        robot.grab("cube")
    if check("the robot's gripper is around cube and the cube is not above the target"):
        robot.slide("cube to target")
    if check("the cube is above the target"):
        robot.release("cube at target")