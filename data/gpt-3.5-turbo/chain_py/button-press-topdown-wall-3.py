# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move the robot around the wall to get into pushing position
    #  3. Push down on the button from the top
    # Because there's a wall in the way, we need to first move the robot around
    # it to get into position to push the button.
    if check("the robot is not in position to push button"):
        robot.move_around("the wall")
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")