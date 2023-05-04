
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet open
    # We need to put the gripper above the faucet handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.put("gripper around faucet handle")
    # Once the gripper is around the faucet handle, we can just turn it open.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("the faucet open")

# peg-unstack-side: grab the top peg and pull the pegs apart to the side
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above top peg
    #  2. Drop gripper around top peg
    #  3. Pull top peg away
    # First, put the gripper above top peg.
    if check("the robot's gripper is not above the top peg"):
        robot.put("gripper above top peg")
    # If the top peg is not around the gripper, put it around the top peg.
    if check("the top peg is not around the robot's gripper and the robot's gripper is open"):
        robot.drop("gripper around top peg")
    # If the top peg is around the gripper, just pull the pegs apart.
    if check("the top peg is around the robot's gripper and the robot's gripper is closed"):
        robot.unstack("the pegs sideways")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close grip