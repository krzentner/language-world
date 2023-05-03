# Steps:
    #  1. Put gripper below faucet handle
    #  2. Grab faucet handle
    #  3. Turn handle left
    # First, put the gripper mostly below the faucet handle.
    if check("the robot's gripper is not mostly below the faucet handle"):
        robot.put("gripper below faucet handle")
    # As long as the gripper is mostly lined up, closing it should line it up
    # all the way.
    # Because the faucet handle is small and round, we should grip it tightly to
    # make sure it doesn't slip out of the gripper.
    if check("the robot's gripper is mostly below the faucet handle and the robot's gripper is open"):
        robot.grasp("faucet handle")
    # As long as the gripper is still below the faucet handle, turn the handle
    # to the left.
    if check("the robot's gripper is below the faucet handle"):
        robot.turn("faucet handle left")