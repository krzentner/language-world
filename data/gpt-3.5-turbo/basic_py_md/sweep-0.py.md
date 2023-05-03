# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    if check("the robot's gripper is not vertically aligned with the cube and the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.grab("cube")
    if check("the robot's gripper is around the cube and the robot's gripper is not aligned with the target location"):
        robot.move("gripper to the left of the target")
    if check("the robot's gripper is to the left of the target location"):
        robot.slide("the cube to the right")
    if check("the cube is at the target location"):
        robot.release("cube")