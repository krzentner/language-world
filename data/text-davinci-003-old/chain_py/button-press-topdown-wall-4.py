
    # Steps:
    #  1. Put gripper above the wall
    #  2. Line up the gripper as viewed from above
    #  3. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Put the gripper above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")