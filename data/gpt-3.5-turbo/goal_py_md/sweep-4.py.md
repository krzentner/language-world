# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Next, move the gripper near the cube and grab it.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube, move the cube to the target location by moving the gripper sideways.
    if check("the robot's gripper is around the cube and the robot's gripper is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")