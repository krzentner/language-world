# Steps:
    #  1. Position the gripper to the right of the wall
    #  2. Move the gripper over the wall and above the button
    #  3. Push down on the button from the top
    # If the robot's gripper is not to the right of the wall, move it there
    if check("the robot's gripper is not to the right of the wall"):
        robot.move("gripper to the right of the wall")
    # Once the gripper is positioned to the right of the wall, we can move it over
    # the wall and line up with the button from above.
    if check("the gripper is not above button"):
        robot.slide("gripper over the wall")
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")