
    # Steps:
    #  1. Put gripper vertically aligned with faucet handle
    #  2. Move gripper around faucet handle
    #  3. Turn faucet left
    # If the gripper isn't vertically aligned with the faucet handle, we should
    # put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle", close_gripper=True)
    # If the faucet handle is right of the gripper, we should move the gripper
    # left around the faucet handle.
    if check("the faucet handle is right of the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the faucet handle")
    # If the gripper is around the faucet handle as seen from the top, we should
    # be able to turn the faucet handle left.
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.move_gripper("around the faucet handle")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper vertically aligned with faucet handle
    #  2. Move gripper around faucet handle
    #  3. Turn faucet right
    # First, we need to put the gripper above the faucet handle.
    # It is important to line the robot's gripper up with faucet handle before
    # reaching for the faucet, since the robot's gripper isn't very wide.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle", close_gripper=True)
    # If the faucet handle is left of the gripper, we should move the gripper
    # left around the faucet handle.
    if check("the faucet handle is left of the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the faucet handle")
    # If the gripper is around the faucet handle as seen from the top, we should
    # be able to turn the faucet handle right.
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.move_gripper("around the faucet handle")

# peg-