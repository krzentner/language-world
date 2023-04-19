# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift puck over wall
    #  5. Move puck to goal
    # First, put the gripper roughly above the puck and make sure that the wall is detected.
    if check("the robot's gripper is not above the puck or the wall is not detected"):
        robot.place("gripper above puck and detect the wall")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # Once we have the puck, raise it over the wall.
    if check("the robot's gripper is closed around the puck"):
        robot.lift("puck over the wall")
    # We lifted the puck over the wall, so now we can move it to the goal.
    if check("the puck is over the wall"):
        robot.place("puck at goal")