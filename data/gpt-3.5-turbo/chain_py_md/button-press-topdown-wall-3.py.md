# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move forward until the wall is detected
    #  3. Move left/right to position gripper over the button
    #  4. Push down on the button from the top
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Move forward until the wall is detected
    if check("the robot's front sensor sees a wall"):
        robot.move("right until the wall is not detected")
    # Move left/right to position the gripper over the button
    if check("the robot's gripper is not correctly positioned over the button"):
        robot.move("gripper left/right until it's positioned over the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")