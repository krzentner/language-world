
    # Steps:
    #  1. Move gripper above and around wall
    #  2. Put gripper above button
    #  3. Push down on the button from the top
    # We need to move the gripper above and around the wall in order to push the
    # button down.
    if check("the wall is in the way and the robot's gripper is not above and around the wall"):
        robot.put("the gripper above and around wall")
    # Once the gripper is around the wall, put it above the button.
    if check("the wall is out of the way and the robot's gripper is not above button"):
        robot.put("the gripper above the button")
    # Push the button.
    if check("the robot's gripper is above button"):
        robot.push("down on button")