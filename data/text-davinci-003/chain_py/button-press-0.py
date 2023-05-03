
    # Steps:
    #  1. Line up the gripper with the button from the front
    #  2. Push down on the button from the front
    # The robot needs to line up the gripper with the button from the front before
    # it can push on the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.align("gripper with button")
    # Now that the gripper is lined up with the button, just push down on it.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")