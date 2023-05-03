# Steps:
    #  1. Put gripper above the coffee button
    #  2. Drop gripper around the coffee button
    #  3. Push the coffee button
    # First, put the gripper above the coffee button.
    if check("the robot's gripper is not above the coffee button"):
        robot.place("gripper above coffee button")
    # If the gripper isn't around the coffee button, put it around the coffee button.
    if check("the robot's gripper is not around the coffee button and the robot's gripper is open"):
        robot.drop("gripper around coffee button")
    # If the gripper is near the coffee button and open, maybe we can push it by closing
    # the gripper around the coffee button and then pushing.
    if check("the robot's gripper is near the coffee button and the robot's gripper is open"):
        robot.close("gripper around coffee button")
        robot.push("coffee button")
    # If we closed the gripper successfully and pushed the button, open the gripper again
    if check("the robot's gripper is closed and the button is pushed"):
        robot.drop("gripper open")