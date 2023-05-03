# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above the cube")
    if check("the robot's gripper is vertically aligned with the cube and the cube is not in the gripper"):
        robot.grab("the cube")
    if check("the robot's gripper is holding the cube and the robot is not aligned with the target location"):
        robot.move("the gripper to the side of the target location")
    if check("the robot's gripper and the cube are aligned with the target location"):
        robot.slide("the cube sideways to the target location")