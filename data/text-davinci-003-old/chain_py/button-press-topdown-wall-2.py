
    # Steps:
    #  1. Put the gripper over the top of the wall
    #  2. Line the gripper up with the button as viewed from above
    #  3. Put the gripper around the button
    #  4. Push down on the button
    # Put the gripper over the top of the wall but near the button, so that we can
    # sink the gripper down to the button over the wall.
    if check("the robot's gripper is not above the wall and the robot's gripper is below the button"):
        robot.put("gripper above the wall")
    # Once the gripper is above the wall, line up the gripper as viewed from
    # above with the button.
    if check("the robot's gripper is above the wall and the robot's gripper is not vertically aligned with the button from above"):
        robot.align("gripper to button from above")
    # Once the gripper is aligned with the button, lower the gripper so that it's
    # around the button.
    if check("the robot's gripper is vertically aligned with the button from above and the robot's gripper is not around the button"):
        robot.alight("gripper to button from above")
    # If the button is in the gripper, sink the gripper down and press the
    # button.
    if check("the robot's gripper is around the button"):
        robot.push("down on button")