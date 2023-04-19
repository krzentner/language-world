
    # Steps:
    #  1. Put gripper on top of the wall
    #  2. Align the gripper with the button, taking the wall into consideration
    #  3. Push down on the button from the top
    # First, move the gripper to the top of the wall.
    if check("the robot's gripper is not near the wall"):
        robot.move("gripper to top of wall")
    # Now that the gripper is above the wall, we can align it with the button,
    # but take the wall into account.
    if check("the robot's gripper is above the wall and the robot's gripper is not vertically aligned with button"):
        robot.align("gripper around wall with button")
    # Now that the gripper and button are aligned, we can push it down.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is above the button"):
        robot.push("down on button")