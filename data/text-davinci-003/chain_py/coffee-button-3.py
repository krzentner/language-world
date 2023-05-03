
    # Steps:
    #  1. Line up the gripper forward of the button
    #  2. Push the button
    # We just need to line up the gripper forward of the button, so that the
    # button is in front of us.
    # It's probably better to line up the gripper as viewed from above rather than
    # as seen from the side, to get it as close to the button as possible.
    if check("the robot's gripper is not forward aligned with button and the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is lined up forward of the button, just push the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")