
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push on the button from the front
    # First, line up the gripper from the front. This could be done by looking
    # for the button's position from the front view and pointing the gripper
    # there.
    if check("the robot's gripper is not forward aligned with button and the robot's gripper is not vertical aligned with button"):
        robot.align("button to gripper")
    # Once the gripper is lined up, push on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")