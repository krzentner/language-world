# Steps:
    #  1. Move gripper above the button, accounting for the wall
    #  2. "Peek" around the wall to make sure gripper is aligned with button
    #  3. Push down on the button from the top
    # Because there is a wall in the way, we need to move the gripper over the
    # wall before we can push the button down.
    # We'll first move the gripper above where the button is and then peek around
    # the wall to make sure the gripper is aligned with the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper above button, accounting for wall")
    if check("robot does not "peek" around the wall to make sure gripper is aligned with the button"):
        robot.peek("around the wall to make sure gripper is aligned with the button")
    # Once the gripper is lined up with the button from above, just push down on the button.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")