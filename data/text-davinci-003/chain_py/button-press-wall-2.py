
    # Steps:
    #  1. Put gripper left of wall
    #  2. Push wall away from the button
    #  3. Push the button
    # The robot needs to position the gripper near the wall.
    # The wall should block the robot's gripper from accessing the button,
    # so it needs to be moved.
    if check("the robot's gripper is not to left of wall"):
        robot.put("gripper to left of wall")
    # The robot needs to push the wall away to have access to the button.
    if check("the wall is left of the robot's gripper and the robot's gripper is not in front of the button"):
        robot.push("wall away from the button")
    # The robot can push the button once the wall is out of the way.
    if check("wall is to the left of the button and the robot's gripper is in front of the button"):
        robot.push("button")