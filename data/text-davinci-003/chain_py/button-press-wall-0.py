
    # Steps:
    #  1. Line up the gripper with the wall
    #  2. Put gripper behind wall
    #  3. Push the button from the front
    # We don't know how long the wall is, so we need to line up the gripper with
    # the wall first, so that it won't hit the wall while pushing.
    # Line up the gripper as seen from behind (into the wall).
    # This will also start to line up the gripper with the button.
    if check("the robot's gripper is not in line (vertically) with wall"):
        robot.put("gripper in line (vertically) with wall")
    # Now that the gripper is lined up with the wall, we need to move the
    # gripper behind the wall.
    if check("the robot's gripper is not behind wall"):
        robot.move("gripper as far behind wall as possible")
    # Once the gripper is behind the wall, it should be lined up with the
    # button, so just push the button.
    if check("the robot's gripper is behind wall"):
        robot.push("button from front")