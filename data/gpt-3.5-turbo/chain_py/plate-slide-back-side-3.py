# Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Close gripper around plate
    #  4. Move plate back
    # First, position the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the gripper is not around the plate, move the gripper down and around
    # the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is around the plate, close it to hold onto it.
    if check("the robot's gripper is around plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # If the gripper is holding the plate and not aligned with the target
    # location, slide the plate towards the target location.
    if check("the robot's gripper is holding the plate and the plate is not aligned to the target location"):
        # We need to move the plate diagonally if it needs to slide sideways, so
        # first we check which way the target location is and move the gripper to
        # the opposite side of the plate (facing the same way) before trying to
        # slide it.
        # If the target location is to the right, move the gripper to the left of
        # the plate.
        if check("the target location is to the right of the plate and the robot's gripper is not left of the plate"):
            robot.move("gripper to left of plate (facing right)")
        # If the target location is to the left, move the gripper to the right of
        # the plate.
        elif check("the target location is to the left of the plate and the robot's gripper is not right of the plate"):
            robot.move("gripper to right of plate (facing left)")
        # Now slide the plate back towards the target location.
        robot.slide("plate back to target location")