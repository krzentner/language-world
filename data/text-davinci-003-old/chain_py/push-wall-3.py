
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide the puck towards the wall
    #  4. Push puck along the wall to the goal
    # First, put the gripper above the puck so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck towards the wall.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.slide("puck towards wall")
    # If the puck is near the wall, we can try to push it along the wall to the
    # goal.
    if check("the puck is near wall"):
        robot.push("puck along wall to goal")