# Steps:
    #  1. Put gripper above button
    #  2. Drop gripper onto button
    #  3. Push down on button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the gripper is above the button, drop it onto the button.
    if check("the robot's gripper is above button and the robot's gripper is open"):
        robot.drop("gripper onto button")
    # If the gripper is holding onto the button, push it down.
    if check("the robot's gripper is holding button"):
        robot.push("button down")