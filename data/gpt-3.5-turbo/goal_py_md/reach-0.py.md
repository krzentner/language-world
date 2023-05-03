# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Put gripper horizontally aligned with the target location
    #  2. Move gripper down to target location
    # The robot needs to simply reach out to the target location without grabbing anything.
    # If the gripper is not horizontally aligned to the target location, move it there.
    if check("the robot's gripper is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the gripper is horizontally aligned to the target location but not at the right height, move it down.
    if check("the robot's gripper is not almost vertically aligned with the target location"):
        robot.move_gripper("almost vertically aligned with the target location")