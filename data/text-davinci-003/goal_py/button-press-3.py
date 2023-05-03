
    # Steps:
    #  1. Line up the gripper forward as viewed from the side
    #  2. Push down on the button
    # Because this is "front", we should line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("aligned with the button from the side")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")