# Steps:
    #  1. Put gripper above the door handle
    #  2. Move the gripper to the target location while pushing the door closed
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle")
    # Once the gripper is above the door handle, move the gripper to the target
    # location while pushing the door closed.
    if check("the robot's gripper is above the door handle"):
        robot.move_gripper("near the target location", push=True)