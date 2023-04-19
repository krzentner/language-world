# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # First, put the gripper above the puck, so that we don't bump into the wall
    # while trying to move the puck later.
    if check("the robot's gripper is not above the puck and the puck is not behind the wall"):
        robot.place("gripper above puck")
    # If the gripper is above the puck but not gripping it, put it around the puck
    if check("the robot's gripper is above the puck and the robot's gripper is not gripping it"):
        robot.drop("gripper around puck")
    # While the puck is gripping the gripper, try to push the puck towards the
    # goal. If the puck hits the wall, nudge it over and try again.
    while check("the robot's gripper is gripping the puck and the puck is not at the goal"):
        if check("the puck is behind the wall or has hit the wall"):
            robot.push("puck away from the wall")
        robot.slide("puck to the goal")