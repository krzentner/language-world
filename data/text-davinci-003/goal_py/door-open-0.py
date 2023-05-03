
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull open the door
    # Put the gripper above the door handle before trying to grab it.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # If the gripper is above the door handle, we should be able to grab it
    # by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")