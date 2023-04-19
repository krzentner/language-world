
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Move gripper around the faucet handle
    #  3. Turn the faucet left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper is above the faucet handle, move it around the faucet
    # handle.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.move("gripper around faucet handle")
    # If the gripper is around the faucet handle, turn it left.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Move gripper around the faucet handle
    #  3. Turn the faucet right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper is above the faucet handle, move it around the faucet
    # handle.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.move("gripper around faucet handle")
    # If the gripper is around the faucet handle, turn it right.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet right")