
    # Steps:
    #  1. Move the robot's gripper in front of the button
    #  2. Push the button through the wall with the robot's gripper
    # First, move the robot's gripper in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move("to front of button")
    # Now that the gripper is in front of the button, we can push the button
    # through the wall.
    # Check to make sure the gripper is lined up with the button from the side.
    if check("the robot's gripper is side aligned with the button"):
        robot.push("through wall")