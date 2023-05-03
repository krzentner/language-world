# Steps:
    #  1. Move gripper to left of puck and wall
    #  2. Move gripper down to above puck
    #  3. Drop gripper around puck
    #  4. Close gripper around puck
    #  5. Move puck up and over the wall to the goal
    # First, move the gripper to the left of the puck and wall so that we can
    # approach the puck from the open side.
    if check("the robot's gripper is not left of the puck and wall"):
        robot.move("gripper to left of puck and wall")
    # Once the gripper is left of the puck and wall, move it down to above the
    # puck so that we can grab it.
    if check("the robot's gripper is left of the puck and wall and the robot's gripper is not above puck"):
        robot.move("gripper down to above puck")
    # Once the gripper is above the puck, drop it around the puck.
    if check("the robot's gripper is above puck and the robot's gripper is not around the puck"):
        robot.drop("gripper around puck")
    # With the gripper around the puck, try to close it around the puck to grab
    # it.
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # If we closed the gripper around the puck, move it up and over the wall to
    # the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around puck and the puck is above the wall"):
        robot.place("puck at goal")