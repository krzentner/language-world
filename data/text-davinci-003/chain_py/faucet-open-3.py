
    # Steps:
    #  1. Put gripper above faucet
    #  2. Drop gripper around faucet
    #  3. Turn faucet left
    # We need to put the gripper above the faucet before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.place("gripper above faucet")
    # Once the gripper is lined up above the faucet, we should be able to grab
    # the faucet by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet and the robot's gripper is not around faucet"):
        robot.grab("gripper around faucet")
    # Once the gripper is around the faucet, turn it to the left to open it.
    if check("the robot's gripper is around faucet"):
        robot.turn("left")