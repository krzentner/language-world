
    # Steps:
    #  1. Line up the gripper above the wrench and peg as viewed from above
    #  2. Push down on the wrench to try to remove it from the peg
    #  3. Grab the wrench
    #  4. Pull the wrench off the peg
    # First, we have to get the gripper above the wrench, or we'll just bump the
    # wrench off the table instead of pushing it down.
    if check("the robot's gripper is not vertically aligned with wrench and peg and the robot's gripper is not above wrench and peg"):
        robot.put("gripper above wrench and peg")
    # Since the gripper is vertically aligned with the wrench and peg, we can
    # push down on the wrench.
    # This should push the wrench off the peg.
    if check("the robot's gripper is vertically aligned with wrench and peg"):
        robot.push("gripper into wrench and peg")
    # If the gripper is in front of the wrench and peg, that means we've probably
    # pushed the wrench off the peg and can grab the wrench.
    if check("the robot's gripper is in front of wrench and peg"):
        robot.grab("wrench")
    # If the robot's gripper is in front of the wrench, we can pull the wrench
    # off the peg.
    if check("the robot's gripper is in front of wrench"):
        robot.pull("wrench off of peg")

# peg-insert-front: grab the peg and insert it into the hole in front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg forwards into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.