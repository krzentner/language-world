
    # Steps:
    #  1. Put gripper above the wall
    #  2. Put gripper above the puck
    #  3. Push gripper into top of puck
    #  4. Slide the puck to goal
    # First, lift the gripper up over the wall so that it can move the puck
    # without going over the wall.
    if check("the wall is above the robot's gripper"):
        robot.move_gripper("above the wall")
    # Then, put the gripper roughly above puck so that it can trap the puck
    # without moving the wall.
    if check("the robot's gripper is above the wall and the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Once the gripper is above the puck, trap it by pushing down on it and
    # sliding the puck to the target location.
    if check("the robot's gripper is above the puck and the puck is below the robot's gripper"):
        robot.move_gripper("near the target location", close_gripper=True)