# Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # Once the gripper is above the handle, we should be able to grab the handle
    # by moving the gripper down around it.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, we can just pull up on the handle.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")