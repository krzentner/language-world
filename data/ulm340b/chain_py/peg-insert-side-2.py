
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Slide the peg towards the hole
    #  5. Align the gripper with the hole from the side
    #  6. Push the peg into the hole
    # First, put the gripper roughly above the peg so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Now that we're holding the peg, try to slide it into the hole.
    # We want the gripper to be mostly near the hole but mostly not near the
    # back of the hole.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is open and the peg is above the hole"):
        robot.slide("peg towards hole")
    # If the gripper is not lined up with the hole from the side, put it there.
    if check("the robot's gripper is not side aligned with hole and the peg is above the hole"):
        robot.put("gripper side aligned with hole")
    # If the gripper is aligned with the hole, push the peg in.
    if check("the robot's gripper is side aligned with hole and the peg is above the hole"):
        robot.push("peg into hole")

# switch-right: pull the switch to the right
def switch_right(robot):
    # Steps:
    #  1. Put gripper below switch
    #  2. Close gripper around switch
    #  3. Pull switch right
   