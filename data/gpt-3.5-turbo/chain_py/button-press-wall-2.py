# Steps:
    #  1. Move gripper to position next to button
    #  2. Push wall aside with gripper
    #  3. Line up gripper with button
    #  4. Push down on button
    # We need to move the gripper to the position next to the button.
    if check("the robot's gripper is not next to the button and there is a wall in the way"):
        robot.push("wall aside")
        robot.move("gripper to position next to button")
    # Line up the robot's gripper with the button.
    if check("the robot's gripper is not lined up with button"):
        robot.move("gripper in front of button")
    # Push down on the button.
    if check("the robot's gripper is lined up with button"):
        robot.push("down on button")