
    # Steps:
    #  1. Put gripper front of the faucet handle
    #  2. Push down on the faucet handle
    #  3. Twist the faucet handle left
    # We can turn the handle by pushing it sideways, so we want the gripper to be
    # front of the handle.
    # If the gripper isn't lined up front of the handle, line it up.
    if check("gripper is not forward aligned with faucet handle"):
        robot.put("gripper front of the faucet handle")
    # Now that the gripper is lined up, push down the handle.
    if check("the robot's gripper is forward aligned with the faucet handle"):
        robot.push("down on faucet handle")
    # Finally, twist the handle to the left.
    if check("the robot's gripper is pushing down on the faucet handle"):
        robot.twist("faucet handle left")