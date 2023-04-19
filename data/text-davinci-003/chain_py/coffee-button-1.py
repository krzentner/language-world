
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button
    # To press the button, we can just line up the gripper as seen from the
    # front.
    # Move the robot's gripper to the front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.place("gripper in front of button")
    # Once the gripper is lined up with the button, press the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")