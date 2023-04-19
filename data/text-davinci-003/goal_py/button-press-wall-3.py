
    # Steps:
    #  1. Put the gripper in front of the button
    #  2. Push the button
    # If the gripper is not aligned with the button as seen from the front, move
    # it to the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("close to the button")
    # If there's a short wall between the gripper and the button, the gripper
    # should be close to the wall and aligned with the button as seen from the
    # front.
    if check("the robot's gripper is close to the wall and the robot's gripper is forward aligned with button"):
        robot.move_gripper("close to the button")