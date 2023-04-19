
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    # To close the door, put the gripper near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # Once the gripper is near the handle, just push the door closed.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("above the target location")