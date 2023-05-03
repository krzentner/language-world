
    # Steps:
    #  1. Line up the gripper as viewed from above with the wall in the way
    #  2. Push down on the button from the top
    # Put the gripper above the button while avoiding the wall.
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.put("gripper above button, avoiding wall")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is almost vertically aligned with button"):
        robot.push("down on button")