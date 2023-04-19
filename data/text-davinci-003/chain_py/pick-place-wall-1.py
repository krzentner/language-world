
    # Steps:
    #  1. Put gripper above the wall
    #  2. Move gripper behind the wall
    #  3. Put gripper above puck
    #  4. Move gripper around the wall
    #  5. Drop gripper around puck
    #  6. Close gripper around puck
    #  7. Move puck to goal
    # If the gripper isn't above the wall, move it that way first.
    if check("the robot's gripper is not above the wall"):
        robot. place("gripper above wall")
    # If the gripper is above the wall, move the gripper behind the wall so the
    # wall doesn't block the gripper from reaching the puck.
    if check("the robot's gripper is above the wall"):
        robot.move("gripper behind wall")
    # Move the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # Move the gripper around the wall, aiming for the puck.
    if check("the robot's gripper is not near the puck and the robot's gripper is still behind the wall"):
        robot.move("gripper around wall")
    # Drop the gripper around the puck, then close the gripper around the puck.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
        robot.close("gripper around puck")
    # Move the puck to the goal.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("puck to goal")