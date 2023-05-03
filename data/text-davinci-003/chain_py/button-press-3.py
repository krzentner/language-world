
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button
    # Although this isn't "topdown", we can still line up the robot's gripper
    # from above before pushing down.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is aligned with the button, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")