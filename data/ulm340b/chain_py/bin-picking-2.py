
    # Steps:
    #  1. Put gripper above bin
    #  2. Drop gripper around bin
    #  3. Close gripper around bin
    #  4. Move bin to goal
    # First, put the gripper roughly above bin, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the bin"):
        robot.place("gripper above bin")
    # If the gripper isn't around the bin, put it around the bin.
    if check("the robot's gripper is not around bin and the robot's gripper is open"):
        robot.drop("gripper around bin")
    # If the gripper is near the bin and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near bin and the robot's gripper is open"):
        robot.close("gripper around bin")
    # We closed the gripper, and the bin is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the bin to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above bin and the robot's gripper is closed"):
        robot.place("bin at goal")

# bottle-open: pull open the bottle lid
def bottle_open(robot):
    # Steps:
    #  1. Put gripper near the bottle lid
    #  2. Put gripper around the bottle lid
    #  3. Pull the bottle lid up
    #  4. Pull the bottle lid further up
    # First, put the gripper roughly above bottle lid, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not near the bottle lid"):
        robot.move("gripper to bottle lid")
    # If the gripper isn't around the bottle lid, put it around the bottle lid.
    if check("the robot's gripper is not around bottle lid and the robot's gripper is open"):
        robot.drop("gripper around bottle lid")
    # If the gripper is near the bottle lid