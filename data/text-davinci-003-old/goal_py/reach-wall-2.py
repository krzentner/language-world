
    # Steps:
    #  1. Reach towards the target with arm
    #  2. Push/slide arm over wall to target
    # If the robot's gripper is far enough away, we can just reach with the arm.
    # Lines of move the arm should help avoid the wall in the way and move the
    # gripper to the target.
    if check("the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")
    # If the robot's arm isn't yet above the wall, move it near the wall so that
    # it can move over the wall
    if check("the robot's arm is not above the wall"):
        robot.move_gripper("above the wall")
    # Once the arm is above the wall, move it to the right of the wall.
    if check("the robot's arm is above the wall and the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")