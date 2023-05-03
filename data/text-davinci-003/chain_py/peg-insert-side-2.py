
    # Steps:
    #  1. Put gripper forward of peg
    #  2. Drop gripper around peg
    #  3. Close gripper
    #  4. Move peg to hole
    # If the gripper isn't near the peg, move it to the peg.
    if check("the robot's gripper is not near the peg"):
        robot.grab("peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the peg to the hole.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near peg and the robot's gripper is closed"):
        robot.slide("peg to hole")