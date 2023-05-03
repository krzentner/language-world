
    # Steps:
    #  1. Lineup the gripper as viewed from the side
    #  2. Push the button
    # First line up the gripper with the button from the side.
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.put("gripper beside the button")
    # Then push the button.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.push("the button")