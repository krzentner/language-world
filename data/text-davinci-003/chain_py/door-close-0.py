
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push door closed
    # We need to put the gripper almost above the door handle to get the best
    # angle to push it.
    if check("the robot's gripper is not almost vertically aligned with the door handle and the robot's gripper is below the door handle"):
        robot.put("the gripper above the door handle")
    # As long as the gripper is close to being aligned with the door handle,
    # closing it should align it.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("the gripper around the door handle")
    # As long as the gripper is still aligned with the door handle, it's being
    # closed, so keep pushing.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed to goal")