
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Lift the peg out
    #  5. Move peg to goal
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not forward aligned with peg"):
        robot.grab("peg")
    # If the gripper is around the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is forward aligned with peg and the robot's gripper is open"):
        robot.lift("peg out of hole")
    # We closed the gripper, and the peg is still around the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.place("peg at goal")

# insert: put the peg into the hole
def insert(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot