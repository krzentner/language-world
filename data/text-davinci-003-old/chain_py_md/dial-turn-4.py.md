

Steps: 
  1. Put gripper above dial
  2. Drop gripper around dial
  3. Rotate dial 

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Rotate dial 
    # First, put the gripper roughly above dial, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above dial"):
        robot.place("gripper above dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # If the gripper is near the dial and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    # We closed the gripper, and the dial is still near the gripper, so maybe we
    # grabbed it.
    # Try to rotate the dial.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is closed"):
        robot.turn("dial")