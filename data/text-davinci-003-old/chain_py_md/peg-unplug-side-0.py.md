

Steps:
1. Put gripper above the peg
2. Grab the peg with the gripper
3. Move the peg sideways
4. Pull the peg out

# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the peg sideways
    #  4. Pull the peg out
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # Once the gripper is lined up above the peg, we should be able to
    # grab the peg by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.grab("peg")
    # Now, we should be able to move the peg sideways
    if check("the robot's gripper is around peg and the peg is not sideways to the hole"):
        robot.slide("peg sideways")
    # When the peg is sideways to the hole, we can pull it out.
    if check("the peg is sideways to the hole"):
        robot.pull("peg out")