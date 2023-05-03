# Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Pull the stick towards the thermos
    #  4. Place the thermos at goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we
    # grabbed it. Try to move the stick by pulling towards the thermos.
    # If we didn't grab the stick, we'll just go back to an earlier step.
    if check("the robot's gripper is above the stick and the robot's gripper is closed"):
        robot.pull("stick towards thermos")
    # If the stick is now on the thermos, place the thermos at the goal location.
    if check("the stick is on the thermos"):
        robot.place("thermos at goal")