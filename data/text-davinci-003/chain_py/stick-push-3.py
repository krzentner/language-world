
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to the thermos
    #  5. Push the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper is not around the stick, move it around the stick.
    if check("the gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # If we've closed the gripper, we've probably grabbed the stick.
    # Move the stick to the thermos.
    if check("the robot's gripper is closed and the stick is not near thermos"):
        robot.place("stick near thermos")
    # We placed the stick near the thermos, so try to push it toward the target
    # location.
    if check("the stick is near thermos"):
        robot.push("thermos toward goal")