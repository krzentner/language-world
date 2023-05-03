
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push on the button from the front
    # To use the front view, we want to line up the gripper from the front, and
    # this requires knowing which direction "right" is from.
    # Align the robot's gripper from the front
    if check("the robot's gripper is not forward aligned with button"):
        robot.align("gripper to button front")
    # Now that the gripper is lined up, push on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("on button front")