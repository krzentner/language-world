# Steps:
    #  1. Line up the gripper as viewed from above, left of the short wall
    #  2. Move the gripper over the wall
    #  3. Push down on the button from the top
    # Because there is a wall in the way, we need to first line up the gripper to
    # the left of the wall.
    if check("the robot's gripper is not vertically aligned with button and the wall is between the robot's gripper and the button"):
        robot.put("gripper left of the wall and above the button")
    # Once the gripper is lined up left of the wall, move it over the wall.
    if check("the robot's gripper is left of the wall and the robot's gripper is not above the button"):
        robot.move("gripper over the wall")
    # Now that the gripper is over the wall and above the button, push down on the
    # button.
    if check("the robot's gripper is above the button"):
        robot.push("down on button")
