
    # Steps:
    #  1. Move gripper above wall
    #  2. Move gripper to left of button
    #  3. Move gripper around button and over wall
    #  4. Push button
    # If the gripper isn't above the wall, move it to the wall.
    if check("the robot's gripper is not above wall"):
        robot.grab("wall")
    # If the gripper is above the wall, move it to the left of the button.
    if check("the robot's gripper is above wall"):
        robot.move("gripper to left of button")
    # Once the gripper is to the left of the button, move it around the button
    # and over the wall.
    # This requires the robot to angle its arm down and away from the wall.
    if check("gripper is to left of button and the robot's gripper is not above wall and the robot's gripper is not above the button"):
        robot.put("gripper around button and over wall")
    # Finally, if the gripper is above the wall and the button, push the button.
    if check("the robot's gripper is above wall and the robot's gripper is above button"):
        robot.push("button")