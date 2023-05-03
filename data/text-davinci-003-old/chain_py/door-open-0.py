
    # Steps:
    #  1. Put the gripper above the door handle
    #  2. Drop the gripper around the door handle
    #  3. Pull open the door
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")