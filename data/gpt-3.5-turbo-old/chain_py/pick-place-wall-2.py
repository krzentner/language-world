# Steps:
    #  1. Put gripper roughly above puck
    #  2. Move gripper to the side of the wall
    #  3. Put gripper above the puck again, on the other side of the wall
    #  4. Drop gripper around puck
    #  5. Close gripper around puck
    #  6. Move puck to goal
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # Move the gripper to the side of the wall.
    if check("the robot's gripper is not next to the wall"):
        robot.move("gripper to the side of the wall")
    # Move the gripper above the puck again, on the other side of the wall.
    if check("the robot's gripper is not above the puck on the other side of the wall"):
        robot.place("gripper above puck, on the other side of the wall")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")