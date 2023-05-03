
    # Steps:
    #  1. Move the gripper directly under the hoop
    #  2. Drop the ball into the hoop
    # First, move the gripper directly under the hoop.
    if check("the robot's gripper is not below the hoop"):
        robot.move("gripper below hoop")
    # Once the gripper is under the hoop, we can just drop the ball into it.
    if check("the robot's gripper is below the hoop"):
        robot.drop("ball into hoop")