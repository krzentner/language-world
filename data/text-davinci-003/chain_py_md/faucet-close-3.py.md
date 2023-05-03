

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet lever
    #  2. Grip faucet lever horizontally
    #  3. Turn faucet right until closed
    # First, put the gripper above the faucet lever.
    if check("the robot's gripper is not vertically aligned with faucet lever"):
        robot.put("gripper above faucet lever")
    # If the faucet lever isn't left of the gripper, grab it and turn it left
    # until it's lined up
    if check("the faucet lever is not left of the robot's gripper and the robot's gripper is not forward aligned with the faucet lever"):
        robot.grab("faucet lever horizontally")
    # Once the gripper is forward aligned with the faucet lever, turn the faucet
    # right until it's closed.
    if check("the robot's gripper is forward aligned with the faucet lever"):
        robot.turn("faucet right until closed")