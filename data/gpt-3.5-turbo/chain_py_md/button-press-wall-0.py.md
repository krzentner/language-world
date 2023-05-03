# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Rotate the gripper to avoid the wall
    #  3. Push the button from the front
    # If the robot's gripper is not vertically aligned with the button, move the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # The gripper needs to be rotated to avoid the wall.
    # If the wall is on the left of the robot's gripper, rotate the gripper to the right.
    # If the wall is on the right of the robot's gripper, rotate the gripper to the left.
    if check("there is a wall in the way of the button and the robot's gripper"):
        if check("the wall is on the left of the robot's gripper"):
            robot.rotate("gripper to the right")
        else:
            robot.rotate("gripper to the left")
    # Once the gripper is rotated and near the button, push the button from the front.
    if check("the robot's gripper is near the button"):
        robot.push("button from the front")