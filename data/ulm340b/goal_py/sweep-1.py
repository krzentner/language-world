
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move the cube to the target location
    #  5. Open gripper to release the cube
    # Put the gripper above the cube so we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is not around cube and the robot's gripper is closed"):
        robot.move_gripper("around the cube")
    # If the gripper is around the cube, move the cube to the target location
    if check("the robot's gripper is around cube"):
        robot.move_gripper("above the target location")

# grasp-pick-place: grab and move a cylinder
def grasp_pick_place(robot):
    # Steps:
    #  1. Put gripper above cylinder
    #  2. Drop gripper around cylinder
    #  3. Close gripper around cylinder
    #  4. Move cylinder to the target location
    #  5. Open gripper to release cylinder
    # Put the gripper above the cylinder so we don't bump it while trying to
    # grab it.
    if check("the robot's gripper is not above the cylinder"):
        robot.move_gripper("above the cylinder")
    # If the gripper isn't around the cylinder, put it around the cylinder.
    if check("the robot's gripper is not around cylinder and the robot's gripper is open"):
        robot.move_gripper("near the cylinder", close_gripper=True)
    # If the gripper is near the cylinder and open, maybe we can grab it by
    # closing the