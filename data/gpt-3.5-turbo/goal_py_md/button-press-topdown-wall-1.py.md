# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    # 1. Move to the side of the wall
    # 2. Move the gripper above the button
    # 3. Move the gripper to the front of the button
    # 4. Move the gripper forward and push down on the button
    # 5. Move the gripper back up
    # 6. Move the gripper back to the side of the wall
    
    # Move robot to the side of the wall
    if check("the robot is not beside the wall"):
        robot.move("to the side of the wall")
    # Move the gripper above the button
    if check("the gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Move the gripper to the front of the button
    if check("the gripper is not almost vertically aligned with the button"):
        robot.move_gripper("almost vertically aligned with the button")
    # Move the gripper forward and push down on the button
    if check("the gripper is not above the button"):
        robot.move_gripper("near the button", close_gripper=True)
    # Move the gripper back up
    if check("the gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Move the gripper back to the side of the wall
    if check("the robot is not beside the wall"):
        robot.move("to the side of the wall")