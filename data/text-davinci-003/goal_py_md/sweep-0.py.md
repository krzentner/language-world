

Steps:
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Move sideways to the target location

#sweep: grab the cube and move sideways it to the target location
#def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    #  2. Drop gripper around cube
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    #  3. Close gripper around cube
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.move_gripper("above the cube", close_gripper=True)
    #  4. Move sideways to the target location
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("sideways aligned with the target location")