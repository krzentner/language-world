
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Drop gripper around the wrench
    #  3. Move the wrench around the peg
    # First, put the gripper above the wrench, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is near the wrench and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    # We closed the gripper, and the wrench is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the wrench around the peg.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above the wrench and the robot's gripper is closed"):
        robot.move("wrench around peg")