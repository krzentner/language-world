# Steps:
    #  1. Put gripper around the handle from the side
    #  2. Pull the handle upwards
    # Move the gripper around the handle from the side.
    if check("the robot's gripper is not around handle from the side"):
        robot.move("gripper around handle from the side")
    # Once the gripper is around the handle from the side, pull it upwards.
    if check("the robot's gripper is around handle from the side"):
        robot.pull("handle upwards")