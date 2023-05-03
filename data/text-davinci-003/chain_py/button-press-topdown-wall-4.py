
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Rotate the gripper to the side to slide around the wall
    #  3. Push down on the button from the top
    # First, line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, rotate the gripper so it's sliding
    # against the wall instead of hitting it.
    # This step is necessary to go past the short wall blocking the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not against wall"):
        robot.rotate("gripper to side")
    # Now that the gripper is lined up alongside the wall, we can push down on
    # the button from the top.
    if check("the robot's gripper is vertically aligned with the button and the gripper is against wall"):
        robot.push("down on button")