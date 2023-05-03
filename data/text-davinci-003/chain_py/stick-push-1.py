
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to thermos
    #  5. Move stick so it pushes thermos
    # First, put the gripper roughly above the stick, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the stick to underlying the thermos.
    if check("the robot's gripper is above the stick and the robot's gripper is closed"):
        robot.place("stick under thermos")
    # Now that the stick is positioned underneath the thermos, we can start
    # pushing the thermos by moving the stick.
    if check("the stick is stuck between the thermos and the goal"):
        robot.push("the stick to move the thermos to the goal")