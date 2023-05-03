

# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper around the short wall with button behind it
    #  2. Reach around the short wall and line the robot's gripper up with button
    #  3. Push the button down
    # The button is behind a short wall and we can't see it.
    # The gripper won't be able to get around the wall, so we have to line up the
    # gripper with the wall and try to push the button down from behind.
    if check("the robot's gripper is not around the short wall"):
        robot.grab("short wall")
    # Now that the gripper is around the wall, we can reach around the wall
    # with the gripper.
    if check("the robot's gripper is around the short wall and the robot's gripper is not vertically aligned with the button"):
        robot.reach("gripper around wall to button")
    # Finally, if the gripper is forward aligned with the button, we can finally
    # push the button down.
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("down on button")