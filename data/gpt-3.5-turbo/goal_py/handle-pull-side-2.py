# Steps:
    #  1. Put the gripper around the handle from the side
    #  2. Pull up the handle
    # Start by aligning the robot's gripper with the handle from the side.
    if check("the robot's gripper is not around the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is in the right position, move it around the handle to
    # grab it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # With the handle grabbed, pull it up to open the object.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")