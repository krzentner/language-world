
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube and the cube is above the gripper,
    # put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open and the cube is above the robot's gripper"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube, we've probably grabbed it and can move it
    # to the target location.
    if check("the robot's gripper is around the cube and the cube is above the robot's gripper"):
        robot.move_gripper("near the target location", close_gripper=True)

# sweep-into-goal: sweep the cube into the bin
def sweep_into_goal(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube and the cube is above the gripper,
    # put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open and the cube is above the robot's gripper"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube, we've probably grabbed it and can move it
    # to the target location.
    if check("the robot's gripper is around the cube and the cube is above the robot's gripper")