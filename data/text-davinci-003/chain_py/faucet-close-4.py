
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Move gripper around faucet handle
    #  3. Turn the faucet to the right
    # Put the gripper several decimeters above the faucet handle. This gives the
    # robots more freedom to move the gripper.
    if check("the robot's gripper is not well above the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper isn't around the faucet handle, move it around the handle.
    if check("the robot's gripper is well above the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.move("gripper around faucet handle")
    # If the gripper is around the faucet handle, we can start to turn it so
    # that it turns right.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("right")