# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the thermos with the target location
    #  4. Use the stick to pull the thermos to the target location
    # First, put the gripper roughly above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around the stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around the stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we
    # grabbed it. Check if the gripper is around the stick before proceeding.
    if check("the robot's gripper is around the stick"):
        # Check if the thermos is to the left of the stick and aligned in the same direction
        if check("the thermos is to the left of the stick and the robot's gripper is aligned with the stick"):
            # Align the gripper with the thermos
            robot.align("gripper to thermos")
        # Check if the thermos is to the right of the stick and aligned in the same direction
        elif check("the thermos is to the right of the stick and the robot's gripper is aligned with the stick"):
            # Align the gripper with the thermos
            robot.align("gripper to thermos")
            # If the thermos is not already touching the stick, move it toward the stick
            if check("the thermos is not in contact with the stick"):
                robot.slide("the thermos towards the stick")
        # Check if the thermos is forward aligned with the stick
        elif check("the thermos is forward aligned with the stick"):
            # If the thermos is not in contact with the stick, move it towards the stick
            if check("the thermos is not in contact with the stick"):
                robot.slide("the thermos towards the stick")
        # If the thermos is not aligned with the stick, move it to the left/ right side of the stick
        else:
            robot.move("the thermos to the left/ right side of the stick")
        
        # If the thermos