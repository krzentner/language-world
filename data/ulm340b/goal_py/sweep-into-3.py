
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube but not around it, drop the gripper
    # around the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("around the cube")

# sweep-onto: grab the cube and move it to the top of the target location
def sweep_onto(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube but not around it, drop the gripper
    # around the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
