# Steps:
    #  1. Put gripper above plate
    #  2. Lower gripper and grasp plate
    #  3. Move the plate back along the surface to its original position
    # First, put the gripper above the plate
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Lower the gripper and grasp the plate
    if check("the robot's gripper is above the plate" and "the robot's gripper is not holding the plate"):
        robot.move_gripper("on top of the plate", close_gripper=True)
    # Move the plate back to the target location
    if check("the robot's gripper is holding the plate" and "the plate is not at the target location"):
        robot.move_gripper("near the target location")