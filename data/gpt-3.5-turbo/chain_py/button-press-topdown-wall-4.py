# Steps:
    #  1. Move gripper to side of the wall
    #  2. Move gripper around the wall
    #  3. Line up gripper with button from above
    #  4. Push down on the button from above
    # Because there is a wall in the way, we need to move the gripper around it
    # to get to the button.
    # Move the gripper to the side of the wall
    if check("the robot's gripper is not beside the wall"):
        robot.move("gripper beside wall")
    # Move the gripper around the wall
    if check("the robot's gripper is beside the wall but not past it"):
        robot.move("gripper around wall")
    # With the gripper on the other side of the wall, line it up with the button
    # from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")