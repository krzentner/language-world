
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Lift the mug
    #  4. Move mug to goal
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # When the gripper is above the handle, drop it around the handle to grab it.
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # We should be able to lift the mug now that it's been grabbed.
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.lift("mug")
    # Now that the mug is lifted, we can move it.
    if check("the mug is not in the goal area and the robot's gripper is closed and the robot's gripper is around handle"):
        robot.move("mug to goal")