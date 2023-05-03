# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move gripper to the side
    #  4. Move the gripper towards the target location
    #  5. Release the cube
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Once the gripper is above the cube, grab it.
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Move the gripper to the side of the cube.
    if check("the robot's gripper is not sideways aligned with the cube"):
        robot.move_gripper("sideways aligned with the cube")
    # Move the gripper towards the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Release the cube.
    if check("the cube is held by the robot's gripper"):
        robot.move_gripper("above the target location", close_gripper=False)