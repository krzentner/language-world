# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is open and is above the cube"):
        robot.grab("cube")
    if check("the cube is above the target location and the gripper is closed around the cube"):
        robot.move("gripper to target location")
    if check("the gripper is above the target location and the cube is not in the gripper"):
        robot.drop("cube at target location")