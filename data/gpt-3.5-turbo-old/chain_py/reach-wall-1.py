# Steps:
    #  1. Move gripper over the wall
    #  2. Reach towards the target
    # To reach over the wall, we need to move the robot's arm over the wall before
    # reaching towards the target.
    if check("the robot's arm is not over the wall"):
        robot.move("arm over the wall")
    # Now that the robot's arm is over the wall, we can just reach towards the
    # target location.
    if check("the robot's arm is over the wall"):
        robot.reach("to goal")