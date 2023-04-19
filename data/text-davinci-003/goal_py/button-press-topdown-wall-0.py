
    # Steps:
    #  1. Put the gripper above the wall
    #  2. Put the gripper near the button while making sure the wall is still between the gripper and button
    #  3. Push down on the button from the top
    # First, put the gripper above the wall.
    if check("the robot's gripper is not vertically aligned with the wall"):
        robot.move_gripper("vertically aligned with the wall")
    # Make sure the wall is still between the gripper and the button by lining
    # up the gripper from the side.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("left of the button")
    # Once the gripper is lined up, just push down on the button.
    if check("the robot's gripper is above the wall and the robot's gripper is near the button"):
        robot.move_gripper("vertically aligned with the button")