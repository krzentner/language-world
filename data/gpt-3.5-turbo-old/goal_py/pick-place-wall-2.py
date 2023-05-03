# Steps:
    #  1. Put gripper above puck
    #  2. Check if there is a wall in the way
    #  3. If there is a wall, move the gripper to a different location on the same side of the wall
    #  4. Drop gripper around puck
    #  5. Close gripper around puck
    #  6. Move puck to goal
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Check if there is a wall in the way of the gripper and the puck.
    if check("there is a wall between the robot's gripper and the puck"):
        # If there is a wall, move the gripper to a different location on the
        # same side of the wall.
        robot.move_gripper("to a different location on the same side of the wall")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")