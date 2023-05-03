# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move gripper and cube towards lower edge of the pan
    #  5. Slide cube towards the target location
    #  6. Drop the cube at the target location
    # First, put the gripper roughly above the cube, so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the lower edge of the pan")
    # If the gripper is aligned with the lower edge of the pan, move the gripper and the cube towards the target location.
    if check("the robot's gripper is horizontally aligned with the lower edge of the pan"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, slide the cube towards the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("dropped at the target location")