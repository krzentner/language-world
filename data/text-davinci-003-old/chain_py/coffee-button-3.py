
    # Steps:
    #  1. Put gripper above the button
    #  2. Put gripper around the button
    #  3. Push the button
    # We should put the gripper above the button to make sure we don't bump it
    # while trying to press it.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    # Once the gripper is lined up above the button, we should be able to press
    # it by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not around button"):
        robot.put("gripper around button")
    # Once the gripper is around the button, we can just press the button.
    if check("the robot's gripper is around button"):
        robot.push("button")