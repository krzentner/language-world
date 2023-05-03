
    # Steps:
    #  1. Put gripper right of door handle
    #  2. Push door closed
    # First, place the gripper just past the door handle, so that we can push
    # against it.
    if check("door handle is left of the robot's gripper and the robot's gripper is not right of door handle"):
        robot.put("gripper right of door handle")
    # As long as the gripper is past the door handle, just keep pushing.
    if check("the robot's gripper is to the right of the door handle"):
        robot.push("door closed")