# Steps:
    #  1. Put gripper above button
    #  2. Drop gripper onto button
    #  3. Push down on button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # As long as the gripper is above the button, drop it to push the button.
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.drop("gripper onto button")
    # Once the gripper is around the button, push down.
    if check("the robot's gripper is around button"):
        robot.push("button down")