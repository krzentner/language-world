
    # Steps:
    #  1. Place gripper appropriately next to the wall
    #  2. Push the button
    # First, place the gripper appropriately next to the wall, so that we can
    # press the button while not touching the wall.
    if check("the robot's gripper is not aligned with the wall"):
        robot.move_gripper("aligned with the wall", close_gripper=True)
    # If the gripper is near the wall, but not in a position where it can press
    # the button, adjust its position.
    if check("the robot's gripper is not left of button"):
        robot.move_gripper("left of button")
    # Once the gripper is left of the button, just press the button.
    if check("the robot's gripper is left of button"):
        robot.move_gripper("near the button")