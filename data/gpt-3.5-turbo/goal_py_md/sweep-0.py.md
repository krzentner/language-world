# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Lift the cube
    #  4. Move the cube sideways to the target location
    #  5. Lower the cube

    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Next, grab the cube with the gripper.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # After grabbing the cube, lift it.
    if check("the robot's gripper is around the cube and the robot's gripper is not lifted"):
        robot.move_gripper("lifted")
    # Move the cube sideways to the target location.
    if check("the robot's gripper is lifted and it is not sideways aligned with the target location"):
        robot.move_gripper("sideways aligned with the target location")
    # Finally, lower the cube.
    if check("the robot's gripper is sideways aligned with the target location and the robot's gripper is not lowered"):
        robot.move_gripper("almost vertical with the target location")