# Steps:
    #  1. Move the robot to the side of the wall
    #  2. Face the gripper towards the button
    #  3. Line up the gripper as viewed from above
    #  4. Push the gripper down on the button
    # To press the button while the wall is in the way, we need to position the
    # robot to the side of the wall first.
    if check("the robot is not positioned to the side of the wall"):
        robot.move("to the side of the wall")
    # Once we're positioned to the side of the wall, we need to rotate the
    # gripper so that it's facing the button.
    if check("the gripper is not facing the button"):
        robot.rotate("gripper towards button")
    # Next, we need to align the robot's gripper with the button from above.
    if check("the gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # Finally, we can push the gripper down on the button to press it while
    # taking the wall into account.
    if check("the gripper is vertically aligned with the button"):
        robot.push("down on button with wall in the way")