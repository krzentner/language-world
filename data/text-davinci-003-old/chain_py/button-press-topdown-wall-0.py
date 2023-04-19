
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the button from the top over the wall
    # We need to line up the gripper from above so that it's in front of the
    # button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, push down on the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is below the wall"):
        robot.push("down on button over wall")