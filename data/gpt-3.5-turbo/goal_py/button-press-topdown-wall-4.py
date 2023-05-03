# Steps:
    # 1. Move the gripper above the button towards the wall
    # 2. Rotate the gripper to fit between the wall and the button
    # 3. Push down on the button from the top
    # First, move the gripper above the button towards the wall.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
        robot.move_gripper("near the wall")
    # Rotate the gripper to fit between the wall and the button.
    if check("the robot's gripper is not oriented correctly"):
        robot.rotate_gripper("aligned with the wall and button")
    # Push down on the button from the top.
    if check("the robot's gripper is correctly oriented"):
        robot.move_gripper("near the button")