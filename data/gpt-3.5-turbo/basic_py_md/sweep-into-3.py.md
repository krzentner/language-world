# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not above the cube and the gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the gripper is vertically aligned with the cube and the gripper is not around the cube"):
        robot.drop("gripper around cube")
    if check("the gripper is around the cube and the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location and the cube is below the robot's gripper"):
        robot.slide("cube into target location")
    if check("the cube is at the target location"):
        robot.release("cube")