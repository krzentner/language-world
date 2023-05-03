# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to the right
    #  5. Move cube to the left
    #  6. Move cube to the right
    #  7. Move cube to the target location
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("right of the cube")
    if check("the robot's gripper is near the right of the cube and the cube is not at the right edge"):
        robot.move_gripper("left of the cube")
    if check("the robot's gripper is near the left of the cube and the cube is at the right edge"):
        robot.move_gripper("right of the cube")
    if check("the robot's gripper is right of the cube and the cube is at the right edge"):
        robot.move_gripper("near the target location")