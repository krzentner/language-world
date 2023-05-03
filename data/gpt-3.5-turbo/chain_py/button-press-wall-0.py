# Steps:
    #  1. Move gripper to side of wall
    #  2. Line up gripper with button
    #  3. Push gripper against wall to stabilize
    #  4. Push gripper into button
    # To press the button with a wall in the way, we need to first move the
    # gripper to the side of the wall so that it can be brought in front of the
    # button.
    if check("the robot's gripper is not clear of the wall"):
        robot.move("gripper to side of wall")
    # Once the gripper is to the side of the wall, line it up with the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # To stabilize the push, the robot can push against the wall with the
    # gripper.
    if check("the robot's gripper is vertically aligned with the button and near the wall"):
        robot.push("against wall")
    # While continuing to push against the wall for stability, push the gripper
    # into the button.
    if check("the robot's gripper is against the wall and the gripper is in front of the button"):
        robot.push("into button")