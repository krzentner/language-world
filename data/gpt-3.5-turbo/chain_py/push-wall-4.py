# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck until it reaches the wall
    #  4. Move gripper to the other side of the puck
    #  5. Push puck until it reaches the goal
    # Like push, we first need to position the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above the puck")
    # Next, we need to close the gripper around the puck and move it until it reaches the wall.
    # Make sure that the gripper is not slipping by applying enough force to the puck.
    if check("the robot's gripper is open and the gripper is not near the wall"):
        robot.drop("gripper around puck")
        while not check("puck has reached the wall"):
            robot.slide("puck")
            robot.apply_force("gripper", 1)
    # Once the puck has reached the wall, we need to move the gripper to the other side of the puck.
    if check("the gripper is not on the other side of the puck"):
        robot.move("gripper to other side of the puck")
    # Finally, we can push the puck until it reaches the goal.
    if check("the gripper is on the other side of the puck"):
        while not check("puck has reached the goal"):
            robot.push("puck")
            robot.apply_force("gripper", 1)