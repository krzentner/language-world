

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Place the robot's gripper above the faucet
    #  2. Place the gripper around the faucet
    #  3. Turn the faucet left
    # First, put the gripper roughly above the faucet so that we don't bump it 
    # while trying to grab it.
    if check("the robot's gripper is not above the faucet"):
        robot.move_gripper("above the faucet")
    # If the gripper isn't around the faucet, put it around the faucet.
    if check("the robot's gripper is not around faucet and the robot's gripper is open"):
        robot.move_gripper("around the faucet", close_gripper=True)
    # If the gripper is around the faucet, turn the faucet left.
    if check("the robot's gripper is around faucet and the faucet is not facing left"):
        robot.move_gripper("left of the faucet")