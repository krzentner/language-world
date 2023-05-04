
    # Steps:
    #  1. Put gripper vertically aligned with the faucet
    #  2. Turn the faucet to the right
    #  3. Turn the faucet further to the right
    # As long as the gripper isn't lined up vertically with the faucet, move the
    # gripper to line up with the faucet.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.move_gripper("vertically aligned with the faucet", close_gripper=True)
    # Now that the gripper is roughly aligned, turn the faucet to the right.
    if check("the faucet is left of the robot's gripper"):
        robot.move_gripper("around the faucet")
    # Now that the gripper is roughly around the faucet, rotate it more to the
    # right.
    if check("the faucet is right of the robot's gripper"):
        robot.move_gripper("above the faucet")

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper vertically aligned with the faucet
    #  2. Turn the faucet to the left
    #  3. Turn the faucet further to the left
    # As long as the gripper isn't lined up vertically with the faucet, move the
    # gripper to line up with the faucet.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.move_gripper("vertically aligned with the faucet", close_gripper=True)
    # Now that the gripper is roughly aligned, turn the faucet to the left.
    if check("the faucet is left of the robot's gripper"):
        robot.move_gripper("around the faucet")
    # Now that the gripper is roughly around the faucet, rotate it more to the
    # left.
    if check("the faucet is right of the robot's gripper"):
        robot.move_gripper("above the faucet")

# drawer-pull: pull the drawer open
def drawer_pull(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the