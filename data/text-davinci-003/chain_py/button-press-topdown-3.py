
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop the gripper to the button
    #  3. Push the button
    #
    # First, put the gripper mostly above the button.
    if check("the robot's gripper is not almost vertically aligned with the button"):
        robot.put("gripper above button")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the button and the robot's gripper is open"):
        robot.put("gripper around the button")
    # As long as the gripper is still vertically aligned with the button,
    # it's being pressed, so keep pushing.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")