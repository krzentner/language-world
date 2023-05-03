
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move puck to predetermined coordinates
    #  4. Release puck
    #  We should start by moving the gripper above the puck so that we can grab it.
    if check("the robot's gripper is not aobve the puck"):
        robot.put("gripper above puck")
    # Close the gripper to scoop up the puck.  We don't have to worry about
    # lining the gripper up with the puck, since we just want to grab it.
    if check("the robot's gripper is above the puck and the puck is below the robot's gripper"):
        robot.grab("the puck")
    # Move the puck to the predetermined coordinates.  Again, we don't have to
    # worry about lining the gripper up with the puck
    if check("the robot's gripper is near the predetermined coordinates"):
        robot.move("puck to loaction with gripper")
    # Release the puck.
    if check("the puck is in the predetermined coordinates"):
        robot.release("the puck")