
    # Steps:
    #  1. Put gripper above button
    #  2. Line up gripper with button
    #  3. Push button
    # We need to put the gripper above the button before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is lined up above the button, we should be able to grab
    # the button by moving the gripper towards it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.put("gripper near button")
    # Once the gripper is near the button, we can just push the button.
    if check("the robot's gripper is near button"):
        robot.push("on button")