
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift puck off wall
    #  5. Move puck to goal
    # Move the gripper above the puck and line it up so it can be grabbed.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, the puck is still near the gripper, and it's still
    # up against the wall, so lift the puck off of it.
    # This might be difficult if it doesn't have anything to slide back against.
    if check("the robot's gripper is closed around puck and the puck is up against wall"):
        robot.lift("puck off wall")
    # We probably lifted the puck off of the wall and it's near the gripper, so
    # try to move the puck to the goal.
    if check("the robot's gripper is closed around puck and the puck is not up against wall"):
        robot.place("puck at goal")