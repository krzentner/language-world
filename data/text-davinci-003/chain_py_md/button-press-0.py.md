

Steps:
1. Align the gripper as viewed from in front
2. Push the button from the front

    # First, put the gripper in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up, just push on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("on button")