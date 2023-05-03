
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top with the wall in the way
    # If the wall is preventing the gripper from seeing the button, first move the
    # gripper around the wall until it can be seen.
    if check("the wall is preventing the robot's gripper from seeing the button"):
        robot.navigate("around wall")
    # Once the gripper can see the button, line it up from above.
    if check("the robot's gripper can see the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, Just push down on the button.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")