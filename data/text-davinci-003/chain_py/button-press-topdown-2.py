
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around button and push downwards
    # First, line the gripper up above the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # Once the gripper is above the button, drop the gripper onto the button and
    # push downwards.
    if check("the robot's gripper is above button and the robot's gripper is not around button"):
        robot.drop("gripper around button and push down")
    # Keep pushing down if the gripper is still lined up with the button,
    # otherwise this means the button has been pressed.
    if check("the robot's gripper is around button"):
        robot.push("down on button")