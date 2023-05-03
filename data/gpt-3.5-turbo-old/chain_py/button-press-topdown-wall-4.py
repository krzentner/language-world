# Steps:
    #  1. Put gripper above the button
    #  2. Move the gripper to the side to avoid the wall
    #  3. Move the gripper back above the button
    #  4. Push down on the button from the top

    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # If there is a wall to the side, move the gripper around the wall to the
    # button.
    if check("there is a wall blocking the gripper's direct path to the button"):
        robot.move("gripper around the wall")
    # Once the gripper is in position above the button, push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")