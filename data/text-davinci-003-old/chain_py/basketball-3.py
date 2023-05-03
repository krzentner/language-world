
    # Steps:
    #  1. Put the gripper above the hoop
    #  2. Move gripper downwards in front of the hoop
    #  3. Drop the ball into the hoop
    # Put the gripper roughly above the hoop, as that should be close enough to
    # catch the ball.
    if check("the robot's gripper is not above the hoop"):
        robot.put("gripper above hoop")
    # When the gripper is above the hoop, move it just slightly below the hoop
    # so that when we drop the ball in, it has room to fall into the hoop.
    if check("the robot's gripper is above the hoop and the robot's gripper is not below the hoop"):
        robot.move("gripper downwards in front of the hoop")
    # When the gripper is below the hoop, we can drop the ball into the hoop.
    if check("the robot's gripper is below the hoop"):
        robot.drop("ball into hoop")