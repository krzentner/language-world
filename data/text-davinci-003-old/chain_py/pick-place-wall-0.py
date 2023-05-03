
    # Steps:
    #  1. Put gripper above the puck
    #  2. Move gripper above wall
    #  3. Put gripper around puck
    #  4. Close gripper around puck
    #  5. Move puck to goal
    # First, put the gripper above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # Then move the gripper above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.move("gripper above wall")
    # Now that the wall is out of the way, the same steps for pick_place apply.
    if check("the robot's gripper is above puck and the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")