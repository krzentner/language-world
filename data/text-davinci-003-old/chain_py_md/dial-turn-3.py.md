

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Close gripper around the dial
    #  4. Rotate the dial with the gripper
    # We need to put the gripper roughly above the dial before we can grab it, 
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not roughly above dial"):
        robot.put("gripper above dial")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("gripper is almost aligned with dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # As long as the gripper is still aligned with the dial and the gripper is
    # open, we can grab the dial by closing the gripper.
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    # We should have grabbed the dial now. 
    # Now we can rotate the dial by turning the gripper.
    if check("the robot's gripper is around dial and the robot's gripper is closed"):
        robot.turn("gripper to rotate the dial")