
    # Steps:
    #  1. Move the gripper slightly right of the button
    #  2. Line up the gripper as viewed from above
    #  3. Push down on the button from the top
    # 
    # Since there is a wall blocking the robot's gripper from directly above the
    # button, we need to move the gripper slightly to the right and line up the
    # gripper as viewed from above.
    # Move the gripper slightly to the right of the button.
    if check("the gripper is left of the button"):
        robot.move("gripper right of button")
    # Now that the gripper is just right of the button, line it up with the
    # button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")