
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# peg-unstack: pull the peg out of the hole
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Pull peg out of the hole
    # First, put the gripper roughly above peg, so that we don't bump it while
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
    # We closed the gripper, and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the peg out of the hole.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.slide("peg out of hole")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around the door handle