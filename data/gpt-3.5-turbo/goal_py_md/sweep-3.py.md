# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the side
    #  4. Move the cube to the target location
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, we can grab it by closing the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("to the side of the cube")
    # If the cube is sideways to the gripper, move it to the target location.
    if check("the robot's gripper is to the side of the cube and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")