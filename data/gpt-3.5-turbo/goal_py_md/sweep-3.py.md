# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Move gripper to the left until at the target location
    #  4. Release the cube
    # First we need to put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, we need to move it to the left
    # until it is at the target location.
    if check("the robot's gripper is around the cube and the gripper is not at the target location"):
        robot.move_gripper("to the left of the target location")
    # Once the gripper is at the target location, we can release the cube.
    if check("the robot's gripper is at the target location"):
        robot.move_gripper("above the target location", close_gripper=False)