
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Position stick in front of thethermos
    #  5. Push thermos with stick
    # Put the robot's gripper above the stick, so we don't knock it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the robot's gripper is around the stick, but open, close it.
    if check("the robot's gripper is around the stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We need the stick to be in front of the thermos before we can push it
    # with the stick.
    if check("the robot's gripper is closed and the stick is not positioned in front of the thermos"):
        robot.align("stick in front of thermos")
    # If the stick is in front of the thermos, we can try to push the thermos
    # with the stick.
    if check("the stick is positioned in front of the thermos"):
        robot.push("thermos with stick")