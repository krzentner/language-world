# Steps:
    #  1. Put gripper above coffee machine button
    #  2. Drop gripper around button
    #  3. Push down on button
    # First, put the gripper roughly above the coffee machine button.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.place("gripper above coffee machine button")
    # If the gripper isn't around the button, put it around the button.
    if check("the robot's gripper is not around button and the robot's gripper is open"):
        robot.drop("gripper around button")
    # If the gripper is near the button and open, maybe we can push it by closing
    # the gripper.
    if check("the robot's gripper is near button and the robot's gripper is open"):
        robot.close("gripper around button")
    # We closed the gripper, and the button is still near the gripper, so maybe we
    # have pressed it.
    if check("the robot's gripper is above button and the robot's gripper is closed"):
        robot.push("down on button")