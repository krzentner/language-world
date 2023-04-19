# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("the gripper above the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("the gripper around the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("the gripper around the cube")
    if check("the robot's gripper is above the cube and the cube is below the robot's gripper"):
        robot.lift("the cube off the surface")
    if check("the robot's gripper is not above the target location"):
        robot.reach("the target location")
    if check("the robot's gripper is above the target location and the cube is not above the target location"):
        robot.drop("the gripper above the target location")
    if check("the gripper is around the target location and the cube is not touching sides of the gripper"):
        robot.push("the cube into the target location")