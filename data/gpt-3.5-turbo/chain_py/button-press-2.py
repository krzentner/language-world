# Steps:
    #  1. Line up the gripper from the front
    #  2. Push the button from the front
    # Because this is "front", we need to line up the gripper from the front, which
    # is different than from above.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up from the front, just push the button.
    if check("the robot's gripper is aligned with button and the robot's gripper is not touching button"):
        robot.push("button")