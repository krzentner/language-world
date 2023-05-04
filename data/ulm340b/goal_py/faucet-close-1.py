
    # Steps:
    #  1. Put gripper below the faucet handle
    #  2. Start pushing against the faucet handle to turn off the faucet
    #  3. Push the faucet off harder
    # First, put the gripper right under the faucet handle.
    if check("the robot's gripper is not below the faucet handle"):
        robot.move_gripper("below the faucet handle")
    # If the gripper is already near the faucet handle, we can probably push the
    # faucet off by moving the gripper right.
    if check("the robot's gripper is not forward aligned with the faucet handle"):
        robot.move_gripper("in front of the faucet handle")
    # If the gripper is in front of the faucet handle, push it harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.move_gripper("above the faucet handle")

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Start pushing against the faucet handle to turn on the faucet
    #  3. Push the faucet on harder
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper is already near the faucet handle, we can probably turn on
    # the faucet by pushing the gripper left.
    if check("the robot's gripper is not forward aligned with the faucet handle"):
        robot.move_gripper("in front of the faucet handle")
    # If the gripper is in front of the faucet handle, push it harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.move_gripper("right of the faucet handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large