# Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button from the front
    # Because this is not "topdown", we need to line up the gripper from the
    # front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.align("gripper to button")
    # Now that the gripper is lined up, just push the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")