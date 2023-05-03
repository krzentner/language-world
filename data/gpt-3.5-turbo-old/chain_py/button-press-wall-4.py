# Steps:
    #  1. Line up the gripper with the button from the front
    #  2. Push the gripper forward, bumping gently against the wall
    #  3. Push down on the button
    # Because there is a wall in the way, we need to bump against it gently and
    # then push down on the button. We start by lining up the gripper with the
    # button as seen from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    # Once the gripper is lined up with the button, we can move it forward to
    # gently bump against the wall.
    if check("the robot's gripper is horizontally aligned with button and the robot's gripper is not touching the wall"):
        robot.push("gripper forward gently")
    # Once the gripper is against the wall, we can push down on the button.
    if check("the robot's gripper is touching the wall"):
        robot.push("down on button")