
    # Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Start pushing the faucet handle to the right
    #  3. Push the faucet handle to the right harder
    # If the faucet handle is left of the robot's gripper, we should move the
    # gripper near the faucet handle to start pushing
    if check("the robot's gripper is not near faucet handle and the faucet handle is left of the robot's gripper"):
        robot.move("gripper to right of faucet handle")
    # If the robot's gripper is near the faucet handle we can probably push the
    # faucet handle now.
    if check("the robot's gripper is near faucet handle"):
        robot.push("faucet handle to the right")
    # If the faucet handle is starting to be in front of the robot's gripper,
    # push harder.
    if check("the robot's gripper is in front of faucet handle"):
        robot.push("faucet handle to the right harder")

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Start pushing the faucet handle to the left
    #  3. Push the faucet handle to the left harder
    # If the faucet handle is right of the robot's gripper, we should move the
    # gripper near the faucet handle to start pushing
    if check("the robot's gripper is not near faucet handle and the faucet handle is right of the robot's gripper"):
        robot.move("gripper to left of faucet handle")
    # If the robot's gripper is near the faucet handle we can probably push the
    # faucet handle now.
    if check("the robot's gripper is near faucet handle"):
        robot.push("faucet handle to the left")
    # If the faucet handle is starting to be in front of the robot's gripper,
    # push harder.
    if check("the robot's gripper is in front of faucet handle"):
        robot.push("faucet handle to the left harder")

# door-close: pull the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above