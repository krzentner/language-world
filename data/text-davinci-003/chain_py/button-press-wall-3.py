
    # Steps:
    #  1. Line up gripper as viewed from the side
    #  2. Move the gripper to the side of the short wall
    #  3. Push down on the button from the wall side
    # First, line up the gripper from the side.
    if check("the robot's gripper is not horizontalaligned with the button and the robot's gripper is not forward aligned with the button"):
        robot.put("gripper to side of the wall")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is at the side of the wall and the robot's gripper is forward aligned with the button"):
        robot.push("down on button from the wall side")