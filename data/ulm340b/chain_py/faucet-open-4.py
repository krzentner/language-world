
    # Steps:
    #  1. Put gripper above faucet
    #  2. Grab the faucet
    #  3. Turn the faucet left
    # First, put the robot's gripper above the faucet.
    if check("the robot's gripper is not above faucet"):
        robot.put("gripper above faucet")
    # If the faucet handle is left of the gripper, go back to putting the
    # gripper above the faucet handle.
    if check("faucet is not left of the robot's gripper"):
        robot.grab("faucet")
    # The faucet handle is vertically aligned with the gripper and left of it,
    # so turn the faucet on.
    if check("faucet is left of the robot's gripper and the robot's gripper is vertically aligned with faucet"):
        robot.turn("faucet on")

# turn-on: turn the light switch on
def turn_on(robot):
    # Steps:
    #  1. Put gripper above light switch
    #  2. Grab the light switch
    #  3. Turn the light switch on
    # If the light switch handle is right of the robot's gripper, put the
    # gripper above the light switch handle.
    if check("the light switch is right of the robot's gripper"):
        robot.put("gripper above light switch")
    # Once the gripper is above the light switch handle, we should be able to
    # grab it by moving the gripper down around it.
    if check("the robot's gripper is above light switch and the robot's gripper is not around light switch"):
        robot.grab("light switch")
    # The light switch is already aligned with the gripper, so flip it on
    # immediately.
    if check("the robot's gripper is around light switch"):
        robot.flip("light switch on")

# peg-insert-side-long: grab the peg and insert it into the hole from the side
def peg_insert_side_long(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the