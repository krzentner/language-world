
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    # Because we are holding the gripper open to grab the peg, use the
    # front-aligned condition.
    if check("the robot's gripper is open and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long as the gripper is still mostly around the peg, pull it out of the
    # hole.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.pull("peg out of hole")

# peg-insert-vertical: grab the peg and insert it into the hole from the top
def peg_insert_vertical(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    # Because we are holding the gripper open to grab the peg, use the
    # front-aligned condition.
    if check("the robot's gripper is open and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole"):
        robot.align("peg to