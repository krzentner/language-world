# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("the gripper above the cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near the cube"):
        robot.push("the gripper into the cube")
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.grab("the cube")
    if check("the cube is in the robot's gripper"):
        robot.move("the gripper to the side")
    if check("the cube is in front of the target location"):
        robot.push("the cube towards the target")
    if check("the cube is at the target location"):
        robot.drop("the cube")