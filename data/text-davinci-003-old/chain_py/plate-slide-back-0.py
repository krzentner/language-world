
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push plate back
    # First, move the gripper close to the plate so that we can start pushing it.
    if check("the robot's gripper is not close to the plate"):
        robot.put("gripper in front of plate")
    # If the gripper is close to the plate, push the plate back into the target
    # location.
    if check("the robot's gripper is close to the plate"):
        robot.push("plate back to target")